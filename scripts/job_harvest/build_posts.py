#!/usr/bin/env python3
"""Process LinkedIn hiring posts -> cleaned records + DM/email drafts -> HIRING_POSTS.md.

Input:  scratchpad/jobpipe/linkedin_posts.json
Output: HIRING_POSTS.md (append mode, like NETWORKING.md)

JSON schema (one object per post):
  poster_name      str   — display name on LinkedIn
  poster_headline  str   — e.g. "Head of FP&A | Majid Al Futtaim"
  poster_url       str   — linkedin.com/in/... profile URL
  post_text        str   — full visible post text
  post_url         str   — linkedin.com/feed/update/... or activity URL
  date_label       str   — "1d", "3d", "1w", "1mo" etc. from LinkedIn
  emails_in_post   list  — emails extracted from post text (may be empty)
  has_dm_cta       bool  — post explicitly says "DM me" / "message me"
  likes            int   — reaction count (0 if unknown)
  comments         int   — comment count (0 if unknown)
  search_query     str   — which query surfaced this post
"""
import json, re, os, datetime

ROOT = "/Users/ashnad/my_career"
SRC  = os.path.join(ROOT, "scratchpad/jobpipe/linkedin_posts.json")
OUT  = os.path.join(ROOT, "HIRING_POSTS.md")
TODAY = datetime.date.today().isoformat()

EMAIL_RE = re.compile(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}')
JUNK_EMAIL = re.compile(r'example|noreply|no-reply|test@|sentry|wix|yourdomain', re.I)

# --- seniority filter ---
# Only surface posts from people who can hire or refer, not peers
KEEP_SENIORITY = re.compile(
    r'\b(cfo|chief financial|finance director|fp&a director|head of fp&a|head of finance|'
    r'vp finance|vice president finance|finance manager|fp&a manager|financial planning manager|'
    r'commercial finance manager|financial controller|controller|group finance|'
    r'hr |human resources|talent acquisition|recruiter|hiring manager|'
    r'people partner|talent partner|managing director|md\b|ceo|'
    r'director of finance|finance business partner|senior finance manager)\b',
    re.I
)
PEER_FILTER = re.compile(
    r'\b(financial analyst|fp&a analyst|senior analyst|finance analyst|'
    r'accountant|senior accountant|associate|intern|trainee|graduate|'
    r'executive\s+\-|executive\s+at\b)\b',
    re.I
)

# --- post relevance ---
ROLE_KW = re.compile(
    r'\b(fp&a|financial planning|financial analyst|finance analyst|'
    r'budgeting|forecasting|management reporting|financial reporting|'
    r'commercial finance|business partnering|variance analysis|'
    r'planning and analysis|planning & analysis|cost analyst|'
    r'budget analyst|financial modelling|financial modeling)\b',
    re.I
)
HIRING_KW = re.compile(
    r'\b(hiring|we.re hiring|looking for|seeking|open role|open position|'
    r'join (?:us|our team|the team)|send (?:your |me )?(?:cv|resume)|'
    r'dm me|message me|reach out|apply|opportunity|vacancy|vacancies|'
    r'feel free to (?:send|reach|dm)|drop (?:your|me))\b',
    re.I
)

UAE_KW = re.compile(r'\b(uae|dubai|abu dhabi|sharjah|difc|adgm|ajman|ras al khaimah)\b', re.I)


def is_relevant(p):
    """True if post is from a decision-maker/HR in the right domain."""
    headline = p.get("poster_headline", "")
    post_text = p.get("post_text", "")
    combined = headline + " " + post_text

    # must have hiring intent in post
    if not HIRING_KW.search(post_text):
        return False, "no hiring intent"

    # must mention a relevant role
    if not ROLE_KW.search(post_text):
        return False, "no role match"

    # must be UAE context
    if not UAE_KW.search(combined):
        return False, "no UAE context"

    # poster must be manager+ or HR
    if not KEEP_SENIORITY.search(headline):
        return False, "poster not senior enough"

    # skip peers even if they slip through
    if PEER_FILTER.search(headline) and not KEEP_SENIORITY.search(headline):
        return False, "peer-level poster"

    return True, "ok"


def legit_score(p):
    """Simple quality signal: higher = more trustworthy post."""
    score = 0
    headline = p.get("poster_headline", "")
    post_text = p.get("post_text", "")
    emails = p.get("emails_in_post", [])

    # engagement signals
    if p.get("likes", 0) >= 10:
        score += 2
    elif p.get("likes", 0) >= 3:
        score += 1
    if p.get("comments", 0) >= 3:
        score += 1

    # corporate email (not gmail/yahoo)
    for e in emails:
        dom = e.split("@")[-1].lower()
        if not re.search(r'gmail|yahoo|hotmail|outlook\.com', dom):
            score += 2

    # known Dubai/UAE employers relevant to FP&A
    for firm in ["majid al futtaim", "emaar", "damac", "aldar", "adnoc", "enoc",
                 "emirates", "flydubai", "etihad", "du ", "etisalat", "e&",
                 "mashreq", "fab", "emirates nbd", "adcb", "hsbc", "standard chartered",
                 "kpmg", "deloitte", "pwc", "ey ", "ernst & young",
                 "al futtaim", "al tayer", "chalhoub", "azizi", "nakheel",
                 "dp world", "port", "dewa", "sewa", "expo", "vision 2030"]:
        if firm.lower() in headline.lower():
            score += 1
            break

    # post has meaningful length
    if len(post_text) > 200:
        score += 1

    # penalise: recruiter agency spam
    if re.search(r'apply now|click here|submit your application|our client', post_text, re.I):
        score -= 1

    return score


def action_type(p):
    """Classify what Ashnad should do."""
    emails = [e for e in p.get("emails_in_post", []) if not JUNK_EMAIL.search(e)]
    if emails:
        return "EMAIL", emails[0]
    if p.get("has_dm_cta"):
        return "DM", None
    return "CONNECT", None


def _company_from_headline(headline):
    h = headline
    if " at " in h:
        c = h.split(" at ")[-1]
    elif " | " in h:
        c = h.split(" | ")[-1]
    else:
        return ""
    c = re.split(r'[|•,]', c)[0]
    c = re.sub(r',?\s*(Dubai|Abu Dhabi|UAE|MENA|GCC|Sharjah)\s*$', '', c, flags=re.I)
    return c.strip()


def _first_name(name):
    name = re.sub(r'•.*', '', name)
    name = re.split(r',', name)[0]
    name = re.sub(r'\s*[-–]\s*(MBA|CFA|CMA|ACCA|CPA|CA|CIA|PhD|MSc|FCCA|ACA)\b.*', '', name, flags=re.I)
    parts = [p for p in name.split() if p and not re.match(
        r'^(dr|mr|ms|mrs|eng|ca|cpa|cfa|cma|acca|aca|fcca|mba|cia)\.?$', p, re.I)]
    return parts[0] if parts else name.split()[0] if name.split() else name


def _role_hint(post_text):
    """Pull a short role phrase from the post for personalisation."""
    m = re.search(
        r'(?:looking for|seeking|hiring|role of|position of|join as)\s+(?:a\s+|an\s+)?'
        r'((?:senior |lead |head of |)(?:fp&a|financial analyst|finance analyst|'
        r'financial planning|budgeting|management reporting|commercial finance|'
        r'cost analyst|budget analyst)[^\.,\n]{0,30})',
        post_text, re.I
    )
    if m:
        return m.group(1).strip().rstrip('.,')
    return None


def draft_dm(p, action):
    fn = _first_name(p.get("poster_name", "there"))
    comp = _company_from_headline(p.get("poster_headline", ""))
    role_hint = _role_hint(p.get("post_text", ""))
    act, email = action

    role_str = f" for the {role_hint} role" if role_hint else ""
    comp_str = f" at {comp}" if comp else ""

    if act == "EMAIL":
        subject = "FP&A / Financial Analyst — Finance background, Dubai-based"
        body = (
            f"Hi {fn},\n\n"
            f"Saw your post{role_str}. I'm a finance professional based in Dubai with a background in "
            f"ERP systems implementation, financial reporting and P&L management at Promotech, and "
            f"prior tax advisory at EY. Looking to move into FP&A and this looks like a good fit{comp_str}.\n\n"
            f"Sending my CV across in case it's useful. Happy to have a quick call if the timing works.\n\n"
            f"Thanks,\nMuhammed Ashnad\nmuhammedashnad@gmail.com"
        )
        return f"**Subject:** {subject}\n\n**Body:**\n{body}"

    elif act == "DM":
        msg = (
            f"Hi {fn}, saw your post{role_str}. "
            f"I'm in Dubai, finance background covering ERP systems, financial reporting and P&L "
            f"at Promotech and tax advisory at EY. "
            f"Looking to move into FP&A. Happy to share my CV if it's still relevant."
        )
        if len(msg) > 300:
            msg = msg[:297] + "..."
        return f"**LinkedIn DM:**\n> {msg}"

    else:  # CONNECT
        msg = (
            f"Hi {fn}, came across your post on hiring{role_str}{comp_str}. "
            f"I'm in Dubai in finance, looking to move into FP&A. "
            f"Wanted to connect in case there's a fit."
        )
        if len(msg) > 200:
            msg = msg[:197] + "..."
        return f"**Connection note:**\n> {msg}"


if not os.path.exists(SRC):
    print(f"No posts file at {SRC}. Run LinkedIn posts harvest first.")
    exit(0)

# Load already-saved post URLs from HIRING_POSTS.md
_known_post_urls: set = set()
if os.path.exists(OUT):
    _hp_text = open(OUT, encoding="utf-8", errors="ignore").read()
    _known_post_urls = set(re.findall(r'https://www\.linkedin\.com/feed/update/[^\s)\]]+', _hp_text))
    _known_post_urls |= set(re.findall(r'\*\*Post:\*\*\s*(https://[^\s\n]+)', _hp_text))
    print(f"Loaded {len(_known_post_urls)} existing post URLs from HIRING_POSTS.md")

raw = json.load(open(SRC))
print(f"Loaded {len(raw)} raw posts from JSON.")

kept = []
skipped_dups = 0
for p in raw:
    # dedup against already-saved posts
    post_url = p.get("post_url", "").split("?")[0].rstrip("/")
    if post_url and post_url in _known_post_urls:
        skipped_dups += 1
        continue

    ok, reason = is_relevant(p)
    if not ok:
        print(f"  skip ({reason}): {p.get('poster_name','?')} — {p.get('poster_headline','')[:50]}")
        continue
    score = legit_score(p)
    if score < -1:
        print(f"  spam ({score}): {p.get('poster_name','?')}")
        continue
    p["_score"] = score
    p["_action"] = action_type(p)
    kept.append(p)

if skipped_dups:
    print(f"Skipped {skipped_dups} already-saved posts (dedup)")

# Sort: email actions first, then DM, then connect; within each by score desc
ACTION_ORDER = {"EMAIL": 0, "DM": 1, "CONNECT": 2}
kept.sort(key=lambda p: (ACTION_ORDER.get(p["_action"][0], 3), -p["_score"]))

print(f"Kept {len(kept)} relevant posts after filtering.")

# --- build section ---
section = [f"\n---\n\n## LinkedIn Hiring Posts — Batch {TODAY} ({len(kept)} posts)\n"]
section.append("**Sending is Ashnad's action.** Attach resume PDF to email outreach.\n")
section.append(f"Attach: `resumes/Muhammed_Ashnad_Resume.pdf`\n")

by_action = {"EMAIL": [], "DM": [], "CONNECT": []}
for p in kept:
    by_action[p["_action"][0]].append(p)

action_labels = {
    "EMAIL":   "Email Outreach (highest priority)",
    "DM":      "LinkedIn DM (post says DM me)",
    "CONNECT": "Connection + Context (reference their post)",
}

for act_key in ["EMAIL", "DM", "CONNECT"]:
    grp = by_action[act_key]
    if not grp:
        continue
    section.append(f"\n### {action_labels[act_key]} ({len(grp)})\n")

    for i, p in enumerate(grp, 1):
        name = p.get("poster_name", "Unknown")
        headline = p.get("poster_headline", "")
        profile_url = p.get("poster_url", "")
        post_url = p.get("post_url", "")
        post_snippet = p.get("post_text", "")[:280].replace("\n", " ").strip()
        date_label = p.get("date_label", "")
        score = p["_score"]
        act_detail = p["_action"]
        emails_in_post = [e for e in p.get("emails_in_post", []) if not JUNK_EMAIL.search(e)]
        query = p.get("search_query", "")
        dm_draft = draft_dm(p, act_detail)

        section.append(f"#### {i}. {name}")
        section.append(f"- **Headline:** {headline}")
        if profile_url:
            section.append(f"- **Profile:** {profile_url}")
        if post_url:
            section.append(f"- **Post:** {post_url}")
        section.append(f"- **Posted:** {date_label}  |  Legit score: {score}  |  Query: `{query}`")
        if emails_in_post:
            section.append(f"- **Email in post:** {', '.join(emails_in_post)}")
        section.append(f"- **Post preview:** _{post_snippet}..._")
        section.append(f"- **Status:** PENDING")
        section.append(f"- **Draft:**\n")
        section.append(f"  {dm_draft.replace(chr(10), chr(10)+'  ')}\n")
        section.append(f"- **Ashnad's response:** —\n")

with open(OUT, "a", encoding="utf-8") as f:
    f.write("\n".join(section) + "\n")

print(f"\nAppended {len(kept)} hiring posts to HIRING_POSTS.md")
counts = {k: len(v) for k, v in by_action.items() if v}
for k, n in counts.items():
    print(f"  {action_labels[k]}: {n}")

# my_career — Claude Session Context

This file documents the collaboration model, conventions, and context for working on the my_career project.

---

## Project Purpose

`my_career` is a personal career repository that tracks:
- **Career transition narrative** — from traditional finance (accounting operations) to trading platform building
- **Professional profiles** — detailed user profile, resume alignment, skills inventory
- **Growth & learning** — documenting expertise, values, and collaboration patterns
- **Version-controlled evolution** — every update committed + pushed, CHANGELOG + PENDING maintained

**Distinct from:** Ultimate Trading Terminal (product repo). This is the **career/personal brand** repo.

---

## Conventions (Match Ultimate Trading Terminal)

1. **Commit + push at every clean milestone** — no staging, no hoarding
2. **Timestamped entries** — `YYYY-MM-DD HH:MM` in +04 timezone
3. **State tracking** — CHANGELOG.md (done) + PENDING.md (open items)
4. **Clear specs** — documentation-first, verification requirements explicit
5. **Main branch only** — working branch, immediate push to origin/main

---

## Files & Their Purpose

| File | Purpose |
|---|---|
| **USER_PROFILE.md** | Comprehensive, evolving profile: role, competencies, work patterns, values, collaboration model. Updated as you provide new context. |
| **Muhammed_Ashnad_Resume.md** | Current resume (accounting operations focus). Needs reframing to align with actual capabilities. |
| **Ashnad_Career_Transition_Brief_for_Claude_Cowork.md** | Career transition context document (existing). To be integrated/updated. |
| **CHANGELOG.md** | Timestamped log of all changes (what was done, when). Never delete entries. |
| **PENDING.md** | Open items, decisions pending, backlog. Clear as items complete. |
| **CLAUDE.md** | This file — session context, conventions, collaboration patterns. |

---

## Collaboration Model

### How We Work Together (on this repo)

1. **You define** — what needs updating on your resume/profile, what narrative to tell
2. **I implement** — updates to docs, commits with clear messages, push to GitHub
3. **You validate** — review changes, suggest refinements
4. **Iterate** — quick feedback loop, commit each refinement

### Your Role
- Provide career context, goals, aspirations
- Validate/critique updates (does this sound right?)
- Decide on career narrative (what story do you want to tell?)
- Expand USER_PROFILE.md as you think of new details

### Claude's Role
- Maintain version control discipline (commit + push at every step)
- Reframe content to align capability with narrative
- Keep CHANGELOG + PENDING current and accurate
- Suggest improvements based on context (but you decide)

---

## Open Questions (for future sessions)

These are in PENDING.md as "Decisions Pending":

1. **Resume reframing approach:**
   - Expand current Promotech role to highlight systems/automation work?
   - Add separate "Personal Projects" section for trading platform?
   - Create entirely new resume highlighting both traditional finance + quant platform building?

2. **Career brand:**
   - "Trading Platform Builder"?
   - "Quantitative Trading Strategist"?
   - "AI-Powered Product Builder"?

3. **Public visibility:**
   - How much should the trading platform be public (GitHub, documentation)?
   - Should Ultimate Trading Terminal be listed on resume/portfolio?
   - LinkedIn profile alignment?

---

## Next Steps (from PENDING.md)

**Immediate:**
- [ ] Decide on resume reframing approach
- [ ] Update Muhammed_Ashnad_Resume.md to align with actual capabilities

**Follow-up:**
- [ ] Create career narrative document (the story you want to tell)
- [ ] Update LinkedIn profile
- [ ] Document the Ultimate Trading Terminal publicly (architecture, learnings)
- [ ] Define target roles/opportunities (what's next after current position?)

---

## Useful Patterns (from Ultimate Trading Terminal)

### Commit Message Format
```
Brief one-line summary of what changed

More context if needed (why, what impact, any notes).

Co-Authored-By: Claude Haiku 4.5 <noreply@anthropic.com>
```

### Example
```
Resume: reframe Promotech role to emphasize systems & automation work

Highlighted ERP migration project, data validation, workflow optimization 
to better reflect capability in technical problem-solving and product thinking.
Aligns resume with actual expertise in platform building.

Co-Authored-By: Claude Haiku 4.5 <noreply@anthropic.com>
```

---

**Last Updated:** 2026-08-20 00:20  
**Next Review:** As we make progress on career/resume updates

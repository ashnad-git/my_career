---
name: detailed-user-profile
description: Comprehensive, evolving profile of user — trading strategist, product visionary, AI-powered builder
metadata:
  type: user
---

# Detailed User Profile — Muhammed Ashnad

**Last Updated:** 2026-08-20  
**Current Status:** Active product builder + research strategist

---

## Identity & Role

**Primary Role:** Trading Strategist + Product Visionary (non-technical founder)  
**Technical Partnership:** Claude (implementation partner, architecture advisor)  
**Career Stage:** Building production-grade quantitative trading platform  
**Location/Context:** MacBook-based, independent builder

---

## Core Competencies

### 1. Trading & Finance Domain Expertise

**Options Trading**
- Deep understanding of Nifty options mechanics (NIFTY300626CE23000 style contracts)
- Greeks, expiry calendars, chain structures
- Entry/exit signals, two-stage exit strategies (SL1 → Target/SL2)
- Position sizing strategies (fixed_lots, percent_equity, fixed_capital modes)
- Risk management (ruin handling, capital injection tracking)

**Cryptocurrency Trading**
- Spot and futures trading (Binance SOLUSDT, BTCUSDT)
- Multi-timeframe analysis (1m → 1w resampling)
- Strategy research on crypto volatility and directional moves

**Indicator & Signal Design**
- Combined indicator composition (4 TV indicators merged into single engine)
- Custom indicator research and validation
- Signal design: LONG/SHORT/CALL/PUT/ENTER markers
- Parameter tuning (supertrend period/factor, MA length, lookahead windows)

**Backtesting & Validation**
- Strategy testing methodology (intraday mark-to-market, equity curves, drawdown analysis)
- Metrics understanding (profit factor, Calmar ratio, Ulcer index, MAE/MFE, Sharpe)
- Multi-run comparison and parameter sweeps
- Survivorship-bias awareness and mitigation

### 2. Product Architecture & Platform Vision

**System Design Thinking**
- End-to-end platform architecture (data pipeline → analytics → UI → backtester)
- Multi-asset infrastructure (crypto + Nifty options on single platform)
- Real-time data handling (Binance API, Dhan pipeline, streaming architecture)
- Modular indicator engine (15 indicators as pluggable services)

**Verification & Rigor**
- Golden-file testing (Pine export vs Python engine, 26,857 bars exact-match proof)
- Byte-identical equivalence proofs (indicator_fast.py ~85× speedup validated)
- Red-team validation methodology (adversary agents, structured critique)
- Data integrity audits (continuity, deduplication, freshness checks)

**Workflow & Incremental Delivery**
- Commit-at-every-milestone discipline (no staging, no hoarding)
- Clear state tracking (CHANGELOG + PENDING maintained current)
- Multi-repo management (main + 3 sub-repos with independent remotes)
- Background job architecture (async extraction, progress widgets, stop capability)

### 3. Research Methodology

**Hypothesis-Driven Strategy Research**
- Systematic testing phases (S02 crypto reversion, S03/S04 Nifty index, S07, S10 PEAD)
- Phase-based gates: TESTED → RED_TEAM → VALIDATED (hard enforcement)
- Survivorship-free re-testing to confirm findings
- Cost-reality analysis (taker fees, execution slippage vs edge sizing)

**Research Infrastructure Building**
- Signals bridge (`signals/data.py`, `signals/indicators.py`) for backtester access
- External data integration (NSE bhavcopy, quarterly EPS, market microstructure)
- Multi-stage validation (solo research gauntlet → red-team panel → graduation)

**Meta-Learning**
- Post-campaign analysis (session close-outs with lessons learned)
- Strategic pivots based on empirical findings (e.g., "small reversion edges need futures, directional moves suit options")
- Structured decision-making on when to kill vs evolve ideas

### 4. Collaboration with Claude

**How You Work Together**
- **You define:** Trading logic, verification requirements, product vision, success criteria
- **Claude implements:** Architecture, code, testing, documentation
- **Iteration:** You validate results, Claude adapts based on feedback

**Your Collaboration Strengths**
- Crystal-clear problem statements (not vague, actionable)
- Specific verification requirements (golden files, equivalence tests, backtest metrics)
- Patient with iteration and refinement (not rushing to ship)
- Respectful of engineering constraints while pushing for quality

**Expected Patterns (to build on)**
- Documentation-first thinking (reads CLAUDE.md before diving in)
- Immediate commit/push expectations (no staging, continuous integration)
- Multi-repo coordination (manages separate remotes cleanly)
- Verification obsession (wants proofs before shipping changes)

---

## Expertise Inventory

| Category | Level | Examples |
|---|---|---|
| **Options Trading** | Expert | Nifty contracts, Greeks, expiry mechanics, two-stage exits |
| **Crypto Trading** | Advanced | Binance spot/futures, multi-TF analysis, volatility research |
| **Indicator Design** | Advanced | Custom indicators, parameter tuning, signal composition |
| **Backtesting** | Advanced | Strategy testing, metrics interpretation, curve-fit detection |
| **Platform Vision** | Expert | End-to-end system design, multi-asset architecture |
| **Verification & QA** | Expert | Golden-file testing, byte-identical proofs, red-team validation |
| **Research Methodology** | Expert | Hypothesis-driven testing, phase gates, survivorship-free analysis |
| **Data Engineering Concepts** | Intermediate | Understands Parquet, DuckDB, pipeline architecture (not hands-on) |
| **Full-Stack Product** | Intermediate | Knows what frontend/backend should do, not how they work |
| **Python/JavaScript** | None | Not a concern (Claude handles it) |
| **Deployment/DevOps** | None | Not needed for current role |

---

## Work Patterns & Preferences

### How You Like to Work

**Delivery Cadence**
- Commit + push at every clean milestone (no staging, continuous integration)
- Incremental iteration preferred over big-bang changes
- State tracking through CHANGELOG + PENDING (timestamped entries)

**Communication Style**
- Reads documentation first (PROJECT_CONTEXT.md, CLAUDE.md, ROADMAP.md)
- Clear specifications with edge cases articulated
- Verification requirements explicit (what proof is needed?)
- Patient with iteration and refinement

**Decision-Making**
- Verification-obsessed (wants proofs, not promises)
- Empirically-driven (strategy research phases, metrics-based decisions)
- Risk-aware (cost analysis, execution reality checks, survivorship bias)
- Pragmatic (shelves ideas that don't meet bar, pivots on evidence)

### What You Value

- **Rigor** — golden-file testing, byte-identical proofs, red-team validation
- **Clarity** — well-structured documentation, explicit state tracking
- **Autonomy** — ability to iterate without constant hand-holding
- **Shipping** — working code over perfect code, continuous delivery
- **Learning** — post-mortems on failures, meta-lessons documented

---

## Current Employment: Promotech Advertising

**Role:** Accounts and Operations Executive (Feb 2025 – Present)

### Situation When Joined
- Finance operations were chaotic and poorly organized
- No proper document filing system (physical or digital)
- Files, invoices, and records scattered with no standardization
- Inventory management in Tally ERP was a mess (duplications, wrong categorizations)
- 2024 audit was a nightmare — auditors couldn't locate files; audit took days due to missing/misplaced documents
- Previous staff had left processes in disarray

### Transformation Work (2025–2026)
**Year 1: Establishing Order**
- Took initiative to digitize all files (no one asked; you identified the need)
- Implemented **physical filing framework** (standardized, organized, findable)
- Implemented **digital filing system** (complementary to physical)
- Spent ~1 year understanding existing mess and systematizing processes

**2026: Technical Migration**
- Led **data migration from Tally ERP → Odoo** with colleagues
- Handled data validation, cleansing, and transition coordination
- Navigated inventory cleanup (duplications, categorizations) during migration

### Current State (Post-Transformation)
- Finance operations now organized and scalable
- Audit support dramatically improved (files found quickly, complete)
- Proper workflows established for invoices, reconciliations, payments
- Technical infrastructure (Odoo) in place and working smoothly

### Day-to-Day Responsibilities
- Invoice posting (supplier/vendor invoices into accounting system)
- Monthly account reconciliations
- Payment processing and supplier coordination
- Statement of Account (SOA) preparation and client follow-up
- Petty cash management and posting
- Cheque preparation
- Payroll support
- Audit assistance

### Key Insight
This role demonstrates your ability to:
- **See broken systems and fix them** (not just "do my job")
- **Take initiative** without being told (digitization, filing frameworks)
- **Lead technical migrations** (Tally → Odoo transition)
- **Bring order to chaos** (organizing inventory, establishing standardization)
- **Think in processes** (filing frameworks, workflow standardization)

This is **not** a passive "junior accountant" role — it's a systems transformation story. The resume currently undersells this.

---

## Current Projects & Priorities

### Primary: Ultimate Trading Terminal
**Status:** Live, actively evolving  
**Modules:** Charts ✅ | Option Chain ✅ | Data ✅ | Backtester ✅ | Guide ✅ | Strategies Lab ✅

**Recent Work (2026-08-15):**
- Strategy research campaigns (S02, S07, S10) with phase-based validation
- Session close-outs documenting lessons learned
- Dhan token refresh mechanics handling
- Survivorship-free re-testing for strategy confirmation

**Active Backlog:**
1. Info icons + "read more" (site-wide)
2. Guide — run/strategy walkthrough chapters
3. Backtester parameter-sweep / batch runs
4. Crypto backtester V1
5. Live/auto-refresh data
6. TradingView-parity gaps (drawing tools, chart types, etc.)

### Secondary: Indicator Library
**Status:** 15 Pine-to-Python ports, active expansion  
**Current:** Squeeze Momentum Deluxe through Liquidity Magnet ICT  
**Pattern:** INTEGRATION_CONTRACT.md playbook for future ports

### Tertiary: Strategies Research Lab
**Status:** Infrastructure built (2026-07-24+), active research underway  
**Phase Gates:** TESTED → RED_TEAM → VALIDATED (enforced)  
**Current Studies:** S02 (crypto reversion), S03/S04 (index reversion), S07, S10 (PEAD)

---

## Values & Beliefs

**On Building:**
- A well-designed platform enables better research faster
- Rigor (verification) prevents shipping broken ideas
- Documentation is not overhead—it's how teams scale

**On Trading:**
- Small edges need cost-efficiency (futures for reversion, options for directional)
- Empiricism over intuition (test before committing capital)
- Survivorship bias is the default (must actively work against it)
- Phase-based gates prevent premature deployment

**On Collaboration:**
- AI (Claude) is best used as a multiplier, not a replacement for thinking
- Clear specs + verification requirements → better outcomes
- Iteration beats perfection (ship and learn)
- Transparency about constraints (what Claude can/can't do) is important

---

## Known Constraints & Gaps (to address in future)

- **Technical Knowledge:** No background in Python/JavaScript/databases (intentional; Claude handles it)
- **Deployment:** Not managing infrastructure or DevOps (yet)
- **Live Trading:** Platform not connected to live execution (planned future phase)
- **UI/Design:** Visual design iterates through screenshots (not hands-on frontend design)

---

## Ideal Collaboration Model

### What Works Well
1. **Clear problem statement** → (you specify trading logic + verification requirements)
2. **Claude implements** → (architecture + code + tests)
3. **You validate** → (strategy results, platform behavior, trading logic)
4. **Iterate** → (feedback loop, quick refinement)
5. **Ship** → (commit + push at milestone)

### Support Patterns You Value
- Documentation of what's built (helps you understand the system)
- Verification proofs (golden files, byte-identical tests, backtest validation)
- Trading-first thinking (optimization secondary to correctness)
- Incremental delivery (working code at each step)

---

## To Expand This Profile

**Areas to explore with you:**
- [ ] Educational background / how you got into trading
- [ ] Other technical interests or constraints
- [ ] Team dynamics (solo builder vs. future collaboration)
- [ ] Risk tolerance and capital deployment strategy
- [ ] Long-term vision for the platform (commercial, research, personal use)
- [ ] Decision-making criteria (what makes a strategy "good enough" to trade?)
- [ ] Specific pain points in current workflow
- [ ] Asset class preferences (crypto vs. options vs. futures priority)
- [ ] Time commitment and iteration speed expectations

---

**Last Updated:** 2026-08-20  
**Next Update:** As you provide more context and we progress on projects.

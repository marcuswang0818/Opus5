# 共享任务简报 / Shared Brief — "爆学分臻享版" 150.334 cr Plan

**Today:** 2026-09-13. Planning horizon starts **Fall 2026 Session A (26Fall-1st)**, which has
ALREADY begun — ASU ULC enrollment is assumed in progress as of now.

## Terminal credential (结算 / "settle-out" target)
**ASU Online — Bachelor of Arts in General Studies (BA GenStu)**
Two declared focus areas:
1. **Technology & Government** (tech policy / governance / regulation / public administration of tech)
2. **Socio-Technical Systems: Energy & Environment**, with an engineering slant toward
   **power electronics / power systems / grid** (converters, inverters, drives, grid integration,
   energy storage, renewables, energy policy & environmental impact)

## Hard constraints (user-specified, DO NOT renegotiate)
- **Total = exactly 150.334 US semester credits** ("仿佛五年本科的量" — a 5-year-bachelor's worth).
- Per-school quotas are FIXED:
  | # | School / platform | Quota (US semester credits) |
  |---|---|---|
  | 1 | SNHU Online | 12 |
  | 2 | Harvard Extension School (HES) | 12 |
  | 3 | ASU Universal Learner Courses (ULC), **session-based** | 42 |
  | 4 | UMPI YourPace (competency-based) — spread over **3 sessions** | 42 |
  | 5 | UCLA Extension | 21.334 (= 32 quarter units × 2/3) |
  | 6 | BYU Independent Study (BYU-IS) | 21 |
  | | **TOTAL** | **150.334** |
- **ASU 30-credit residency requirement is treated as WAIVED** (user instruction). Assume even
  IDS 321, IDS 402 and ASU 101 are satisfied by transfer equivalents taken at the six platforms.
  (Flag in notes that this is a user-imposed modeling assumption, not real ASU policy.)
- **BYU-IS rule:** every BYU-IS course must be planned to finish **inside a single semester-length
  window** — do NOT rely on the 1-year enrollment period. Pick courses that are realistically
  completable in ≤ 14 weeks.
- **UMPI rule:** exactly **3 YourPace sessions**, ~14 credits per session (flat-rate tuition ⇒
  credit-cramming is the whole point of the cost play).

## Optimization objective
- **80% primary goal:** take each school's *strongest* subject areas — "取百家之长".
- **20% secondary goal:** use the cheap external platforms to cut total cost — "省钱".
- **Student profile:** employed full-time, studying part-time, but with **top-20% available time
  and top-20% academic ability**. Aggressive but not fantasy load is acceptable.

## School strength assignments (guidance, refine with evidence)
- **SNHU** — cheap, 8-week terms, strong in business/IT/project-management style applied courses.
- **HES** — the prestige/depth slot: government, public policy, environmental science, data science.
- **ASU ULC** — cheapest per-credit general-education engine; ASU-native credit, no admission.
- **UMPI YourPace** — flat-rate competency-based: bulk business/management/leadership/analytics.
- **UCLA Extension** — engineering-grade certificate courses: power electronics, power systems,
  grid, renewables, sustainability. This is the power-electronics backbone.
- **BYU-IS** — cheap, self-paced, rigorous general-ed + math/physics/humanities fillers.

## What each Round-1 sub-agent must deliver
Write ONE file: `research/<NN>-<school-slug>.md` containing:
1. A prose section: tuition model, academic calendar (term names + typical start dates through 2028),
   enrollment/admission requirements, transferability to ASU, and why this school owns these subjects.
2. A human-readable course table.
3. A fenced ```json block (last thing in the file) with EXACTLY this shape:

```json
{
  "school": "...",
  "slug": "...",
  "credit_quota_semester": 0,
  "tuition_model": "...",
  "cost_basis_note": "verified 2026-09 | estimated from 20XX rate",
  "total_cost_usd": 0,
  "calendar": { "terms_per_year": 0, "term_length_weeks": 0, "term_names": ["..."] },
  "courses": [
    {
      "code": "ABC 123",
      "title": "...",
      "native_units": 3,
      "native_unit_type": "semester|quarter",
      "semester_credits": 3.0,
      "prereqs": ["..."],
      "asu_slot": "General Studies gen-ed (SB/SQ/HU/L/MA/CS/G/H/C) | Tech&Govt focus | SocioTech Energy focus | IDS core equiv | free elective",
      "focus_tag": "TECH-GOV | ENERGY-PE | GENED | IDS-CORE | ELECTIVE",
      "list_price_usd": 0,
      "weeks": 8,
      "notes": "..."
    }
  ],
  "strengths_rationale": "...",
  "risks": ["..."]
}
```

**Rules for sub-agents**
- `semester_credits` must sum to the quota EXACTLY. UCLA quarter units: semester = quarter × 2/3.
- Verify catalogs and 2026 prices with WebSearch/WebFetch where possible
  (load them first: `ToolSearch` with `select:WebSearch,WebFetch`). If a figure cannot be verified,
  keep it but label it `est.` in `cost_basis_note` and in `notes`. **Never invent a course code you
  did not see** — if unverified, say so in `notes` and keep the title generic but plausible.
- Prefer courses that map to the two focus areas; use gen-ed only where the degree needs it.
- Note prerequisites explicitly — Round 2 builds the prerequisite-ordered timeline.

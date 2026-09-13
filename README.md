# 爆学分臻享版 — 150.334-Credit Multi-School Course Plan

A planning repo for a single terminal credential — **ASU Online, BA in General Studies** —
assembled from **six** separate teaching platforms, at **exactly 150.334 US semester credits**
("仿佛五年本科的量" / roughly a five-year bachelor's worth of coursework).

## Declared focus areas
1. **Technology & Government**
2. **Socio-Technical Systems: Energy & Environment** — engineering slant toward
   **power electronics / power systems / grid**

## Credit allocation (fixed)

| # | Platform | Semester credits |
|---|----------|-----------------:|
| 1 | SNHU Online | 12 |
| 2 | Harvard Extension School | 12 |
| 3 | ASU Universal Learner Courses (session-based) | 42 |
| 4 | UMPI YourPace (3 sessions) | 42 |
| 5 | UCLA Extension (32 quarter units × 2/3) | 21.334 |
| 6 | BYU Independent Study | 21 |
| | **Total** | **150.334** |

## Method
- **Round 1** — six parallel sub-agents, one per platform: catalog + pricing research,
  course selection against that platform's genuine strengths, exact quota fill.
- **Round 2** — three sub-agents: degree-requirement review, duplicate-course removal,
  prerequisite-ordered timeline.
- **Output** — a single timeline / course / credit / cost sheet, published as an Artifact.

## Modeling assumptions (user-imposed)
- Start of horizon: **Fall 2026 Session A**, already under way (ASU ULC in progress).
- Student is **employed, studying part-time**, with top-20% available time and top-20% ability.
- ASU's **30-credit residency requirement is treated as waived**; ASU 101, IDS 321 and IDS 402
  are assumed satisfiable by transfer equivalents from the six platforms.
  *This is a planning assumption requested by the user, not current ASU policy.*
- 80% of the objective is subject quality ("取百家之长"); 20% is cost arbitrage ("省钱").

## Layout
```
research/00-SHARED-BRIEF.md   brief every Round-1 agent worked from
research/0N-<school>.md       per-platform research + course table + JSON payload
plan/aggregate.py             pulls the JSON payloads, validates quotas, totals cost
plan/aggregate.json           machine-readable merged plan
```

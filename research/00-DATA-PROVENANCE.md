# Data provenance & confidence convention

**Environment constraint (verified 2026-09-13):** this session's egress policy denies direct
HTTPS to university hosts — the agent proxy answers `403` to `CONNECT` for e.g. `www.snhu.edu`
and `courses.ulc.asu.edu`, and the same for catalog mirrors and archive.org. Per the proxy's
own guidance these denials must be reported, not routed around.

**Consequence:** every catalog fact and price in this repo comes from *indexed search results*,
not from a catalog page read in full. That is good enough to plan with and not good enough to
enroll on. Each figure therefore carries one of three confidence levels:

| Level | Meaning |
|-------|---------|
| **A — corroborated** | Two or more independent search results agree, or one result plus an internally consistent cross-check (e.g. per-credit rate × 120 cr matches the school's published program total). |
| **B — single source** | One indexed result, not contradicted. |
| **C — modeled** | Derived from a prior-year rate, a sibling course, or a stated policy; explicitly an estimate. |

**Rule for the final sheet:** the cost column shows the planned figure; the confidence column
shows A/B/C. Anything at level C is also called out in the caveats section. No course code is
presented as catalog-verified unless a search result actually showed that code.

**Before enrolling, re-verify in this order:** (1) the per-course price and the per-credit rate,
(2) that a non-degree / visiting student may actually register for that specific course,
(3) the prerequisite, (4) the term start date, (5) that ASU will accept the credit into the slot
this plan assigns it to.

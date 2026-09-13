#!/usr/bin/env python3
"""Aggregate + validate the six Round-1 school research files.

Each research/NN-*.md ends with a fenced ```json block describing that school's
course picks. This script pulls them out, checks the credit quotas hold, and
emits plan/aggregate.json for the timeline/artifact builders.
"""
import json, re, sys, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
RESEARCH = ROOT / "research"

QUOTAS = {
    "snhu": 12.0,
    "harvard-extension": 12.0,
    "asu-ulc": 42.0,
    "umpi-yourpace": 42.0,
    "ucla-extension": 64 / 3,   # 32 quarter units, reported as 21.334
    "byu-is": 21.0,
}
TOTAL_TARGET = 12 + 12 + 42 + 42 + 64 / 3 + 21   # 150.3333...


def extract_json(path):
    text = path.read_text(encoding="utf-8")
    blocks = re.findall(r"```json\s*\n(.*?)\n```", text, re.S)
    if not blocks:
        raise ValueError(f"{path.name}: no ```json block found")
    # the payload is the last json block in the file, per the shared brief
    for block in reversed(blocks):
        try:
            data = json.loads(block)
        except json.JSONDecodeError:
            continue
        if isinstance(data, dict) and "courses" in data:
            return data
    raise ValueError(f"{path.name}: no parseable payload block")


def main():
    schools, problems = [], []
    for path in sorted(RESEARCH.glob("[0-9][0-9]-*.md")):
        if path.stem.startswith("00-"):   # the shared brief, not a payload
            continue
        try:
            data = extract_json(path)
        except ValueError as exc:
            problems.append(str(exc))
            continue
        slug = data.get("slug") or path.stem.split("-", 1)[1]
        got = round(sum(float(c["semester_credits"]) for c in data["courses"]), 4)
        want = QUOTAS.get(slug)
        if want is None:
            problems.append(f"{path.name}: unknown slug {slug!r}")
        elif abs(got - want) > 0.005:
            problems.append(f"{slug}: credits sum to {got}, quota is {round(want,4)}")
        data["_slug"] = slug
        data["_credit_sum"] = got
        data["_course_count"] = len(data["courses"])
        data["_source_file"] = path.name
        schools.append(data)

    credits = round(sum(s["_credit_sum"] for s in schools), 4)
    cost = sum(float(s.get("total_cost_usd") or 0) for s in schools)
    courses = sum(s["_course_count"] for s in schools)

    print(f"{'school':<22}{'courses':>9}{'credits':>10}{'cost USD':>12}")
    print("-" * 53)
    for s in sorted(schools, key=lambda x: x["_source_file"]):
        print(f"{s['_slug']:<22}{s['_course_count']:>9}{s['_credit_sum']:>10.3f}"
              f"{float(s.get('total_cost_usd') or 0):>12,.0f}")
    print("-" * 53)
    print(f"{'TOTAL':<22}{courses:>9}{credits:>10.3f}{cost:>12,.0f}")
    print(f"\ntarget credits {TOTAL_TARGET:.4f} -> reported as 150.334")
    if abs(credits - TOTAL_TARGET) > 0.005:
        problems.append(f"grand total {credits} != target {round(TOTAL_TARGET,4)}")
    if credits:
        print(f"blended cost per credit: ${cost/credits:,.2f}")

    out = {
        "total_semester_credits": credits,
        "total_semester_credits_display": 150.334,
        "total_cost_usd": round(cost, 2),
        "total_courses": courses,
        "cost_per_credit": round(cost / credits, 2) if credits else None,
        "schools": schools,
    }
    (ROOT / "plan" / "aggregate.json").write_text(
        json.dumps(out, indent=2, ensure_ascii=False), encoding="utf-8")

    if problems:
        print("\nPROBLEMS:")
        for p in problems:
            print("  ! " + p)
        return 1
    print("\nall quotas check out.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

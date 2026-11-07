"""Regenerate the README's review index, badges, and chart from the reports."""

import argparse
from collections import Counter
from pathlib import Path
import re
from urllib.parse import quote


ROOT = Path(__file__).resolve().parents[1]
CHART = "assets/findings-by-impact.svg"
# File, company counted, display name, and the reader's main takeaway.
REVIEWS = (
    ("SquadStack.ai.md", "SquadStack.ai", "SquadStack.ai",
     "A customer result changes between the case study and the facts file."),
    ("Arcanna.ai.md", "Arcanna.ai", "Arcanna.ai",
     "The homepage omits the scope that makes named SOC outcomes useful."),
    ("Zaperon.md", "Zaperon", "Zaperon",
     "The reporting guide leaves buyers to verify integrity and retention controls."),
    ("Palm-Olympia.md", "Sam India", "Palm Olympia",
     "Similar-looking enquiry routes and image-only offers obscure the buying terms."),
    ("Massive GEO.md", "Massive", "Massive · machine-readable review",
     "Two public facts files disagree about the same company and its products."),
    ("ChainSecurity.md", "ChainSecurity", "ChainSecurity",
     "The audit PDFs contain proof buyers cannot scan on the website."),
    ("Bolt.new.md", "StackBlitz", "Bolt.new",
     "The homepage leaves out the technology behind Bolt's cost advantage."),
    ("Massive.md", "Massive", "Massive",
     "The public FAQ describes a business the company had already left."),
)

IMPACTS = {
    "High": "#f47782",
    "Medium": "#f4be66",
    "Low": "#64cba0",
    "Informational": "#87b4ff",
}
ICON = "[🔴🟠🟢🔵]"
IMPACT = "(" + "|".join(IMPACTS) + ")"
EFFORT = "(High|Medium|Low)"


def report_findings(path):
    text = (ROOT / path).read_text(encoding="utf-8")
    summary, details = text.split("## Summary of Findings\n", 1)[1].split(
        "## Detailed Findings\n", 1
    )
    details = details.split("\n## ", 1)[0]
    listed = re.findall(
        rf"^\|\s*\d+\s*\|.*\|\s*{ICON}\s*{IMPACT}\s*\|[ \t]*$",
        summary, re.MULTILINE,
    )
    scored = re.findall(
        rf"^\|[ \t]*{ICON}\s*{IMPACT}\s*\|[ \t]*{ICON}\s*{EFFORT}\s*\|",
        details.replace("**", ""), re.MULTILINE,
    )
    if not listed or listed != [impact for impact, _ in scored]:
        raise ValueError(f"{path}: summary and detailed finding scores differ")
    date_field = re.search(r"^\|\s*Date of review\s*\|([^|\n]+)\|", text, re.MULTILINE)
    dates = re.findall(r"(?:\d{1,2} )?[A-Z][a-z]+ \d{4}", date_field[1]) if date_field else []
    if not dates:
        raise ValueError(f"{path}: missing review date")
    return scored, dates[-1]


def replace_block(text, name, content):
    start, end = f"<!-- {name}:start -->", f"<!-- {name}:end -->"
    before, rest = text.split(start)
    _, after = rest.split(end)
    return f"{before}{start}\n{content}\n{end}{after}"


def findings_chart(counts):
    total = sum(counts.values())
    breakdown = ", ".join(f"{counts[label]} {label.lower()}" for label in IMPACTS)
    svg = [
        '<svg xmlns="http://www.w3.org/2000/svg" width="600" height="156" viewBox="0 0 600 156" role="img" aria-labelledby="title description">',
        '  <title id="title">Findings by impact</title>',
        f'  <desc id="description">{total} findings. {breakdown}.</desc>',
        '  <rect width="600" height="156" rx="12" fill="#182a44"/>',
        '  <g font-family="system-ui, -apple-system, Segoe UI, sans-serif" fill="#f3f6fc">',
        '    <text x="24" y="35" font-size="21" font-weight="700">Findings by impact</text>',
        f'    <text x="576" y="35" font-size="16" text-anchor="end" fill="#c8d5e8">{total} total</text>',
        '    <defs><clipPath id="bar"><rect x="24" y="52" width="552" height="23" rx="6"/></clipPath></defs>',
        '    <g clip-path="url(#bar)">',
    ]
    offset = 0
    for label, colour in IMPACTS.items():
        left = 24 + 552 * offset / total
        offset += counts[label]
        width = 24 + 552 * offset / total - left
        svg.append(f'      <rect x="{left:.3f}" y="52" width="{width:.3f}" height="23" fill="{colour}"/>')
    svg.append('    </g>')
    for i, (label, colour) in enumerate(IMPACTS.items()):
        x, y = 24 + i % 2 * 276, 106 + i // 2 * 26
        svg.append(f'    <circle cx="{x + 6}" cy="{y - 5}" r="6" fill="{colour}"/>')
        svg.append(f'    <text x="{x + 20}" y="{y}" font-size="16">{label} · {counts[label]}</text>')
    svg.extend(("  </g>", "</svg>"))
    return "\n".join(svg) + "\n", breakdown


def generated_files():
    counts = Counter()
    high_low = 0
    index = [
        "| Review | Key takeaway | Findings | Last checked |",
        "|:--|:--|--:|:--|",
    ]
    for path, _, name, takeaway in REVIEWS:
        findings, date = report_findings(path)
        counts.update(impact for impact, _ in findings)
        high_low += findings.count(("High", "Low"))
        index.append(f"| [{name}](./{quote(path)}) | {takeaway} | {len(findings)} | {date} |")

    badges = (
        ("published_reviews", len(REVIEWS), "published reviews", "1F3A5F"),
        ("companies_reviewed", len({review[1] for review in REVIEWS}), "companies reviewed", "1F3A5F"),
        ("documented_findings", sum(counts.values()), "documented findings", "1F3A5F"),
        ("high_impact", counts["High"], "high-impact findings", "CB2431"),
        ("high_impact_%2B_low_effort", high_low, "high-impact, low-effort opportunities", "2EA043"),
    )
    images = [
        f'  <img src="https://img.shields.io/badge/{key}-{number}-{colour}?style=flat-square" '
        f'alt="{number} {label}" height="24">'
        for key, number, label, colour in badges
    ]
    chart, breakdown = findings_chart(counts)
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    readme = replace_block(readme, "badges", "\n".join(["<p>", *images, "</p>"]))
    readme = replace_block(
        readme, "chart",
        f"![Findings by impact. {breakdown}.](./{CHART})\n\n"
        f"**{high_low} of {counts['High']} high-impact findings** have fixes estimated in hours.",
    )
    readme = replace_block(readme, "review-index", "\n".join(index))
    return {"README.md": readme, CHART: chart}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="report stale files without writing")
    args = parser.parse_args()
    for name, content in generated_files().items():
        path = ROOT / name
        if args.check:
            if not path.exists() or path.read_text(encoding="utf-8") != content:
                parser.exit(1, f"{name} is out of date. Run python3 scripts/update_readme.py.\n")
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")


if __name__ == "__main__":
    main()

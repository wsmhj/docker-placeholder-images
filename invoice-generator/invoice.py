#!/usr/bin/env python3
"""Minimal HTML invoice generator from JSON input."""
import argparse
import json
import sys
from datetime import date

DEMO = {
    "from": {"name": "Acme Co.", "address": "123 Main St"},
    "to":   {"name": "Client LLC", "address": "456 Market St"},
    "number": "INV-001",
    "date": str(date.today()),
    "items": [
        {"desc": "Consulting (hours)", "qty": 10, "rate": 120.0},
        {"desc": "Design review",      "qty": 1,  "rate": 350.0},
    ],
    "tax_rate": 0.0,
}

HTML = """<!doctype html>
<html><head><meta charset="utf-8"><title>Invoice {number}</title>
<style>
body{{font-family:sans-serif;max-width:720px;margin:2em auto;color:#222}}
table{{width:100%;border-collapse:collapse;margin-top:1em}}
th,td{{padding:.5em;border-bottom:1px solid #ddd;text-align:left}}
.right{{text-align:right}}
</style></head><body>
<h1>Invoice {number}</h1>
<p>Date: {date}</p>
<p><b>From:</b><br>{from_name}<br>{from_addr}</p>
<p><b>To:</b><br>{to_name}<br>{to_addr}</p>
<table>
<tr><th>Description</th><th class="right">Qty</th><th class="right">Rate</th><th class="right">Amount</th></tr>
{rows}
<tr><td colspan="3" class="right"><b>Subtotal</b></td><td class="right">${subtotal:,.2f}</td></tr>
<tr><td colspan="3" class="right"><b>Tax ({tax_rate}%)</b></td><td class="right">${tax:,.2f}</td></tr>
<tr><td colspan="3" class="right"><b>Total</b></td><td class="right"><b>${total:,.2f}</b></td></tr>
</table></body></html>"""


def render(data: dict) -> str:
    rows = []
    subtotal = 0.0
    for it in data["items"]:
        amt = it["qty"] * it["rate"]
        subtotal += amt
        rows.append(
            f'<tr><td>{it["desc"]}</td>'
            f'<td class="right">{it["qty"]}</td>'
            f'<td class="right">${it["rate"]:,.2f}</td>'
            f'<td class="right">${amt:,.2f}</td></tr>'
        )
    tax = subtotal * data.get("tax_rate", 0) / 100
    return HTML.format(
        number=data["number"], date=data["date"],
        from_name=data["from"]["name"], from_addr=data["from"]["address"],
        to_name=data["to"]["name"], to_addr=data["to"]["address"],
        rows="\n".join(rows),
        subtotal=subtotal, tax_rate=data.get("tax_rate", 0), tax=tax, total=subtotal + tax,
    )


def main() -> None:
    p = argparse.ArgumentParser(
        description="Render an HTML invoice from JSON. Pass --demo to print a sample."
    )
    p.add_argument("--input", help="JSON file (- for stdin)")
    p.add_argument("--demo", action="store_true", help="Render a demo invoice")
    args = p.parse_args()

    if args.demo or not args.input:
        data = DEMO
    elif args.input == "-":
        data = json.load(sys.stdin)
    else:
        with open(args.input) as f:
            data = json.load(f)
    sys.stdout.write(render(data))


if __name__ == "__main__":
    main()

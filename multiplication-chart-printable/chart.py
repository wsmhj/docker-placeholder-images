#!/usr/bin/env python3
"""Render a multiplication chart as ASCII or HTML."""
import argparse


def ascii_table(n: int) -> str:
    width = len(str(n * n)) + 1
    lines = []
    header = " " * width + "".join(f"{c:>{width}}" for c in range(1, n + 1))
    lines.append(header)
    lines.append("-" * len(header))
    for r in range(1, n + 1):
        row = f"{r:>{width - 1}}|" + "".join(f"{r * c:>{width}}" for c in range(1, n + 1))
        lines.append(row)
    return "\n".join(lines)


def html_table(n: int) -> str:
    rows = [
        '<table border="1" cellpadding="6" '
        'style="border-collapse:collapse;font-family:monospace">'
    ]
    rows.append("<tr><th></th>" + "".join(f"<th>{c}</th>" for c in range(1, n + 1)) + "</tr>")
    for r in range(1, n + 1):
        rows.append(
            f"<tr><th>{r}</th>"
            + "".join(f"<td>{r * c}</td>" for c in range(1, n + 1))
            + "</tr>"
        )
    rows.append("</table>")
    return "\n".join(rows)


def main():
    p = argparse.ArgumentParser(description="Print a multiplication chart of size N.")
    p.add_argument("--size", type=int, default=12, help="Chart size (default 12)")
    p.add_argument("--format", choices=["ascii", "html"], default="ascii")
    args = p.parse_args()
    print(ascii_table(args.size) if args.format == "ascii" else html_table(args.size))


if __name__ == "__main__":
    main()

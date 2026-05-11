#!/usr/bin/env python3
"""Generate printable graph paper as SVG."""
import argparse


def main() -> None:
    p = argparse.ArgumentParser(description="Render printable graph paper as SVG to stdout.")
    p.add_argument("--width", type=float, default=8.5, help="Width in inches (default 8.5)")
    p.add_argument("--height", type=float, default=11.0, help="Height in inches (default 11)")
    p.add_argument("--grid", type=float, default=0.25, help="Grid size in inches (default 0.25)")
    p.add_argument("--major", type=int, default=4, help="Major gridline every N cells (default 4)")
    args = p.parse_args()

    dpi = 96
    w = args.width * dpi
    h = args.height * dpi
    g = args.grid * dpi

    lines = []
    i = 0
    x = 0.0
    while x <= w + 0.001:
        sw = 1.0 if i % args.major == 0 else 0.4
        op = 0.6 if i % args.major == 0 else 0.3
        lines.append(
            f'<line x1="{x:.2f}" y1="0" x2="{x:.2f}" y2="{h:.2f}" '
            f'stroke="#000" stroke-width="{sw}" opacity="{op}"/>'
        )
        x += g
        i += 1

    i = 0
    y = 0.0
    while y <= h + 0.001:
        sw = 1.0 if i % args.major == 0 else 0.4
        op = 0.6 if i % args.major == 0 else 0.3
        lines.append(
            f'<line x1="0" y1="{y:.2f}" x2="{w:.2f}" y2="{y:.2f}" '
            f'stroke="#000" stroke-width="{sw}" opacity="{op}"/>'
        )
        y += g
        i += 1

    print(
        f'<svg xmlns="http://www.w3.org/2000/svg" '
        f'width="{args.width}in" height="{args.height}in" '
        f'viewBox="0 0 {w} {h}">'
    )
    print("\n".join(lines))
    print("</svg>")


if __name__ == "__main__":
    main()

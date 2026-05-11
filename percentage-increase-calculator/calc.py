#!/usr/bin/env python3
"""Percentage increase / decrease calculator."""
import argparse


def main() -> None:
    p = argparse.ArgumentParser(description="Compute percentage change between two values.")
    p.add_argument("--from", dest="src", type=float, required=True, help="Original value")
    p.add_argument("--to", dest="dst", type=float, required=True, help="New value")
    args = p.parse_args()

    if args.src == 0:
        print("Original value is 0 — percentage change is undefined.")
        return

    diff = args.dst - args.src
    pct = diff / abs(args.src) * 100
    label = "increase" if diff >= 0 else "decrease"
    print(f"From:        {args.src}")
    print(f"To:          {args.dst}")
    print(f"Absolute:    {diff:+.4f}")
    print(f"Percentage:  {pct:+.2f}% ({label})")


if __name__ == "__main__":
    main()

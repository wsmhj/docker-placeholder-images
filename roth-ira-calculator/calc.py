#!/usr/bin/env python3
"""Roth IRA balance projection with annual contributions and compound growth."""
import argparse


def main() -> None:
    p = argparse.ArgumentParser(
        description="Project Roth IRA balance with annual contributions and compound growth."
    )
    p.add_argument("--balance", type=float, default=0.0, help="Current balance (default 0)")
    p.add_argument("--annual", type=float, required=True, help="Annual contribution")
    p.add_argument("--years", type=int, required=True, help="Years to project")
    p.add_argument("--rate", type=float, required=True, help="Expected annual return %%, e.g. 7")
    args = p.parse_args()

    r = args.rate / 100
    balance = args.balance
    total_contrib = args.balance
    print(f"{'Year':>5}  {'Contrib':>12}  {'Growth':>12}  {'Balance':>14}")
    for y in range(1, args.years + 1):
        growth = balance * r
        balance += growth + args.annual
        total_contrib += args.annual
        print(f"{y:>5}  ${args.annual:>11,.0f}  ${growth:>11,.2f}  ${balance:>13,.2f}")
    print()
    print(f"Total contributed: ${total_contrib:,.2f}")
    print(f"Final balance:     ${balance:,.2f}")
    print(f"Total growth:      ${balance - total_contrib:,.2f}")


if __name__ == "__main__":
    main()

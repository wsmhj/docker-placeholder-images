#!/usr/bin/env python3
"""Auto loan / car payment calculator."""
import argparse
import sys


def monthly_payment(principal: float, annual_rate: float, term_months: int) -> float:
    if annual_rate == 0:
        return principal / term_months
    r = annual_rate / 100 / 12
    return principal * (r * (1 + r) ** term_months) / ((1 + r) ** term_months - 1)


def main() -> None:
    p = argparse.ArgumentParser(
        description="Compute monthly payment, total interest, and total cost for an auto loan."
    )
    p.add_argument("--price", type=float, required=True, help="Vehicle price")
    p.add_argument("--down", type=float, default=0.0, help="Down payment (default 0)")
    p.add_argument("--trade-in", type=float, default=0.0, help="Trade-in value (default 0)")
    p.add_argument("--rate", type=float, required=True, help="Annual interest rate (APR), e.g. 6.5")
    p.add_argument("--term", type=int, required=True, help="Loan term in months, e.g. 60")
    p.add_argument("--tax", type=float, default=0.0, help="Sales tax rate %% (default 0)")
    args = p.parse_args()

    taxable = max(args.price - args.trade_in, 0.0)
    tax_amount = taxable * args.tax / 100
    loan = args.price + tax_amount - args.down - args.trade_in
    if loan <= 0:
        print("Loan amount is zero or negative — no financing needed.", file=sys.stderr)
        sys.exit(1)

    pmt = monthly_payment(loan, args.rate, args.term)
    total = pmt * args.term
    interest = total - loan
    print(f"Loan amount:     ${loan:,.2f}")
    print(f"Monthly payment: ${pmt:,.2f}")
    print(f"Total interest:  ${interest:,.2f}")
    print(f"Total paid:      ${total:,.2f}")


if __name__ == "__main__":
    main()

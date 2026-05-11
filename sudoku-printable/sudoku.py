#!/usr/bin/env python3
"""Generate a printable sudoku puzzle as an ASCII grid."""
import argparse
import random


def base_grid():
    def pattern(r, c):
        return (3 * (r % 3) + r // 3 + c) % 9

    rows = [g * 3 + r for g in random.sample(range(3), 3) for r in random.sample(range(3), 3)]
    cols = [g * 3 + c for g in random.sample(range(3), 3) for c in random.sample(range(3), 3)]
    nums = random.sample(range(1, 10), 9)
    return [[nums[pattern(r, c)] for c in cols] for r in rows]


def punch(grid, holes):
    cells = [(r, c) for r in range(9) for c in range(9)]
    random.shuffle(cells)
    for r, c in cells[:holes]:
        grid[r][c] = 0
    return grid


def render(grid):
    out = []
    for r in range(9):
        if r % 3 == 0 and r > 0:
            out.append("------+-------+------")
        row = []
        for c in range(9):
            if c % 3 == 0 and c > 0:
                row.append("|")
            v = grid[r][c]
            row.append(str(v) if v else ".")
        out.append(" ".join(row))
    return "\n".join(out)


def main():
    p = argparse.ArgumentParser(description="Print a sudoku puzzle to stdout.")
    p.add_argument("--difficulty", choices=["easy", "medium", "hard"], default="medium")
    p.add_argument("--seed", type=int, help="Random seed for reproducibility")
    args = p.parse_args()

    if args.seed is not None:
        random.seed(args.seed)
    holes = {"easy": 35, "medium": 45, "hard": 55}[args.difficulty]
    grid = punch(base_grid(), holes)
    print(render(grid))


if __name__ == "__main__":
    main()

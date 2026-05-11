#!/usr/bin/env python3
"""Render a simple floor plan from a JSON room spec to ASCII art."""
import argparse
import json
import sys

DEMO = {
    "scale": 1,
    "rooms": [
        {"name": "Living",  "x": 0,  "y": 0,  "w": 16, "h": 10},
        {"name": "Kitchen", "x": 16, "y": 0,  "w": 10, "h": 10},
        {"name": "Bed1",    "x": 0,  "y": 10, "w": 12, "h": 8},
        {"name": "Bed2",    "x": 12, "y": 10, "w": 8,  "h": 8},
        {"name": "Bath",    "x": 20, "y": 10, "w": 6,  "h": 8},
    ],
}


def render(spec: dict) -> str:
    rooms = spec["rooms"]
    w = max(r["x"] + r["w"] for r in rooms) + 1
    h = max(r["y"] + r["h"] for r in rooms) + 1
    grid = [[" "] * w for _ in range(h)]
    for r in rooms:
        for x in range(r["x"], r["x"] + r["w"]):
            grid[r["y"]][x] = "-"
            grid[r["y"] + r["h"] - 1][x] = "-"
        for y in range(r["y"], r["y"] + r["h"]):
            grid[y][r["x"]] = "|"
            grid[y][r["x"] + r["w"] - 1] = "|"
        ty = r["y"] + r["h"] // 2
        for i, ch in enumerate(r["name"]):
            tx = r["x"] + 2 + i
            if tx < r["x"] + r["w"] - 1:
                grid[ty][tx] = ch
    return "\n".join("".join(row) for row in grid)


def main():
    p = argparse.ArgumentParser(
        description="Convert a floor-plan JSON spec to ASCII art. Use --demo for a sample."
    )
    p.add_argument("--input", help="JSON spec file, or - for stdin")
    p.add_argument("--demo", action="store_true", help="Render a demo apartment layout")
    args = p.parse_args()

    if args.demo or not args.input:
        spec = DEMO
    elif args.input == "-":
        spec = json.load(sys.stdin)
    else:
        with open(args.input) as f:
            spec = json.load(f)
    print(render(spec))


if __name__ == "__main__":
    main()

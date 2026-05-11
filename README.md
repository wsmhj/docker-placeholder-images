# docker-placeholder-images

A collection of small command-line utility images. Each image is a single-purpose
CLI built on `python:3.12-alpine` with no runtime dependencies.

| Image | Purpose |
|-------|---------|
| `wsmhj/car-payment-calculator`         | Auto loan amortization calculator |
| `wsmhj/percentage-increase-calculator` | Percentage change between two values |
| `wsmhj/roth-ira-calculator`            | Roth IRA balance growth projection |
| `wsmhj/invoice-generator`              | Render an HTML invoice from JSON |
| `wsmhj/printable-graph-paper`          | Generate SVG graph paper |
| `wsmhj/sudoku-printable`               | Generate a printable sudoku puzzle |
| `wsmhj/multiplication-chart-printable` | ASCII / HTML multiplication chart |
| `wsmhj/floorplan-ai`                   | ASCII floor plan from a JSON room spec |

## Usage

Each image runs as a CLI. Examples:

```bash
docker run --rm wsmhj/car-payment-calculator \
  --price 30000 --rate 6.5 --term 60

docker run --rm wsmhj/percentage-increase-calculator \
  --from 50 --to 75

docker run --rm wsmhj/sudoku-printable --difficulty hard
```

Run with `--help` (the default `CMD`) for full options.

## Build locally

```bash
docker build -t local/car-payment-calculator ./car-payment-calculator
```

## CI

`.github/workflows/build-and-push.yml` builds all images for `linux/amd64`
and `linux/arm64` and pushes `:latest` and `:1.0.0` tags to Docker Hub.
Requires repository secrets `DOCKERHUB_USERNAME` and `DOCKERHUB_TOKEN`.

## License

MIT

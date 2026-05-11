FROM python:3.12-alpine

LABEL org.opencontainers.image.title="Multiplication Chart Printable"
LABEL org.opencontainers.image.description="CLI that renders a printable multiplication chart as ASCII or HTML."
LABEL org.opencontainers.image.source="https://github.com/wsmhj/docker-placeholder-images"
LABEL org.opencontainers.image.version="1.0.0"
LABEL org.opencontainers.image.licenses="MIT"

WORKDIR /app
COPY chart.py /app/chart.py

ENTRYPOINT ["python", "/app/chart.py"]
CMD ["--help"]

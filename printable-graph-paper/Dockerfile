FROM python:3.12-alpine

LABEL org.opencontainers.image.title="Printable Graph Paper"
LABEL org.opencontainers.image.description="CLI that renders printable graph paper as SVG with configurable grid size."
LABEL org.opencontainers.image.source="https://github.com/wsmhj/docker-placeholder-images"
LABEL org.opencontainers.image.version="1.0.0"
LABEL org.opencontainers.image.licenses="MIT"

WORKDIR /app
COPY graph.py /app/graph.py

ENTRYPOINT ["python", "/app/graph.py"]
CMD ["--help"]

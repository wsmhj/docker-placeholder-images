FROM python:3.12-alpine

LABEL org.opencontainers.image.title="Invoice Generator"
LABEL org.opencontainers.image.description="Minimal HTML invoice generator that renders an invoice from a JSON spec."
LABEL org.opencontainers.image.source="https://github.com/wsmhj/docker-placeholder-images"
LABEL org.opencontainers.image.version="1.0.0"
LABEL org.opencontainers.image.licenses="MIT"

WORKDIR /app
COPY invoice.py /app/invoice.py

ENTRYPOINT ["python", "/app/invoice.py"]
CMD ["--help"]

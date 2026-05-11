FROM python:3.12-alpine

LABEL org.opencontainers.image.title="Car Payment Calculator"
LABEL org.opencontainers.image.description="CLI to compute monthly payment, total interest, and total cost for an auto loan."
LABEL org.opencontainers.image.source="https://github.com/wsmhj/docker-placeholder-images"
LABEL org.opencontainers.image.version="1.0.0"
LABEL org.opencontainers.image.licenses="MIT"

WORKDIR /app
COPY calc.py /app/calc.py

ENTRYPOINT ["python", "/app/calc.py"]
CMD ["--help"]

FROM python:3.12-alpine

LABEL org.opencontainers.image.title="Floorplan AI"
LABEL org.opencontainers.image.description="CLI helper that converts a JSON room spec into a simple ASCII floor plan."
LABEL org.opencontainers.image.source="https://github.com/wsmhj/docker-placeholder-images"
LABEL org.opencontainers.image.version="1.0.0"
LABEL org.opencontainers.image.licenses="MIT"

WORKDIR /app
COPY floorplan.py /app/floorplan.py

ENTRYPOINT ["python", "/app/floorplan.py"]
CMD ["--help"]

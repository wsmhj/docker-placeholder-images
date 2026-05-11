FROM python:3.12-alpine

LABEL org.opencontainers.image.title="Sudoku Printable"
LABEL org.opencontainers.image.description="CLI that generates printable sudoku puzzles with selectable difficulty."
LABEL org.opencontainers.image.source="https://github.com/wsmhj/docker-placeholder-images"
LABEL org.opencontainers.image.version="1.0.0"
LABEL org.opencontainers.image.licenses="MIT"

WORKDIR /app
COPY sudoku.py /app/sudoku.py

ENTRYPOINT ["python", "/app/sudoku.py"]
CMD ["--help"]

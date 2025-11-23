FROM mcr.microsoft.com/devcontainers/python:3.11

# Init uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
ENV UV_PROJECT_ENVIRONMENT="/home/vscode/.venv"
ENV PATH="/home/vscode/.venv/bin:$PATH"
FROM mcr.microsoft.com/devcontainers/python:3.11

# Init uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
USER vscode
ENV VIRTUAL_ENV="/home/vscode/.venv" 
ENV UV_PROJECT_ENVIRONMENT="$VIRTUAL_ENV"
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN uv venv $VIRTUAL_ENV
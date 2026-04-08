# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

```bash
# Run all non-integration tests (no Ollama required)
uv run pytest -m "not integration"

# Run integration tests (requires a running Ollama/LM Studio instance at settings.yaml base_url)
uv run pytest -m integration

# Lint
uv run ruff check src/ tests/

# Type-check
uv run mypy src/
```

## Architecture

The system has three independent pipeline layers, each mirroring the same structural pattern:

```
src/
├── core/ # base module
├── module/ # any new functionality
```

The modules shall have dependcies only in one direction. The base functions and models are in core.


### Configuration

Always move configurable values like llm-settings to the settings.yaml.
`settings.yaml` at project root. Key fields:
- Here add key fields

### Test structure

```
tests/
├── data/                    # test data files
├── module [...]
```

Integration tests use `@pytest.mark.integration` and require the Ollama endpoint from `settings.yaml` to be reachable. Unit tests mock at the library boundary and run without any external services.

### Implementation Rules

- Never expose document data from test data in prompts or code snippet like model descriptions.
- Always add tests.
- In integration tests, use the real LLM client pointing to the test instance, never a mock.
- In unit tests, mock the LLM client to return fixed responses, never using the real client or test instance.
- Run always all tests and linting checks after you finished changes.
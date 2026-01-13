# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This repository generates the curated "awesome" list for Senzing software and resources. It's a Python CLI tool that queries GitHub's API to fetch repository information from the Senzing organization, categorizes them by topic, and generates the README.md markdown file.

## Development Commands

### Setup

```bash
python -m venv ./venv
source ./venv/bin/activate
python -m pip install --upgrade pip
python -m pip install --group all .
```

### Linting (run all before committing)

```bash
black --check $(git ls-files '*.py' ':!:docs/source/*')
flake8 src/
pylint $(git ls-files '*.py' ':!:docs/source/*')
mypy $(git ls-files '*.py' ':!:docs/source/*')
isort --check src/
```

### Running the Tool

Requires `GITHUB_ACCESS_TOKEN` environment variable:

```bash
python src/awesome.py awesome-page          # Generate the awesome page markdown
python src/awesome.py awesome-groups        # List all topic groups
python src/awesome.py awesome-page-excluded # Show repos not in awesome page
python src/awesome.py version               # Print version
```

## Code Architecture

The entire application lives in `src/awesome.py`:

- **Topic System**: `awesome_topics` dict defines 18 categories (top-pick, documentation, demonstration, dockerfile, kubernetes, helm-chart, aws-environment, azure-environment, sdk, mapper, etc.) with title, description, and member lists
- **Configuration**: `configuration_locator` maps CLI args → environment variables → defaults. Key config: `github_access_token`, `organization`, `subcommand`
- **Command Dispatch**: Uses argparse with subcommand pattern; dispatches via `do_{subcommand_name}(args)` functions
- **GitHub Integration**: Uses PyGithub to query all repos, filter by topics, and extract metadata
- **Blacklist Topics**: Repos with `deprecated`, `obsolete`, `archived`, or `not-in-awesome` topics are excluded

## Code Style

- Line length: 120 characters (Black and Flake8)
- Import sorting: isort with Black profile
- Python version: ≥3.10
- Type checking: mypy with several disabled error codes (see pyproject.toml)

## Senzing Claude Commands

Use `/senzing` to access Senzing-specific workflows:

- `changelog-update` - Update CHANGELOG.md
- `code-review` - Perform code review
- `github-issue-fix-proposal` - Propose code changes based on GitHub issues

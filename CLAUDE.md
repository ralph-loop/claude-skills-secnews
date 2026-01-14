# CLAUDE.md - AI Assistant Guide

## Repository Overview

This repository provides a custom command for **Gemini CLI** called `/secnews` that fetches and summarizes the latest cybersecurity threat news from curated RSS feeds. The project includes automated testing, CI/CD workflows, and self-healing mechanisms for broken feed URLs.

**Repository**: `gemini-cli-command-secnews`
**Primary Language**: Python (tests), TOML (configuration), Markdown (data)
**Target Platform**: Gemini CLI (Google AI command-line interface)

---

## Directory Structure

```
.
├── .gemini/                    # Gemini CLI configuration
│   ├── GEMINI.md              # Gemini AI assistant documentation (Korean)
│   └── commands/
│       └── secnews.toml       # Custom /secnews command definition
├── .github/
│   └── workflows/
│       └── secnews_tester.yml # CI/CD workflow for feed validation
├── tests/
│   └── test_secnews_feeds.py  # pytest tests for RSS feed URLs
├── .gitignore                 # Git ignore patterns
├── requirements.txt           # Python dependencies
└── secnews_feeds.md          # Central data: RSS feed URLs by category
```

---

## Core Components

### 1. secnews_feeds.md
**Location**: `/secnews_feeds.md`
**Purpose**: Central data file containing RSS feed URLs organized by security threat categories.

**Structure**:
```markdown
# SecNews Feeds

## Category Name
*   [Feed Title](Feed URL)
*   [Feed Title](Feed URL)
```

**Current Categories**:
- **Malware**: The Hacker News, BleepingComputer
- **Phishing**: Krebs on Security
- **Vulnerabilities**: Dark Reading

**Modification Guidelines**:
- Always use the exact markdown format: `*   [Title](URL)`
- Group feeds under `## Category Name` headers
- Ensure URLs are valid and accessible
- Run tests after modifications (`pytest`)

### 2. .gemini/commands/secnews.toml
**Location**: `/.gemini/commands/secnews.toml`
**Purpose**: Defines the `/secnews` custom command for Gemini CLI.

**Command Workflow**:
1. **User Input**: `gemini secnews malware phishing`
2. **Fetch Source**: Uses `web_fetch` to retrieve `secnews_feeds.md` from GitHub
3. **Find URLs**: Parses markdown to extract RSS feed URLs for requested categories
4. **Fetch Content**: Retrieves RSS feed content via `web_fetch`
5. **Summarize**: Generates markdown summary of recent updates (last 7 days)
6. **Output**: Clean, readable markdown with titles for each category

**Important Notes**:
- The command is designed for Gemini CLI, not Claude
- Uses Gemini's `web_fetch` tool (different from Claude's WebFetch)
- Must use **gemini-3-pro** or **gemini-3-flash** models (NEVER gemini-1.5-pro)

### 3. tests/test_secnews_feeds.py
**Location**: `/tests/test_secnews_feeds.py`
**Purpose**: Validates that all RSS feed URLs in `secnews_feeds.md` are accessible.

**Key Functions**:
- `extract_urls_from_markdown()`: Extracts URLs using regex
- `test_url_is_valid()`: Parametrized test for each URL

**Test Execution**:
```bash
# Install dependencies
python -m venv .venv
.venv/bin/pip install -r requirements.txt

# Run tests
.venv/bin/pytest -n auto
```

### 4. .github/workflows/secnews_tester.yml
**Location**: `/.github/workflows/secnews_tester.yml`
**Purpose**: Automated CI/CD pipeline for feed validation and remediation.

**Workflow Triggers**:
- Push to `main` branch
- Pull requests targeting `main`
- Manual dispatch (`workflow_dispatch`)
- Daily cron schedule (`0 0 * * *` - midnight UTC)

**Jobs**:
1. **test-feeds**: Runs pytest to validate all feed URLs
2. **create-remediation-issue**: If tests fail, creates GitHub issue with broken URLs and mentions `@gemini-cli` for remediation

**Key Features**:
- Parallel test execution (`pytest -n auto`)
- JUnit XML report generation
- Artifact upload for failed tests
- Automated issue creation with broken URL list

---

## Development Workflows

### Adding New Feed URLs

1. **Edit secnews_feeds.md**:
   ```markdown
   ## New Category
   *   [Feed Name](https://example.com/feed.xml)
   ```

2. **Test Locally**:
   ```bash
   .venv/bin/pytest -n auto
   ```

3. **Commit and Push**:
   ```bash
   git add secnews_feeds.md
   git commit -m "Add new feed for [category]"
   git push
   ```

4. **CI Validation**: GitHub Actions will automatically test the new URLs.

### Modifying the /secnews Command

1. **Edit .gemini/commands/secnews.toml**:
   - Modify the `prompt` section to change behavior
   - Update `description` for command help text

2. **Test in Gemini CLI**:
   ```bash
   gemini secnews [categories]
   ```

3. **Commit Changes**:
   - Follow standard git workflow
   - Ensure changes are compatible with Gemini CLI tool ecosystem

### Updating Tests

1. **Modify tests/test_secnews_feeds.py**:
   - Update `extract_urls_from_markdown()` if markdown format changes
   - Adjust timeout/headers in `test_url_is_valid()` if needed

2. **Update requirements.txt**:
   - Add new dependencies if required
   - Pin versions for reproducibility

3. **Test Workflow**:
   ```bash
   .venv/bin/pytest -v  # Verbose output
   ```

---

## Key Conventions and Best Practices

### Git Workflow

**Branch Naming**:
- Feature branches: `feat/description-<issue-id>`
- Claude branches: `claude/description-<session-id>`
- Always develop on feature branches, merge via PR

**Commit Messages**:
- Use conventional commits format
- Examples:
  - `feat: Add RSS feed for threat intelligence`
  - `fix: Update broken BleepingComputer feed URL`
  - `test: Add timeout handling for slow feeds`

**Push Guidelines**:
```bash
# Always use -u flag for new branches
git push -u origin <branch-name>

# For network failures, retry with exponential backoff
# (2s, 4s, 8s, 16s) - up to 4 retries
```

### Code Style

**Python**:
- Follow PEP 8 style guide
- Use descriptive variable names
- Add docstrings for functions
- Type hints encouraged but not required

**Markdown**:
- Use consistent formatting for feed lists
- Keep category headers at `## Level 2`
- Ensure proper spacing between sections

### Testing

**Test Philosophy**:
- All RSS feed URLs MUST be validated
- Tests should fail fast (15-second timeout)
- Use parallel execution for performance
- Mock external dependencies when appropriate

**CI/CD**:
- All PRs must pass CI checks
- Daily automated runs catch broken feeds
- Failed tests trigger automatic remediation issues

---

## Important Notes for AI Assistants

### For Claude (this assistant)

1. **Repository Context**:
   - This is a **Gemini CLI** project, not Claude Code
   - Don't confuse Gemini CLI commands with Claude Code features
   - The `/secnews` command runs in Gemini, not Claude

2. **File Modifications**:
   - When adding feeds to `secnews_feeds.md`, preserve exact markdown format
   - Always run tests after modifying feed URLs
   - Update tests if feed structure changes

3. **Testing**:
   - Use Python virtual environment (`.venv/`)
   - Run pytest with parallel execution (`-n auto`)
   - Check test reports for specific failures

4. **Git Operations**:
   - Develop on branch: `claude/add-claude-documentation-4dQZr`
   - Use `git push -u origin <branch>` for new branches
   - Follow retry logic for network failures (exponential backoff)

5. **CI/CD Awareness**:
   - GitHub Actions runs automatically on push/PR
   - Daily cron checks feed health
   - Failed feeds trigger issues for remediation

### For Gemini AI

1. **Model Selection**:
   - Use **gemini-3-pro** or **gemini-3-flash**
   - **NEVER** use gemini-1.5-pro (per GEMINI.md)

2. **Command Execution**:
   - Fetch `secnews_feeds.md` from GitHub raw URL
   - Parse markdown to extract category-specific feeds
   - Use `web_fetch` tool for RSS feed content
   - Summarize last 7 days of security news
   - Output clean markdown with category titles

3. **Error Handling**:
   - Handle missing categories gracefully
   - Report when feeds are unavailable
   - Provide clear user feedback

---

## Dependencies

### Python (requirements.txt)
```
pytest          # Testing framework
requests        # HTTP library for URL validation
pytest-xdist    # Parallel test execution
```

**Installation**:
```bash
python -m venv .venv
.venv/bin/pip install -r requirements.txt
```

### External Dependencies
- **GitHub Actions**: CI/CD platform
- **RSS Feeds**: External cybersecurity news sources
- **Gemini CLI**: Command-line interface for Google AI

---

## Troubleshooting

### Common Issues

**1. RSS Feed URL Failing Tests**
- **Symptom**: `pytest` fails with `AssertionError` or `RequestException`
- **Solution**:
  - Check if URL is still valid
  - Update URL in `secnews_feeds.md`
  - Verify feed hasn't blocked automated requests
  - Adjust User-Agent header in tests if needed

**2. CI Workflow Not Running**
- **Symptom**: No GitHub Actions runs on push
- **Solution**:
  - Check workflow file syntax (`.github/workflows/secnews_tester.yml`)
  - Verify branch protection rules
  - Ensure Actions are enabled in repository settings

**3. /secnews Command Not Working in Gemini CLI**
- **Symptom**: Command not recognized
- **Solution**:
  - Verify Gemini CLI is properly installed
  - Check `.gemini/commands/secnews.toml` syntax
  - Reload Gemini CLI configuration
  - Ensure correct Gemini model is selected

**4. Test Environment Issues**
- **Symptom**: `ModuleNotFoundError` or import errors
- **Solution**:
  - Recreate virtual environment
  - Reinstall dependencies: `pip install -r requirements.txt`
  - Check Python version (3.11 recommended)

---

## Related Documentation

- **GEMINI.md**: Gemini AI assistant instructions (Korean language)
- **GitHub Actions Docs**: https://docs.github.com/en/actions
- **pytest Documentation**: https://docs.pytest.org/
- **Gemini CLI**: Google's AI command-line interface

---

## Maintenance

### Regular Tasks

**Weekly**:
- Review failed CI runs
- Check GitHub issues for broken feeds
- Update feed URLs as needed

**Monthly**:
- Review and update RSS feed sources
- Add new security news feeds
- Archive outdated/inactive feeds

**As Needed**:
- Update Python dependencies
- Improve test coverage
- Enhance command prompt for better summaries

### Version History

- **Latest**: Initial setup with secnews command, automated testing, and CI/CD
- **Previous Commits**:
  - `6e30467`: Added GEMINI.md
  - `4571d44`: feat: Add secnews custom command and testing workflow
  - `99be7bc`: Merge pull request #1

---

## Contact and Support

For issues related to:
- **Feed URLs**: Create GitHub issue or PR with updates
- **Gemini CLI**: Refer to Gemini CLI documentation
- **CI/CD**: Check GitHub Actions logs and workflow configuration
- **General Questions**: Open GitHub discussion or issue

---

**Last Updated**: 2026-01-14
**Maintained by**: threathunterr
**License**: (Check repository for license file)

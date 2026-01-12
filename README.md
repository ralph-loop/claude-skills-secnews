# SecNews Command for Gemini CLI

This repository hosts the configuration and data source for the `secnews` custom command for the Gemini CLI. This command acts as a "Cyber Threat News Reporter," fetching and summarizing the latest cybersecurity news from various RSS feeds.

## Features

*   **Categorized News**: Fetch news by category (e.g., Malware, Phishing, Vulnerabilities).
*   **Centralized Feed Management**: All RSS feeds are managed in a single Markdown file (`secnews_feeds.md`).
*   **Automated Validation**: A GitHub Workflow automatically checks the validity of the RSS feed URLs daily.

## Installation & Setup

1.  **Prerequisites**: Ensure you have the [Gemini CLI](https://github.com/google/gemini-cli) installed and configured.

2.  **Clone this Repository**:
    ```bash
    git clone https://github.com/your-username/secnews-command.git
    cd secnews-command
    ```

3.  **Configure the Command**:
    *   Open `.gemini/commands/secnews.toml`.
    *   **Important**: Locate the line containing the URL `https://raw.githubusercontent.com/USER/REPO/main/secnews_feeds.md`.
    *   Replace `USER/REPO` with your actual GitHub username and repository name (e.g., `jdoe/secnews-command`). This ensures the CLI fetches the feed list from your repository.

4.  **Install the Command**:
    *   Copy the `secnews.toml` file to your Gemini CLI's commands directory (usually `~/.gemini/commands/` or the local `.gemini/commands/` if running from the repo root).
    *   *Alternatively*, if you are running Gemini CLI from this directory, it should pick up the local configuration.

## Usage

Run the command followed by a category keyword:

```bash
gemini secnews malware
```

```bash
gemini secnews phishing
```

```bash
gemini secnews vulnerabilities
```

The AI will fetch the relevant feeds defined in `secnews_feeds.md`, summarize the articles from the last 7 days, and present them in a clean Markdown format.

## Configuration

To add or remove news sources, simply edit the `secnews_feeds.md` file:

1.  Open `secnews_feeds.md`.
2.  Add a new feed under the appropriate H2 header (e.g., `## Malware`).
3.  Format: `* [Source Name](Feed URL)`
4.  Commit and push your changes.

## Testing

This project includes automated tests to ensure the RSS feed URLs are valid and reachable.

### Running Tests Locally

1.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

2.  Run the tests:
    ```bash
    pytest
    ```

### GitHub Workflow

The `.github/workflows/secnews_tester.yml` workflow runs automatically on push, pull request, and daily on a schedule. It checks all URLs in `secnews_feeds.md`. If a link is broken, it will create a GitHub Issue to notify you.

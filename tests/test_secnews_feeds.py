import os
import re

import pytest
import requests

# Get the absolute path to the project root directory
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
MARKDOWN_FILE = os.path.join(ROOT_DIR, "secnews_feeds.md")

# Known-flaky feeds: map URL -> reason for expected failure
KNOWN_FAILING_FEEDS = {}


def extract_urls_from_markdown(file_path):
    """Extracts all URLs from a markdown file."""
    if not os.path.exists(file_path):
        pytest.fail(f"Markdown file not found: {file_path}")

    with open(file_path, "r") as f:
        content = f.read()
    # Regex to find URLs in plain text (simple version)
    # Matches http/https URLs, filters out potential trailing parens if inside markdown link syntax
    urls = re.findall(r"https?://[^\s\)]+", content)
    return sorted(list(set(urls)))


# ---------------------------------------------------------------------------
# Feed URL validation tests
# ---------------------------------------------------------------------------

def _get_xfail_mark(url):
    """Return an xfail marker if the URL is a known-failing feed."""
    reason = KNOWN_FAILING_FEEDS.get(url)
    if reason:
        return pytest.param(url, marks=pytest.mark.xfail(reason=reason, strict=False))
    return url


_ALL_URLS = extract_urls_from_markdown(MARKDOWN_FILE)
_PARAMETRIZED_URLS = [_get_xfail_mark(u) for u in _ALL_URLS]


@pytest.mark.parametrize("url", _PARAMETRIZED_URLS)
def test_url_is_valid(url):
    """Tests if a given URL is reachable."""
    try:
        headers = {"User-Agent": "SecNews-Tester/1.0"}
        response = requests.get(url, timeout=15, stream=True, headers=headers)
        assert response.ok, f"URL {url} returned status code {response.status_code}"
    except requests.exceptions.RequestException as e:
        pytest.fail(f"URL {url} failed to load: {e}")


# ---------------------------------------------------------------------------
# Unit tests for URL extraction logic
# ---------------------------------------------------------------------------


class TestExtractUrlsFromMarkdown:
    """Unit tests for the extract_urls_from_markdown helper."""

    def test_extracts_http_and_https_urls(self, tmp_path):
        md = tmp_path / "feeds.md"
        md.write_text(
            "* [Site A](https://example.com/feed)\n"
            "* [Site B](http://legacy.example.org/rss)\n"
        )
        urls = extract_urls_from_markdown(str(md))
        assert urls == ["http://legacy.example.org/rss", "https://example.com/feed"]

    def test_deduplicates_urls(self, tmp_path):
        md = tmp_path / "feeds.md"
        md.write_text(
            "* [A](https://example.com/feed)\n"
            "* [B](https://example.com/feed)\n"
        )
        urls = extract_urls_from_markdown(str(md))
        assert urls == ["https://example.com/feed"]

    def test_returns_sorted_urls(self, tmp_path):
        md = tmp_path / "feeds.md"
        md.write_text(
            "* [Z](https://zzz.com/feed)\n"
            "* [A](https://aaa.com/feed)\n"
        )
        urls = extract_urls_from_markdown(str(md))
        assert urls == ["https://aaa.com/feed", "https://zzz.com/feed"]

    def test_empty_file_returns_empty_list(self, tmp_path):
        md = tmp_path / "feeds.md"
        md.write_text("")
        urls = extract_urls_from_markdown(str(md))
        assert urls == []

    def test_no_urls_returns_empty_list(self, tmp_path):
        md = tmp_path / "feeds.md"
        md.write_text("# Title\nSome text without links.\n")
        urls = extract_urls_from_markdown(str(md))
        assert urls == []

    def test_missing_file_fails(self, tmp_path):
        with pytest.raises(pytest.fail.Exception, match="Markdown file not found"):
            extract_urls_from_markdown(str(tmp_path / "nonexistent.md"))

    def test_strips_trailing_parenthesis(self, tmp_path):
        md = tmp_path / "feeds.md"
        md.write_text("Check [link](https://example.com/path) for details.\n")
        urls = extract_urls_from_markdown(str(md))
        assert urls == ["https://example.com/path"]

    def test_plain_urls_without_markdown_syntax(self, tmp_path):
        md = tmp_path / "feeds.md"
        md.write_text("Visit https://example.com/feed for more info.\n")
        urls = extract_urls_from_markdown(str(md))
        assert urls == ["https://example.com/feed"]

    def test_real_secnews_feeds_file(self):
        """Smoke test: the real secnews_feeds.md should contain many URLs."""
        urls = extract_urls_from_markdown(MARKDOWN_FILE)
        assert len(urls) >= 50, (
            f"Expected at least 50 feed URLs, found {len(urls)}"
        )
        assert all(
            u.startswith("http://") or u.startswith("https://") for u in urls
        )

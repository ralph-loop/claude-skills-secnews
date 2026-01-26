# SecNews - Stay Ahead of Cybersecurity Threats

Instant access to curated cybersecurity news and threat intelligence from 55+ trusted sources. A powerful Claude Code custom command for security professionals, incident responders, and threat hunters.

## Quick Start

### Installation

```bash
mkdir -p ~/.claude/commands && curl -sSL https://raw.githubusercontent.com/threathunterr/claude-commands-secnews/master/.claude/commands/secnews.md -o ~/.claude/commands/secnews.md
```

### Your First Query

```bash
/secnews malware
```

That's it. Get the latest malware threats in seconds.

## Usage

Fetch news by category or get everything:

```bash
# Get all security news across all categories
/secnews all

# Specific threat categories
/secnews malware              # Malware analysis and threats
/secnews ransomware           # Ransomware campaigns and attacks
/secnews vulnerabilities      # CVEs and zero-day exploits
/secnews phishing             # Phishing and social engineering
/secnews apt                  # Advanced Persistent Threats
/secnews threat-intel         # Threat intelligence reports
/secnews government           # Official advisories and alerts
```

Each command fetches the latest articles from the last 7 days, automatically prioritizing critical and zero-day information.

## Threat Categories

| Category | What You'll Get | Sample Sources |
|----------|-----------------|---|
| **malware** | Latest malware variants, analysis, IoCs | The Hacker News, BleepingComputer, Malwarebytes Labs, SecureList, SentinelOne |
| **ransomware** | Ransomware groups, campaigns, victims | The Record, Security Affairs, HackRead, HACKMAGEDDON, UpGuard |
| **vulnerabilities** | CVEs, exploits, patch releases | Dark Reading, Google Project Zero, Microsoft MSRC, Qualys, Rapid7 |
| **phishing** | Phishing campaigns, tactics, defense | Krebs on Security, Cofense, Proofpoint |
| **apt** | Nation-state actors, APT operations | Palo Alto Networks, Google TAG, Cisco Talos, Checkpoint Research |
| **threat-intel** | General threat intelligence | Threatpost, IBM Security, EclecticIQ, Anomali, Bitdefender Labs |
| **government** | Official advisories and alerts | NIST, CIS, SANS ISC |

## Feed Sources

SecNews aggregates from **55+ premium security sources** including:

**Government & Compliance**
- NIST Cybersecurity Insights
- CIS Advisories
- SANS Internet Storm Center

**Major Threat Intelligence**
- Palo Alto Networks (Unit 42)
- Cisco Talos
- Google Threat Analysis Group
- Checkpoint Research
- Trend Micro

**Security Research**
- Krebs on Security
- Dark Reading
- Schneier on Security
- Graham Cluley
- Troy Hunt

**Vendor Security Blogs**
- Microsoft Security
- Google Online Security
- Sophos News
- Cloudflare Security
- McAfee Labs
- Cisco Security

**Community & Independent**
- Reddit r/netsec & r/cybersecurity
- SpecterOps
- SensePost
- Quarkslab

All feeds are curated and tested daily. See the complete feed list in [`secnews_feeds.md`](./secnews_feeds.md).

## Features

- **55+ Trusted Sources** - Carefully curated feeds from government agencies, security vendors, and independent researchers
- **9 Categories** - Malware, Ransomware, Vulnerabilities, Phishing, APT, Threat-Intel, Government, General, Community
- **Real-Time Updates** - Articles from the last 7 days with critical items highlighted
- **Daily Validation** - Automated testing via GitHub Actions ensures all feeds stay operational
- **Auto-Remediation** - Broken feeds automatically flagged for quick restoration

## Development & Contributing

### Manual Installation

If you prefer to set up manually:

1. Clone the repository:
   ```bash
   git clone https://github.com/threathunterr/claude-commands-secnews.git
   cd claude-commands-secnews
   ```

2. Copy the command file:
   ```bash
   cp .claude/commands/secnews.md ~/.claude/commands/
   ```

### Running Tests Locally

```bash
# Install dependencies
pip install -r requirements.txt

# Run feed validation
pytest tests/test_secnews_feeds.py -v
```

### Adding New Feeds

1. Edit [`secnews_feeds.md`](./secnews_feeds.md)
2. Add your feed under the appropriate category:
   ```markdown
   * [Source Name](https://feed-url.com/rss)
   ```
3. Ensure the URL is a valid RSS/Atom feed
4. Submit a pull request

Requirements for new feeds:
- From reputable, established security sources
- Valid RSS or Atom feed format
- Relevant to the category
- Ideally, no more than 100% spam rate

### CI/CD Pipeline

GitHub Actions validates feeds daily:
- Checks all 55+ feeds for accessibility
- Auto-creates issues for broken feeds
- Runs on every push and pull request
- Maintains feed health and uptime

## Troubleshooting

**Command not found?**
- Restart your Claude Code application after installation
- Verify the file exists: `ls ~/.claude/commands/secnews.md`

**No results or connection timeout?**
- Some feeds may be temporarily unavailable
- The command retries automatically
- Try again in a few moments

**Want to report a broken feed?**
- Open an issue on GitHub
- Include the feed name and URL
- Provide the error message if applicable

## License

MIT - See LICENSE file for details

## Contributing

We welcome contributions! Help us keep security news flowing:

1. **Report Broken Feeds** - Open an issue if a feed stops working
2. **Suggest Sources** - Know a great security blog? Submit it!
3. **Improve Docs** - Better explanations always welcome
4. **Add Feeds** - Submit a PR with new, vetted security sources

**Quality standards for contributions:**
- Use reputable, established sources only
- Ensure feeds are RSS/Atom compliant
- Verify feeds are active and well-maintained
- Add feeds to the appropriate category
- Run tests locally before submitting

## Related Resources

- [Claude Code Official Docs](https://github.com/anthropics/claude-code)
- [MITRE ATT&CK Framework](https://attack.mitre.org/)
- [CISA Alert System](https://www.cisa.gov/news-events/alerts)

---

**Repository:** [threathunterr/claude-commands-secnews](https://github.com/threathunterr/claude-commands-secnews)
**Maintained by:** Security researchers and threat hunters
**Last Feed Update:** 2026-01-27

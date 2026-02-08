# SecNews - Stay Ahead of Cybersecurity Threats

Instant access to curated cybersecurity news and threat intelligence from 55 trusted sources. A powerful Claude Code skill for security professionals, incident responders, and threat hunters.

## Quick Start

### Installation

```bash
mkdir -p ~/.claude/skills/secnews && curl -sSL https://raw.githubusercontent.com/ralph-loop/claude-skills-secnews/master/.claude/skills/secnews/SKILL.md -o ~/.claude/skills/secnews/SKILL.md
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
/secnews general              # Major security publications and vendor blogs
/secnews community            # Community-driven security content
/secnews red-team             # Offensive security and red team research
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
| **general** | Major security publications and vendor blogs | Schneier on Security, WIRED, Dark Reading, Sophos, Cloudflare |
| **community** | Community-driven security content | Reddit r/netsec, r/cybersecurity, SpecterOps |
| **red-team** | Offensive security and red team research | SensePost, Quarkslab, Fox-IT, Signals Corps |

## Feed Sources

SecNews aggregates from **55 premium security sources** including:

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

All feeds are curated. See the complete feed list in [`secnews_feeds.md`](./secnews_feeds.md).

## Features

- **55 Trusted Sources** - Carefully curated feeds from government agencies, security vendors, and independent researchers
- **10 Categories** - Malware, Ransomware, Vulnerabilities, Phishing, APT, Threat-Intel, Government, General, Community, Red Team
- **Real-Time Updates** - Articles from the last 7 days with critical items highlighted

## Development & Contributing

### Manual Installation

If you prefer to set up manually:

1. Clone the repository:
   ```bash
   git clone https://github.com/ralph-loop/claude-skills-secnews.git
   cd claude-skills-secnews
   ```

2. Copy the skill file:
   ```bash
   mkdir -p ~/.claude/skills/secnews && cp .claude/skills/secnews/SKILL.md ~/.claude/skills/secnews/
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

## Troubleshooting

**Skill not found?**
- Restart your Claude Code application after installation
- Verify the file exists: `ls ~/.claude/skills/secnews/SKILL.md`

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

## Related Resources

- [Claude Code Official Docs](https://github.com/anthropics/claude-code)
- [MITRE ATT&CK Framework](https://attack.mitre.org/)
- [CISA Alert System](https://www.cisa.gov/news-events/alerts)


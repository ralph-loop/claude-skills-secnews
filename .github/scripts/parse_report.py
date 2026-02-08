#!/usr/bin/env python3
"""Parse JUnit XML test report and output failed feed URLs for GitHub Actions."""

import xml.etree.ElementTree as ET
import re
from urllib.parse import unquote
import os


def parse_junit_report(report_path):
    """Parses a JUnit XML report and returns a list of failed URLs."""
    if not os.path.exists(report_path):
        return []
    try:
        tree = ET.parse(report_path)
        root = tree.getroot()
        failed_urls = []
        for testcase in root.iter('testcase'):
            if testcase.find('failure') is not None:
                match = re.search(r'\[(.*?)\]', testcase.attrib.get('name', ''))
                if match:
                    failed_urls.append(unquote(match.group(1)))
        return sorted(list(set(failed_urls)))
    except ET.ParseError:
        return []


def main():
    failed_urls = parse_junit_report('report.xml')

    # Output has_failures flag
    with open(os.environ['GITHUB_OUTPUT'], 'a') as f:
        has_failures = 'true' if failed_urls else 'false'
        print(f'has_failures={has_failures}', file=f)

    # Only output issue_body if there are actual failures
    if failed_urls:
        issue_body = "The following SecNews feed URLs failed the check:\n\n"
        for url in failed_urls:
            issue_body += f"- `{url}`\n"
        issue_body += "\n\nPlease investigate and fix these broken feed URLs."

        with open(os.environ['GITHUB_OUTPUT'], 'a') as f:
            print('issue_body<<EOF', file=f)
            print(issue_body, file=f)
            print('EOF', file=f)


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Monitor and automatically close browser tabs in Chrome/Chromium
using the DevTools Protocol, based on a dynamic list of title keywords.
"""

import argparse
import requests
import time
from typing import List, Dict


def get_tabs(port: int = 9222) -> List[Dict]:
    """
    Fetch the list of open tabs (targets) from the Chrome DevTools Protocol endpoint.

    Args:
        port (int): Remote debugging port (default: 9222).

    Returns:
        List[Dict]: Each dict represents a tab with keys like 'id', 'title', etc.
    """
    url = f'http://127.0.0.1:{port}/json'
    response = requests.get(url, timeout=2)
    response.raise_for_status()
    return response.json()


def close_tab(target_id: str, port: int = 9222) -> bool:
    """
    Close a Chrome/Chromium tab given its DevTools target ID.

    Args:
        target_id (str): DevTools target ID of the tab.
        port (int): Remote debugging port (default: 9222).

    Returns:
        bool: True if closed successfully, False otherwise.
    """
    url = f'http://127.0.0.1:{port}/json/close/{target_id}'
    try:
        resp = requests.get(url, timeout=2)
        resp.raise_for_status()
        return True
    except requests.RequestException:
        return False


def monitor_tabs(keywords: List[str], poll_interval: int = 5, port: int = 9222):
    """
    Continuously monitor open tabs and close any whose title contains
    one of the specified keywords (case-insensitive).

    Args:
        keywords (List[str]): List of substrings to match in tab titles.
        poll_interval (int): Seconds between checks (default: 5).
        port (int): Remote debugging port (default: 9222).
    """
    lower_keywords = [kw.lower() for kw in keywords]
    print(f"Monitoring for keywords {keywords} every {poll_interval}s...")
    while True:
        try:
            tabs = get_tabs(port)
            for tab in tabs:
                title = tab.get('title', '')
                if any(kw in title.lower() for kw in lower_keywords):
                    tid = tab.get('id', '')
                    if tid and close_tab(tid, port):
                        print(f"Closed tab matching {keywords}: \"{title}\"")
        except Exception as e:
            print(f"Error during monitoring: {e}")
        time.sleep(poll_interval)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Close Chrome/Chromium tabs whose titles match any given keyword."
    )
    parser.add_argument(
        'keywords',
        nargs='+',
        help="One or more substrings to match against tab titles (e.g. youtube marca)"
    )
    parser.add_argument(
        '--interval', '-i',
        type=int,
        default=5,
        help="Polling interval in seconds (default: 5)"
    )
    parser.add_argument(
        '--port', '-p',
        type=int,
        default=9222,
        help="Chrome remote debugging port (default: 9222)"
    )

    args = parser.parse_args()
    monitor_tabs(args.keywords, args.interval, args.port)
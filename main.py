#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Monitor and automatically close YouTube tabs in Chrome/Chromium
using the DevTools Protocol.
"""

import requests
import time


def get_tabs(port: int = 9222) -> list[dict]:
    """
    Fetches the list of open tabs (targets) from the Chrome DevTools Protocol endpoint.

    Args:
        port (int): The remote debugging port Chrome was started with (default: 9222).

    Returns:
        list[dict]: A list of dictionaries representing each open tab.
    """
    url = f'http://127.0.0.1:{port}/json'
    response = requests.get(url, timeout=2)
    response.raise_for_status()
    return response.json()
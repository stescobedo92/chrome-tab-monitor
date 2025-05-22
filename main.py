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


def close_tab(target_id: str, port: int = 9222) -> bool:
    """
    Closes a Chrome/Chromium tab given its DevTools target ID.

    Args:
        target_id (str): The DevTools target ID of the tab to close.
        port (int): The remote debugging port Chrome was started with (default: 9222).

    Returns:
        bool: True if the tab was closed successfully, False otherwise.
    """
    url = f'http://127.0.0.1:{port}/json/close/{target_id}'
    try:
        response = requests.get(url, timeout=2)
        response.raise_for_status()
        return True
    except requests.RequestException:
        return False
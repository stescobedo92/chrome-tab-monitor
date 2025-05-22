# chrome-tab-monitor

A small Python utility that connects to Chrome/Chromium via the DevTools Protocol
and automatically closes any tab whose title contains "youtube".

## Prerequisites

- Python 3.7+
- `requests` library (`pip install requests`)
- Chrome/Chromium started with remote debugging enabled:
```bash
  google-chrome --remote-debugging-port=9222
```

## Installation

- Clone this repository:
```bash
  git clone git@github.com:stescobedo92/chrome-tab-monitor.git
  cd chrome-tab-monitor
```
- Install dependencies:
```bash
  pip install -r requirements.txt
```

## Usage
```bash
  python monitor_tabs.py
```

You will see output like:

```bash
  Monitoring YouTube tabs every 5 seconds...
  Closed YouTube tab: YouTube – Home
```
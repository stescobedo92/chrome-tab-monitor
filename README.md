# chrome-tab-monitor

A Python utility that connects to Chrome/Chromium via the DevTools Protocol and automatically closes any tab whose title matches one or more user-provided keywords.

## Prerequisites

- Python 3.7+
- `requests` library (`pip install requests`)
- Chrome/Chromium started with remote debugging enabled:
```bash
mkdir /tmp/chrome-debug-profile && cd /tmp/chrome-debug-profile
google-chrome --remote-debugging-port=9222 --user-data-dir=/tmp/chrome-debug-profile --disable-features=CloudPolicyInvalidation,OptimizationGuideModelFetcher --enable-logging --v=1
```

## Installation

- Clone this repository:
```bash
git clone git@github.com:stescobedo92/chrome-tab-monitor.git
cd chrome-tab-monitor
```
- (Optional) Create a virtualenv and install dependencies:
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage
```bash
# Close any tab with "youtube" or "programming" or "github.com" in its title:
python monitor_tabs.py youtube programming github.com
```
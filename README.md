# DDoS Protection

A simple Python-based Rate limiter tool that monitors incoming traffic, detects suspicious activity, and applies rate limiting.

## Features

- Monitors incoming HTTP requests
- Detects suspicious activity based on request rate
- Temporarily rate limits IPs exceeding the threshold

## Requirements

- Python 3.x

## Installation

1. Clone the repository:

```sh
git clone https://github.com/YihyunCS/RyoRateLimit.git

pip install -r requirements.txt

python src/monitor.py

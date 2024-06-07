# src/mitigate.py

import time
import logging
from src.detect import detector

rate_limited_ips = {}

def rate_limit_ip(ip, duration=300):
    expire_time = time.time() + duration
    rate_limited_ips[ip] = expire_time
    logging.info(f"Rate-limited IP: {ip} for {duration} seconds")

def should_rate_limit(ip):
    if ip in rate_limited_ips:
        if time.time() > rate_limited_ips[ip]:
            del rate_limited_ips[ip]
            return False
        return True
    if detector.is_suspicious(ip):
        rate_limit_ip(ip)
        return True
    return False

# src/detect.py

import time

class DDoSDetector:
    def __init__(self, threshold=100, time_window=60):
        self.threshold = threshold
        self.time_window = time_window
        self.requests = {}

    def log_request(self, ip):
        now = time.time()
        if ip not in self.requests:
            self.requests[ip] = []
        self.requests[ip].append(now)
        self.cleanup_requests(ip)

    def is_suspicious(self, ip):
        self.cleanup_requests(ip)
        return len(self.requests[ip]) > self.threshold

    def cleanup_requests(self, ip):
        now = time.time()
        self.requests[ip] = [t for t in self.requests[ip] if now - t < self.time_window]

detector = DDoSDetector()

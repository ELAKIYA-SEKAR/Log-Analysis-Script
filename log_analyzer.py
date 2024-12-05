from collections import Counter
from typing import List, Dict, Tuple
from log_parser import LogEntry

class LogAnalyzer:
    def __init__(self, entries: List[LogEntry], failed_login_threshold: int = 10):
        self.entries = entries
        self.failed_login_threshold = failed_login_threshold

    def count_requests_per_ip(self) -> List[Tuple[str, int]]:
        ip_counter = Counter(entry.ip_address for entry in self.entries)
        return sorted(ip_counter.items(), key=lambda x: x[1], reverse=True)

    def find_most_accessed_endpoint(self) -> Tuple[str, int]:
        endpoint_counter = Counter(entry.endpoint for entry in self.entries)
        return endpoint_counter.most_common(1)[0]

    def detect_suspicious_activity(self) -> List[Tuple[str, int]]:
        failed_logins = Counter(
            entry.ip_address
            for entry in self.entries
            if entry.endpoint == "/login" and entry.status_code == 401
        )
        suspicious = {
            ip: count
            for ip, count in failed_logins.items()
            if count >= self.failed_login_threshold
        }
        return sorted(suspicious.items(), key=lambda x: x[1], reverse=True)
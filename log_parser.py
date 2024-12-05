import re
from collections import Counter
from dataclasses import dataclass
from typing import List, Dict, Tuple

@dataclass
class LogEntry:
    ip_address: str
    timestamp: str
    method: str
    endpoint: str
    status_code: int
    response_size: int
    error_message: str = ""

class LogParser:
    def __init__(self, log_file_path: str):
        self.log_file_path = log_file_path
        self.log_pattern = re.compile(
            r'(\d+\.\d+\.\d+\.\d+).*?\[(.*?)\]\s"(\w+)\s([^"]+).*?"\s(\d+)\s(\d+)(?:\s"([^"]*)")?'
        )

    def parse_log_file(self) -> List[LogEntry]:
        entries = []
        with open(self.log_file_path, 'r') as file:
            for line in file:
                match = self.log_pattern.search(line)
                if match:
                    entries.append(LogEntry(
                        ip_address=match.group(1),
                        timestamp=match.group(2),
                        method=match.group(3),
                        endpoint=match.group(4).split()[0],
                        status_code=int(match.group(5)),
                        response_size=int(match.group(6)),
                        error_message=match.group(7) if match.group(7) else ""
                    ))
        return entries
import csv
from typing import List, Tuple
from tabulate import tabulate

class ReportGenerator:
    def __init__(self, output_file: str = "log_analysis_results.csv"):
        self.output_file = output_file

    def display_results(
        self,
        ip_requests: List[Tuple[str, int]],
        most_accessed: Tuple[str, int],
        suspicious: List[Tuple[str, int]]
    ):
        # Display IP requests
        print("\nRequests per IP Address:")
        print(tabulate(
            ip_requests,
            headers=["IP Address", "Request Count"],
            tablefmt="grid"
        ))

        # Display most accessed endpoint
        print("\nMost Frequently Accessed Endpoint:")
        print(f"{most_accessed[0]} (Accessed {most_accessed[1]} times)")

        # Display suspicious activity
        if suspicious:
            print("\nSuspicious Activity Detected:")
            print(tabulate(
                suspicious,
                headers=["IP Address", "Failed Login Attempts"],
                tablefmt="grid"
            ))
        else:
            print("\nNo suspicious activity detected.")

    def save_to_csv(
        self,
        ip_requests: List[Tuple[str, int]],
        most_accessed: Tuple[str, int],
        suspicious: List[Tuple[str, int]]
    ):
        with open(self.output_file, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            
            # Write headers
            writer.writerow(["Section", "Data"])
            
            # Write IP requests
            writer.writerow(["Requests per IP", ""])
            writer.writerow(["IP Address", "Request Count"])
            writer.writerows(ip_requests)
            
            # Write most accessed endpoint
            writer.writerow([])
            writer.writerow(["Most Accessed Endpoint", ""])
            writer.writerow(["Endpoint", "Access Count"])
            writer.writerow(most_accessed)
            
            # Write suspicious activity
            writer.writerow([])
            writer.writerow(["Suspicious Activity", ""])
            writer.writerow(["IP Address", "Failed Login Count"])
            writer.writerows(suspicious)
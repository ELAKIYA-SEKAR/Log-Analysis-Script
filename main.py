from log_parser import LogParser
from log_analyzer import LogAnalyzer
from report_generator import ReportGenerator

def main():
    # Initialize components
    parser = LogParser("sample.log")
    entries = parser.parse_log_file()
    
    analyzer = LogAnalyzer(entries)
    ip_requests = analyzer.count_requests_per_ip()
    most_accessed = analyzer.find_most_accessed_endpoint()
    suspicious = analyzer.detect_suspicious_activity()
    
    # Generate reports
    reporter = ReportGenerator()
    reporter.display_results(ip_requests, most_accessed, suspicious)
    reporter.save_to_csv(ip_requests, most_accessed, suspicious)
    
    print(f"\nResults have been saved to {reporter.output_file}")

if __name__ == "__main__":
    main()
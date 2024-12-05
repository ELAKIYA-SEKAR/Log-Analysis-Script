# Log Analysis Script

## Objective
This Python script analyzes web server log files to extract and analyze key information, focusing on:
- Request frequency per IP address
- Most frequently accessed endpoints
- Detection of suspicious activity (potential brute force attempts)

## Features
1. **IP Request Analysis**
   - Counts requests from each IP address
   - Sorts results by request frequency
   - Displays top requesting IP addresses

2. **Endpoint Analysis**
   - Identifies most accessed endpoints
   - Provides access frequency statistics

3. **Security Analysis**
   - Detects potential brute force attempts
   - Flags IPs exceeding failed login thresholds
   - Monitors failed authentication attempts

## Project Structure
- `main.py`: Entry point of the application
- `log_parser.py`: Handles log file parsing
- `log_analyzer.py`: Implements analysis logic
- `report_generator.py`: Manages output formatting and file generation

## Requirements
- Python 3.6+
- tabulate library for formatted console output

## Usage
1. Place your log file as `sample.log` in the project directory
2. Run the script:
   ```bash
   python main.py
   ```

## Output
The script generates two types of output:
1. **Console Output**: Formatted tables showing analysis results
2. **CSV File**: Detailed results saved in `log_analysis_results.csv`

## Results Format
### Console Output
```
Requests per IP Address:
+---------------+---------------+
| IP Address    | Request Count |
+===============+===============+
| 192.168.1.1   | 234          |
| 203.0.113.5   | 187          |
+---------------+---------------+

Most Frequently Accessed Endpoint:
/home (Accessed 403 times)

Suspicious Activity Detected:
+---------------+---------------------+
| IP Address    | Failed Login Count  |
+===============+=====================+
| 192.168.1.100 | 56                 |
+---------------+---------------------+
```

### CSV Output
The CSV file contains three sections:
1. Requests per IP
2. Most Accessed Endpoint
3. Suspicious Activity

## Implementation Details
- Uses regular expressions for efficient log parsing
- Implements object-oriented design principles
- Modular architecture for easy maintenance and extension
- Efficient data structures for analysis (Counter)

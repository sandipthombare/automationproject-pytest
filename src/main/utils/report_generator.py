import pytest

def generate_html_report(test_file, report_path = "src/reports/pytest_report.html"):
    
    pytest.main([test_file, f"--html={report_path}"])
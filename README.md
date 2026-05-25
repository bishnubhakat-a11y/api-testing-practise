# API Automation Testing Framework

This framework is built using Python, `pytest`, `requests`, and `allure` for reporting.

## Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run tests: `python run_tests.py` or `pytest tests/`

## Reports

To view allure reports:
1. Run tests to generate results: `pytest tests/`
2. Serve the report: `allure serve reports/allure-results`

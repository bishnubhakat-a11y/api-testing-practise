# API Automation Testing Framework

This framework is built using Python, `pytest`, `requests`, `locust`, and `pytest-html` for robust API testing and reporting.

## Features
- **Exhaustive Functional Testing:** Positive, Negative, Edge, and Boundary testing.
- **Performance & Load Testing:** Integrated `locust` for simulating thousands of concurrent users.
- **Data-Driven:** Centralized JSON payload factories for POST, PUT, and DELETE operations.
- **Schema Validations:** Validates API responses against expected JSON schemas.
- **Rich Reporting:** Integrates with `pytest-html` to generate single-page HTML reports.

## Folder Structure

```text
api-testing-framework/
├── config/              # Configuration files (settings.yaml, config.py)
├── data/
│   ├── payloads/        # Centralized payload factories (POST/PUT/DELETE)
│   └── schemas/         # JSON schemas for response validation
├── logs/                # Application and execution logs
├── performance/         # Locust performance and load testing scripts
├── reports/             # Generated HTML test reports
├── src/                 # Core framework logic
│   ├── api/             # API Client wrapper and endpoint routes
│   ├── services/        # Service layer for different API resources
│   └── utils/           # Helper functions, assertions, and loggers
├── tests/               # Pytest test cases
│   └── schema_validations/ # Schema validation tests
├── .env                 # Environment variables
├── .gitignore           # Ignored files (logs, reports, env, caches)
├── pytest.ini           # Pytest configurations
├── requirements.txt     # Python dependencies
└── run_tests.py         # Test execution runner
```

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Setup Environment Variables: Ensure you have your `.env` file configured.

## Execution Commands

### 1. Run Functional Tests
You can run the full suite, or use markers to run specific types of tests:

**Run entire test suite:**
```bash
pytest tests/
```

**Run critical Smoke Tests (Fast Sanity Check):**
```bash
pytest -m smoke
```

**Run full Regression Suite:**
```bash
pytest -m regression
```

### 2. Run Performance/Load Tests
Start the Locust load test and open `http://localhost:8089` in your browser:
```bash
python performance/load_test.py
# OR
locust -f performance/locustfile.py --host=https://jsonplaceholder.typicode.com
```

### 3. Generate HTML Reports
Use `pytest-html` to run your tests and output a single, readable HTML report. The `--self-contained-html` flag ensures all CSS/assets are bundled into one file:
```bash
pytest tests/ --html=reports/report.html --self-contained-html
```
You can then open `reports/report.html` directly in any web browser!

### 4.Generate reports using allure
Using 'allure + pytest' to generate reports
```bash
pytest tests/ --alluredir=reports/allure-results
allure serve reports/allure-results
```
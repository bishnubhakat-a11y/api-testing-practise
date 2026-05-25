# API Automation Testing Framework

This framework is built using Python, `pytest`, `requests`, `locust`, and `allure` for robust API testing and reporting.

## Features
- **Exhaustive Functional Testing:** Positive, Negative, Edge, and Boundary testing.
- **Performance & Load Testing:** Integrated `locust` for simulating thousands of concurrent users.
- **Data-Driven:** Centralized JSON payload factories for POST, PUT, and DELETE operations.
- **Schema Validations:** Validates API responses against expected JSON schemas.
- **Rich Reporting:** Integrates with Allure to generate beautiful HTML reports.

## Folder Structure

```text
api-testing-framework/
├── config/              # Configuration files (settings.yaml, config.py)
├── data/
│   ├── payloads/        # Centralized payload factories (POST/PUT/DELETE)
│   └── schemas/         # JSON schemas for response validation
├── logs/                # Application and execution logs
├── performance/         # Locust performance and load testing scripts
├── reports/             # Generated test reports (Allure results/HTML)
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
Run all exhaustive API tests using `pytest`:
```bash
python run_tests.py
# OR
pytest tests/
```

### 2. Run Performance/Load Tests
Start the Locust load test and open `http://localhost:8089` in your browser:
```bash
python performance/load_test.py
# OR
locust -f performance/locustfile.py --host=https://jsonplaceholder.typicode.com
```

### 3. Generate and Serve Allure Reports
First, run your tests to generate the raw result files in `reports/allure-results`.
```bash
pytest tests/
```
To view the report dynamically in your browser:
```bash
allure serve reports/allure-results
```

### 4. Generate Static HTML Reports
If you want to generate a static HTML folder (e.g. to host on GitHub Pages or a CI/CD server):
```bash
allure generate reports/allure-results -o reports/allure-report --clean
```
You can then open `reports/allure-report/index.html` in any browser.

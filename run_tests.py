import pytest
import sys
import os

if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    exit_code = pytest.main(["tests/", "--alluredir=reports/allure-results", "-v"])
    sys.exit(exit_code)

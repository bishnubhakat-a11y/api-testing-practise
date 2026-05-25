import os

def run_load_test():
    print("Running locust load test. Press Ctrl+C to stop.")
    os.system("locust -f performance/locustfile.py --host=https://jsonplaceholder.typicode.com")

if __name__ == "__main__":
    run_load_test()

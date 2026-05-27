"""
Core API Client Module
This module handles all the underlying HTTP communication using the `requests` library.
It is designed to be reusable so that we don't have to write `requests.get()` everywhere.
"""
import requests
import allure
import json
from config.config import config
from src.utils.logger import logger

class APIClient:
    """
    A wrapper around `requests.Session` to manage HTTP connections globally.
    Using a Session object is faster than standard requests because it reuses the underlying TCP connection.
    """
    def __init__(self):
        self.base_url = config.BASE_URL
        # Initialize a persistent HTTP session
        self.session = requests.Session()
        # Automatically attach Basic Authentication to every request made by this session
        self.session.auth = (config.USERNAME, config.PASSWORD)
        # Automatically attach JSON headers to every request
        self.session.headers.update({"Content-Type": "application/json"})

    def request(self, method, endpoint, **kwargs):
        """
        The master request method. All GET, POST, PUT, DELETE requests flow through here.
        This allows us to attach global logging to EVERY single API call.
        """
        url = f"{self.base_url}{endpoint}"
        logger.info(f"Making {method} request to {url}")
        
        # Execute the HTTP request using the persistent session
        response = self.session.request(method, url, **kwargs)
        
        logger.info(f"Received response {response.status_code} from {url}")

        # --- Allure Attachments ("API Screenshots") ---
        try:
            req_body = json.dumps(kwargs.get("json", {}), indent=4)
            allure.attach(
                body=f"URL: {url}\nMethod: {method}\nPayload:\n{req_body}",
                name=f"HTTP Request ({method})",
                attachment_type=allure.attachment_type.TEXT
            )
        except Exception:
            pass

        try:
            res_body = json.dumps(response.json(), indent=4)
            allure.attach(
                body=f"Status Code: {response.status_code}\nResponse Body:\n{res_body}",
                name="HTTP Response",
                attachment_type=allure.attachment_type.JSON
            )
        except Exception:
            # Fallback if response isn't JSON
            allure.attach(
                body=f"Status Code: {response.status_code}\nResponse Text:\n{response.text}",
                name="HTTP Response",
                attachment_type=allure.attachment_type.TEXT
            )

        return response

    # ---------------------------------------------------------
    # Convenience Wrappers for common HTTP verbs
    # ---------------------------------------------------------
    def get(self, endpoint, **kwargs):
        return self.request("GET", endpoint, **kwargs)

    def post(self, endpoint, **kwargs):
        return self.request("POST", endpoint, **kwargs)

    def put(self, endpoint, **kwargs):
        return self.request("PUT", endpoint, **kwargs)

    def delete(self, endpoint, **kwargs):
        return self.request("DELETE", endpoint, **kwargs)

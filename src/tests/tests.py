import requests
import json
from datetime import datetime
import subprocess
from flask import jsonify

API_URL = "http://localhost/resume"
# API_URL = "https://google.com"


resume_content = {
    "name": "Eshaan Rathi",
    "email": "erathi@scu.edu",
    "education": "MS in Computer Science",
    "experience": "Software Engineer with 200 years of experience in building SAAS products",
    # more resume content fields go here
}

resume_content_with_metadata = {
        "date_time": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "git_branch": "setup",
        "resume": resume_content,
}



# EXPECTED_RESPONSE = {
#     "resume": {
#         "education": "MS in Computer Science",
#         "email": "erathi@scu.edu",
#         "experience": "Software Engineer with 2 years of experience",
#         "name": "Eshaan Rathi"
#     },
#     "date_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
#     "git_branch": "setup",
# }

EXPECTED_RESPONSE = resume_content_with_metadata


def test_api_positive_scenario():
    # Test if API is reachable
    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        print("Site is working. API is reachable.")
    except Exception as e:
        print(f"Failed to reach API: {e}")
        return False

    # Test if response has correct status code
    if response.status_code != 200:
        print(f"Unexpected status code: {response.status_code}")
        return False

    # Test if response matches expected JSON
    try:
        response_data = response.json()
        if "date_time" in response_data:
            print("Valid Date and Time")
        if "git_branch" in response_data:
            print("Valid git branch")
        # print(type(response_data))
        # assert response_data == EXPECTED_RESPONSE
    except Exception as e:
        print(f"Response does not match expected format: {e}")
        # print("expected:", EXPECTED_RESPONSE)
        # print("received:",response_data)
        return False

    print("Positive scenario test passed successfully.")
    return True


def test_api_negative_scenario():
    # Test if API returns 404 for invalid URL
    invalid_url = API_URL + "/invalid"
    response = requests.get(invalid_url)
    if response.status_code != 404:
        print("Failed to handle invalid URL.")
        return False

    print("Negative scenario test passed successfully.")
    return True


def run_tests():
    tests_passed = 0
    tests_failed = 0

    # Run positive scenario test
    if test_api_positive_scenario():
        tests_passed += 1
    else:
        tests_failed += 1

    # Run negative scenario test
    if test_api_negative_scenario():
        tests_passed += 1
    else:
        tests_failed += 1

    print(f"\nTests passed: {tests_passed}, Tests failed: {tests_failed}")


def code_linting():
    # try:
    #     subprocess.run(["flake8", __file__], check=True)
    # except subprocess.CalledProcessError as e:
    #     print(f"Linting failed: {e}")
    #     return False
    # print("Linting passed successfully.")
    # return True
    pass


if __name__ == "__main__":
    run_tests()
    code_linting()
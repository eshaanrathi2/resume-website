import requests
import time
from datetime import datetime
from subprocess import check_output

def test_get_resume_data():
    """
    Tests the / endpoint for valid response and data inclusion.
    """
    response = requests.get("http://localhost/api/resume")
    assert response.status_code == 200

    response_data = response.json()
    assert "data" in response_data
    assert "date_time" in response_data
    assert "git_branch" in response_data

    # Assert presence of expected resume data keys
    for key in ["name", "profile", "skills", "experience"]:
        assert key in response_data["data"]

    # Validate date/time format
    try:
        datetime.strptime(response_data["date_time"], "%Y-%m-%d %H:%M:%S")
    except ValueError:
        assert False, "Invalid date/time format in response."

    # Validate git branch name (optional, adapt based on expectations)
    expected_branch = "feature/my-new-feature"  # Example, replace with expected branch
    assert response_data["git_branch"] == expected_branch

def test_get_specific_section():
    """
    Tests the /sections/ endpoint for valid response and data.
    """
    valid_section = "skills"
    response = requests.get(f"http://localhost/api/sections/{valid_section}")
    assert response.status_code == 200

    response_data = response.json()
    assert "data" in response_data
    assert response_data["data"] == resume_data[valid_section]

    invalid_section = "invalid_section"
    response = requests.get(f"http://localhost/api/sections/{invalid_section}")
    assert response.status_code == 404
    assert "error" in response.json()

# Add

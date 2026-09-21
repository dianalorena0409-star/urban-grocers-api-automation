# Urban Grocers API Test Automation

## Project Description

This project contains automated API tests for the Urban Grocers application. The tests validate the `name` field when creating a new product kit, including valid and invalid values, boundary values, special characters, spaces, numbers, and missing data.

The test flow creates a new user, retrieves an authentication token, and uses Bearer authentication to send requests for creating new kits.

## Technologies and Techniques

- Python
- Pytest
- Requests library
- REST API testing
- JSON request bodies
- Bearer token authentication
- Positive and negative testing
- Boundary Value Analysis
- Automated status code validation

## Automated Test Scenarios

The project includes 9 automated test scenarios for the kit `name` field:

1. Create a kit with a 1-character name
2. Create a kit with a 511-character name
3. Attempt to create a kit with an empty name
4. Attempt to create a kit with a 512-character name
5. Create a kit using special characters
6. Create a kit using spaces
7. Create a kit using numbers as text
8. Attempt to create a kit without the `name` field
9. Attempt to create a kit with a numeric value instead of a string

## Project Structure

- `configuration.py` – Base URL and API endpoint paths
- `data.py` – Request headers and test data
- `sender_stand_request.py` – Functions for sending API requests
- `create_kit_name_kit_test.py` – Automated test scenarios and assertions

## Test Validation

The automated tests validate the HTTP status codes returned by the API:

- `201 Created` for valid kit names
- `400 Bad Request` for invalid kit names according to the project requirements

A failed automated test indicates that the actual API response does not match the expected behavior defined by the test scenario.

## Running the Tests

1. Open the project in PyCharm.
2. Install the required Python packages, including `pytest` and `requests`.
3. Update `URL_SERVICE` in `configuration.py` with the current Urban Grocers server URL.
4. Run `create_kit_name_kit_test.py` using Pytest.

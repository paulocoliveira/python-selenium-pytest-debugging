import json

# Function to load data from a fixture file
def load_data_from_fixture(file_name):
    with open(file_name, "r") as file:
        return json.load(file)

# Sample test using data fixture
def test_using_data_fixture():
    test_data = load_data_from_fixture("test_data.json")
    print(test_data["valid_user"])
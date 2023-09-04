import pytest

# Simulated test functions

@pytest.mark.skip(reason="Temporarily disabled for debugging")
def test_temporarily_disabled():
    print("test will be skipped")

def test_simple_test():
    print("test will not be skipped")
import pytest

# Simulated test functions

@pytest.mark.failed
def test_failing_test():
    assert 2 + 2 == 5

@pytest.mark.slow
def test_slow_execution():
    import time
    time.sleep(3)  # Simulate a slow test
    assert True
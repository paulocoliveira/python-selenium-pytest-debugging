import pytest
import random

# Simulated function with intermittent failures
@pytest.mark.flaky(rerun=3)  # Retry the test up to 3 times
def test_intermittent_failure():
    if random.randint(0, 1) == 0:
        assert False  # Simulate a failure
    else:
        assert True
from utils import setup_custom_logger

def test_function_that_uses_logger():
    # Create two separate loggers, each with a unique name
    logger1 = setup_custom_logger("log1")

    # Log messages using different log levels for each logger
    logger1.info("This is an informational message for logger1")
    logger1.debug("This is a debug message for logger1")  # This will not be printed because the logger's level is INFO
    logger1.warning("This is a warning message for logger1")  # This will be printed
    logger1.error("This is an error message for logger2")  # This will be printed
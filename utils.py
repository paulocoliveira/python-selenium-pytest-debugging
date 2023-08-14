import logging

def setup_custom_logger(name):
    # Define a log message format with date, log level, and the message itself
    formatter = logging.Formatter(fmt='%(asctime)s - %(levelname)s - %(message)s',
                                  datefmt='%Y-%m-%d %H:%M:%S')

    # Create a file handler that will write log messages to the "test.log" file
    handler = logging.FileHandler("test.log")
    handler.setFormatter(formatter)

    # Create a logger with the given name
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)  # Set the logger's level to the lowest level (DEBUG) to capture all messages
    logger.addHandler(handler)  # Attach the file handler to the logger

    return logger

def capture_screenshot(driver, screenshot_path):
    driver.save_screenshot(screenshot_path)
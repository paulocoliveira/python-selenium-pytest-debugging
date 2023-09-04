from utils import setup_custom_logger
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_function_that_uses_logger():

    logger1 = setup_custom_logger("log1")

    driver = webdriver.Chrome()

    logger1.info("This is an informational message for logger1! Chrome driver was set!")  # This will be printed

    driver.maximize_window()

    driver.get("https://www.lambdatest.com/selenium-playground/simple-form-demo")

    logger1.info("This is an informational message for logger1! Chrome windows was maximized and url was opened!")  # This will be printed

    try:
        logger1.warning("This is a warning message for logger1! Next line will try to locate an element and can generate an error!")  # This will be printed
        input_element = driver.find_element(By.ID, "user-messages")
    except:
        logger1.error("This is an error message for logger1! Element was not found!")  # This will be printed

    driver.quit()

# Call the test function
test_function_that_uses_logger()
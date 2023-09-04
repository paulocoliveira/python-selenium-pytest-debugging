from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

def test_no_such_element_exception():
    # Set up the webdriver
    driver = webdriver.Chrome()

    # Navigate to a web page with dynamic content
    driver.get("https://www.lambdatest.com/selenium-playground/simple-form-demo")

    try:
        # Attempt to locate a dynamic element that might not be present
        dynamic_element = driver.find_element(By.ID, "important-message")
    except NoSuchElementException as e:
        print("NoSuchElementException occurred:", e)
    finally:
        # Close the webdriver
        driver.quit()
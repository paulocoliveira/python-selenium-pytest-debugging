from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_timeout_exception():
    # Set up the webdriver
    driver = webdriver.Chrome()

    # Navigate to a web page with a dynamically loading element
    driver.get("https://www.lambdatest.com/selenium-playground/simple-form-demo")

    try:
        # Wait for a dynamically loading element to become visible
        wait = WebDriverWait(driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.ID, "important-message")))

        # Interact with the loaded element
        element.click()
    except TimeoutException as e:
        print("TimeoutException occurred:", e)
    finally:
        # Close the webdriver
        driver.quit()
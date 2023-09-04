from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotInteractableException

def test_element_not_interactable_exception():
    # Set up the webdriver
    driver = webdriver.Chrome()

    # Navigate to a web page with a disabled element
    driver.get("https://www.lambdatest.com/selenium-playground/simple-form-demo")

    try:
        # Attempt to interact with a hidden element
        hidden_element = driver.find_element(By.ID, "message")
        hidden_element.click()
    except ElementNotInteractableException as e:
        print("ElementNotInteractableException occurred:", e)
    finally:
        # Close the webdriver
        driver.quit()
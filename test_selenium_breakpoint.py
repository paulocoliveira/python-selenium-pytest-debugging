from selenium import webdriver
from selenium.webdriver.common.by import By

def test_breakpoint():
    driver = webdriver.Chrome()

    driver.maximize_window()

    driver.get("https://www.lambdatest.com/selenium-playground/simple-form-demo")
    
    breakpoint()

    # Find an input element by its ID and enter text
    input_element = driver.find_element(By.ID, "user-messages")

    driver.quit
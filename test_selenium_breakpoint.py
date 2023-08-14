from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

def test_breakpoint():
    service = Service()
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)

    driver.maximize_window()

    driver.get("https://www.lambdatest.com/selenium-playground/simple-form-demo")
    
    breakpoint()

    # Find an input element by its ID and enter text
    input_element = driver.find_element(By.ID, "user-messages")

    driver.quit
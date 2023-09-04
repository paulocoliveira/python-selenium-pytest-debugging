from selenium import webdriver
from selenium.webdriver.common.by import By

def test_screenshot_1():
    driver = webdriver.Chrome()

    driver.maximize_window()

    driver.get("https://www.lambdatest.com/selenium-playground/simple-form-demo")

    input_element = driver.find_element(By.ID, "user-message")
    input_element.send_keys("This is a test text!")

    driver.save_screenshot('screenshots/fullpage.png')

    driver.quit()
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_pdb():
    driver = webdriver.Chrome()

    driver.maximize_window()

    driver.get("https://www.lambdatest.com/selenium-playground/simple-form-demo")

    input_element = driver.find_element(By.ID, "user-messages")

    driver.quit()

# Call the test function
test_pdb()

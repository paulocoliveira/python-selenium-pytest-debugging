from selenium import webdriver
from selenium.webdriver.common.by import By

def test_implicit_wait():
    # Set up the webdriver with an implicit wait
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)  # Wait for 10 seconds

    # Navigate to the web page
    driver.get("https://ecommerce-playground.lambdatest.io/")

    # Find an element using implicit wait
    add_to_cart_button = driver.find_element(By.CLASS_NAME, "addToCart")
    add_to_cart_button.click()

    # Close the webdriver
    driver.quit()
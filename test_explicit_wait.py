from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_explicit_wait():
    # Set up the webdriver
    driver = webdriver.Chrome()

    # Navigate to the web page
    driver.get("https://ecommerce-playground.lambdatest.io/")

    # Explicitly wait for the "Add to Cart" button to be clickable
    wait = WebDriverWait(driver, 10)
    add_to_cart_button = wait.until(EC.element_to_be_clickable((By.ID, "addToCart")))
    add_to_cart_button.click()

    # Close the webdriver
    driver.quit()
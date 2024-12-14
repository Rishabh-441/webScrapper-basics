from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from credentials import username
from credentials import password


# Initialize the WebDriver
driver = webdriver.Chrome()

# Open the Amazon product page
driver.get('https://www.amazon.in/Apple-MacBook-Chip-13-inch-256GB/dp/B08N5W4NNB/ref=sr_1_4')

# Wait for the page to load completely
try:
    # Wait for the "See All Reviews" link to become clickable
    reviews_url = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@data-hook="see-all-reviews-link-foot"]'))
    )
    # Click the link
    reviews_url.click()

    # Wait for the login form (if it appears)
    email_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'ap_email'))
    )
    # Enter text into the email field
    email_field.send_keys(username)
    print("Entered text into the email field.")

    continue_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'continue'))
    )
    continue_button.click()

    password_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'ap_password'))
    )
    password_field.send_keys(password)

    submit_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'signInSubmit'))
    )
    submit_button.click()



except Exception as e:
    print(f"An error occurred: {e}")

# Pause to view the result and then close the browser
input("Press Enter to close the browser...")
driver.quit()

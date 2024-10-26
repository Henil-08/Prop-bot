from constants import WEBSITE
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def login_to_propstream(username, password, driver):
    driver.get(WEBSITE)
    wait = WebDriverWait(driver, 10)  # Wait for up to 10 seconds

    # Wait for the username and password fields to be present
    username_field = wait.until(EC.presence_of_element_located((By.NAME, "username")))  # Using By.NAME
    password_field = wait.until(EC.presence_of_element_located((By.NAME, "password")))  # Using By.NAME
    
    username_field.send_keys(username)
    password_field.send_keys(password)

    # Submit the login form using the button text instead of ID
    login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Login']")))
    login_button.click()

    # Wait for URL to change after login
    wait.until(EC.url_changes(driver.current_url))
    print("Login successful!")


def search_city(city, driver):
    wait = WebDriverWait(driver, 10)

    # Enter the city in the search box
    search_box = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter County, City, Zip Code(s) or APN #']")))
    search_box.clear()
    search_box.send_keys(city)

    # Wait for the suggestion box to be populated
    suggestion_xpath = "//input[@aria-activedescendant='react-autowhatever-1--item-0']"
    wait.until(EC.presence_of_element_located((By.XPATH, suggestion_xpath)))
    search_box.send_keys(Keys.RETURN) 

    print("First suggestion selected and search triggered.")
    print(f"Search completed for city: {city}")
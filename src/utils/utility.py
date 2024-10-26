import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException

def save_to_csv(data):
    df = pd.DataFrame(data)
    return df.to_csv(index=False).encode('utf-8')

def get_total_listings(driver):
    # Get the total number of listings
    total_listings_text = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='root']/div/div[2]/div/div/div[3]/div[1]/div/section/div[2]/div/div/div/div/div[1]/div[1]/div[2]"))
    ).text

    # Extract the number of listings and convert to int
    total_listings = int(total_listings_text.split(" ")[-1].strip("()")) 
    print(f"Total listings: {total_listings}")
    return total_listings

def go_to_page(driver, page_number):
    try:
        input_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='root']/div/div[2]/div/div/div[3]/div[1]/div/section/div[2]/div/div/div/div/div[3]/div/input"))  # Update the XPath for the page input field
        )
        # Clear the current input, enter the new page number, and trigger a change
        input_field.clear()
        input_field.send_keys(str(page_number))
        input_field.send_keys(Keys.RETURN)  # Simulate pressing Enter
        print(f"Navigated to page {page_number}")
    except StaleElementReferenceException:
        go_to_page(driver, page_number)  # Retry if there's a StaleElementReferenceException


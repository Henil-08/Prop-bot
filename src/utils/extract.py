import time
from utils import utility
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def extract_details(driver):
    wait = WebDriverWait(driver, 15) 
    
    listings_data = {}

    # Owner Information
    for i in range(1, 5):
        label = wait.until(EC.presence_of_element_located((By.XPATH, f'/html/body/div[2]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div/div/div/div/div[2]/div[{i}]/div/div[1]'))).text
        value = wait.until(EC.presence_of_element_located((By.XPATH, f'/html/body/div[2]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div/div/div/div/div[2]/div[{i}]/div/div[2]/div'))).text
        listings_data.update({label: value})

    # Estimated Value
    label = wait.until(EC.presence_of_element_located((By.XPATH, f'//*[@id="propertyDetail"]/div/div/div[2]/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[1]/div[1]'))).text
    value = wait.until(EC.presence_of_element_located((By.XPATH, f'//*[@id="propertyDetail"]/div/div/div[2]/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[1]/div[2]'))).text
    listings_data.update({label: value})

    # Estimated Balance
    label = wait.until(EC.presence_of_element_located((By.XPATH, f'//*[@id="propertyDetail"]/div/div/div[2]/div/div/div/div[1]/div[3]/div/div/div/div/div/div[1]/div[2]/div[2]/div[1]'))).text
    value = wait.until(EC.presence_of_element_located((By.XPATH, f'//*[@id="propertyDetail"]/div/div/div[2]/div/div/div/div[1]/div[3]/div/div/div/div/div/div[1]/div[2]/div[2]/div[2]'))).text
    listings_data.update({label: value})

    # Equity
    label = wait.until(EC.presence_of_element_located((By.XPATH, f'//*[@id="propertyDetail"]/div/div/div[2]/div/div/div/div[1]/div[4]/div/div/div/div/div/div[2]'))).text
    value = wait.until(EC.presence_of_element_located((By.XPATH, f'//*[@id="propertyDetail"]/div/div/div[2]/div/div/div/div[1]/div[4]/div/div/div/div/div/ul/li[1]'))).text
    listings_data.update({label: value})

    # Recording Date
    pfc = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div[2]/div/div/div/div[2]/div/div/ul/li[2]'))
    )
    pfc.click()
    for i in range(1, 5):
        # Get the label and value divs inside each property detail
        label = wait.until(EC.presence_of_element_located((By.XPATH, f'/html/body/div[2]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div[2]/div/div/div/div[2]/div/div/div[2]/div[1]/div/div/div/div/div[3]/div[{i}]/div/div[1]'))).text
        value = wait.until(EC.presence_of_element_located((By.XPATH, f'/html/body/div[2]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div[2]/div/div/div/div[2]/div/div/div[2]/div[1]/div/div/div/div/div[3]/div[{i}]/div/div[2]/div'))).text
        listings_data.update({label: value})
    property = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div[2]/div/div/div/div[2]/div/div/ul/li[1]'))
    )
    property.click()

    # Property information
    for i in range(1, 12):
        label = wait.until(EC.presence_of_element_located((By.XPATH, f'//*[@id="propertyDetail"]/div/div/div[2]/div/div/div/div[1]/div[1]/div/div/div/div/div[2]/div[{i}]/div[1]'))).text
        value = wait.until(EC.presence_of_element_located((By.XPATH, f'//*[@id="propertyDetail"]/div/div/div[2]/div/div/div/div[1]/div[1]/div/div/div/div/div[2]/div[{i}]/div[2]'))).text
        listings_data.update({label: value})
    
    
    # Bed
    label = wait.until(EC.presence_of_element_located((By.XPATH, f'//*[@id="propertyDetail"]/div/div/div[2]/div/div/div/div[1]/div[1]/div/div/div/div/div[1]/div[2]/div[1]/div[1]/div/span[1]'))).text
    value = wait.until(EC.presence_of_element_located((By.XPATH, f'//*[@id="propertyDetail"]/div/div/div[2]/div/div/div/div[1]/div[1]/div/div/div/div/div[1]/div[2]/div[1]/div[1]/div/span[2]'))).text
    listings_data.update({label: value})
    
    # Bath
    label = wait.until(EC.presence_of_element_located((By.XPATH, f'//*[@id="propertyDetail"]/div/div/div[2]/div/div/div/div[1]/div[1]/div/div/div/div/div[1]/div[2]/div[1]/div[2]/div/span[1]'))).text
    value = wait.until(EC.presence_of_element_located((By.XPATH, f'//*[@id="propertyDetail"]/div/div/div[2]/div/div/div/div[1]/div[1]/div/div/div/div/div[1]/div[2]/div[1]/div[2]/div/span[2]'))).text
    listings_data.update({label: value})

    # Property information
    for i in range(2, 6):
        # Get the label and value divs inside each property detail
        label = wait.until(EC.presence_of_element_located((By.XPATH, f'//*[@id="propertyDetail"]/div/div/div[2]/div/div/div/div[1]/div[1]/div/div/div/div/div[1]/div[2]/div[{i}]/div[1]'))).text
        value = wait.until(EC.presence_of_element_located((By.XPATH, f'//*[@id="propertyDetail"]/div/div/div[2]/div/div/div/div[1]/div[1]/div/div/div/div/div[1]/div[2]/div[{i}]/div[2]'))).text
        listings_data.update({label: value})


    close_xpath = f'//*[@id="propertyDetail"]/div/div/div[1]/button'
    close = wait.until(EC.element_to_be_clickable((By.XPATH, close_xpath)))
    close.click()

    return listings_data


def get_listings_data(driver, listings):
    wait = WebDriverWait(driver, 15) 
    
    listings_data = []
    
    # Get all listings
    for i in range (1, listings+1):
        try:
            detail_xpath = f'//*[@id="root"]/div/div[2]/div/div/div[3]/div[1]/div/section/div[2]/div/div/div/div/div[2]/div/div[{i}]/div[3]/div[1]/div[1]/a'
            detail = wait.until(EC.element_to_be_clickable((By.XPATH, detail_xpath)))
            detail.click()

            # Wait for a specific element that indicates the new page has loaded
            time.sleep(2)
            data = extract_details(driver)
            listings_data.append(data)
        except Exception as e: print('Error Occured!', e)
        

    return listings_data


def get_search_data(driver, total_pages, total_listings):
    # Loop through all pages
    all_listings_data = []
    for page in range(1, total_pages + 1):
        # Get listings data from the current page
        if total_pages != 1:
            utility.go_to_page(driver, page)

        listings_data = get_listings_data(driver, total_listings)
        all_listings_data.extend(listings_data)  # Add data to the overall list
        
        # Wait for the page to load
        time.sleep(2)  

    return all_listings_data
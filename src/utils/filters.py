
from datetime import datetime, timedelta
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def click_filter_button(driver):
    wait = WebDriverWait(driver, 15)  
    try:
        # Locate and click the filter button using XPath
        filter_button_xpath = "//*[@id='root']/div/div[2]/div/div/div[3]/div[1]/div/header/div[1]/div[1]/div[2]/div"
        filter_button = wait.until(EC.element_to_be_clickable((By.XPATH, filter_button_xpath)))
        filter_button.click() 
        print("Filter button clicked and menu opened.")
    except Exception as e:
        print(f"An error occurred: {e}")


def select_filter_option(driver, option):
    wait = WebDriverWait(driver, 15)  
    try:
        # Locate the dropdown menu using XPath
        dropdown_xpath = "//*[@id='root']/div/div[2]/div/div/div[3]/div[1]/div/header/div[1]/div[1]/div[2]/div/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div/div/div/select"
        dropdown_menu = wait.until(EC.element_to_be_clickable((By.XPATH, dropdown_xpath)))
        dropdown_menu.click()

        # Select the Pre-Foreclosures
        select = Select(dropdown_menu)
        select.select_by_visible_text("Pre-Foreclosures")
        dropdown_menu.click()

        # Select Property Type
        property_xpath = '//*[@id="root"]/div/div[2]/div/div/div[3]/div[1]/div/header/div[1]/div[1]/div[2]/div/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/span'
        property_span = wait.until(EC.element_to_be_clickable((By.XPATH, property_xpath)))
        property_span.click()
        dropdown_xpath = '//*[@id="root"]/div/div[2]/div/div/div[3]/div[1]/div/header/div[1]/div[1]/div[2]/div/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div[2]/div[2]/div/div/div/div[2]'
        dropdown_menu = wait.until(EC.element_to_be_clickable((By.XPATH, dropdown_xpath)))
        dropdown_menu.click()
        single = '//*[@id="root"]/div/div[2]/div/div/div[3]/div[1]/div/header/div[1]/div[1]/div[2]/div/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div[2]/div[2]/div/div/div/div[1]/div[2]/div/div[1]/label/span'
        single_span = wait.until(EC.element_to_be_clickable((By.XPATH, single)))
        single_span.click()
        condo = '//*[@id="root"]/div/div[2]/div/div/div[3]/div[1]/div/header/div[1]/div[1]/div[2]/div/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div[2]/div[2]/div/div/div/div[1]/div[2]/div/div[2]/label/span'
        condo_span = wait.until(EC.element_to_be_clickable((By.XPATH, condo)))
        condo_span.click()
        dropdown_menu.click()

        # Select On Market Status
        mls_status_span_xpath = '//*[@id="root"]/div/div[2]/div/div/div[3]/div[1]/div/header/div[1]/div[1]/div[2]/div/div[2]/div[2]/div[1]/div[1]/div[3]/div[1]/span'
        mls_status_span = wait.until(EC.element_to_be_clickable((By.XPATH, mls_status_span_xpath)))
        mls_status_span.click()
        no_button_xpath = '//*[@id="root"]/div/div[2]/div/div/div[3]/div[1]/div/header/div[1]/div[1]/div[2]/div/div[2]/div[2]/div[1]/div[1]/div[3]/div[2]/div/div[1]/div[3]/div/label/span'
        no_button = wait.until(EC.element_to_be_clickable((By.XPATH, no_button_xpath)))
        no_button.click()
        mls_status_span.click()
        
        # Select Pre-Foreclosure Options
        pfc_xpath = '//*[@id="root"]/div/div[2]/div/div/div[3]/div[1]/div/header/div[1]/div[1]/div[2]/div/div[2]/div[2]/div[1]/div[1]/div[4]/div[1]/span'
        pfc = wait.until(EC.element_to_be_clickable((By.XPATH, pfc_xpath)))
        pfc.click()
        dropdown_xpath = '//*[@id="root"]/div/div[2]/div/div/div[3]/div[1]/div/header/div[1]/div[1]/div[2]/div/div[2]/div[2]/div[1]/div[1]/div[4]/div[2]/div[1]/div[2]/div/div/div/div[2]'
        dropdown_menu = wait.until(EC.element_to_be_clickable((By.XPATH, dropdown_xpath)))
        dropdown_menu.click()
        notice = '//*[@id="root"]/div/div[2]/div/div/div[3]/div[1]/div/header/div[1]/div[1]/div[2]/div/div[2]/div[2]/div[1]/div[1]/div[4]/div[2]/div[1]/div[2]/div/div/div/div[1]/div/div/div[1]/label/span'
        notice_span = wait.until(EC.element_to_be_clickable((By.XPATH, notice)))
        notice_span.click()
        auction = '//*[@id="root"]/div/div[2]/div/div/div[3]/div[1]/div/header/div[1]/div[1]/div[2]/div/div[2]/div[2]/div[1]/div[1]/div[4]/div[2]/div[1]/div[2]/div/div/div/div[1]/div/div/div[2]/label/span'
        auction_span = wait.until(EC.element_to_be_clickable((By.XPATH, auction)))
        auction_span.click()
        dropdown_menu.click()
        date_input_xpath = '//*[@id="root"]/div/div[2]/div/div/div[3]/div[1]/div/header/div[1]/div[1]/div[2]/div/div[2]/div[2]/div[1]/div[1]/div[4]/div[2]/div[2]/div[2]/div/div/div/div/div/input'
        date_input_field = wait.until(EC.element_to_be_clickable((By.XPATH, date_input_xpath)))
        three_months_ago = datetime.now() - timedelta(days=90)  # Approximately 3 months (90 days)
        formatted_date = three_months_ago.strftime("%m/%d/%y")  # Format date as MM/DD/YY
        date_input_field.clear()  # Clear the existing date if any
        date_input_field.send_keys(formatted_date)  # Enter the new date
        pfc.click()

        if option:
            # Select Owner Options
            owner_xpath = '//*[@id="root"]/div/div[2]/div/div/div[3]/div[1]/div/header/div[1]/div[1]/div[2]/div/div[2]/div[2]/div[1]/div[1]/div[5]/div[1]/span'
            owner = wait.until(EC.element_to_be_clickable((By.XPATH, owner_xpath)))
            owner.click()
            dropdown_xpath = '//*[@id="root"]/div/div[2]/div/div/div[3]/div[1]/div/header/div[1]/div[1]/div[2]/div/div[2]/div[2]/div[1]/div[1]/div[5]/div[2]/div[2]/div[2]/div/div/div/div[2]'
            dropdown_menu = wait.until(EC.element_to_be_clickable((By.XPATH, dropdown_xpath)))
            dropdown_menu.click()
            individual = '//*[@id="root"]/div/div[2]/div/div/div[3]/div[1]/div/header/div[1]/div[1]/div[2]/div/div[2]/div[2]/div[1]/div[1]/div[5]/div[2]/div[2]/div[2]/div/div/div/div[1]/div/div/div[1]/label/span'
            individual_span = wait.until(EC.element_to_be_clickable((By.XPATH, individual)))
            individual_span.click()
            trust = '//*[@id="root"]/div/div[2]/div/div/div[3]/div[1]/div/header/div[1]/div[1]/div[2]/div/div[2]/div[2]/div[1]/div[1]/div[5]/div[2]/div[2]/div[2]/div/div/div/div[1]/div/div/div[4]/label/span'
            trust_span = wait.until(EC.element_to_be_clickable((By.XPATH, trust)))
            trust_span.click()
            dropdown_menu.click()
            owner.click()

            # Select Loan Value Options
            loan_xpath = '//*[@id="root"]/div/div[2]/div/div/div[3]/div[1]/div/header/div[1]/div[1]/div[2]/div/div[2]/div[2]/div[1]/div[1]/div[7]/div[1]/span'
            loan = wait.until(EC.element_to_be_clickable((By.XPATH, loan_xpath)))
            loan.click()
            loan_input_xpath = '//*[@id="root"]/div/div[2]/div/div/div[3]/div[1]/div/header/div[1]/div[1]/div[2]/div/div[2]/div[2]/div[1]/div[1]/div[7]/div[2]/div[8]/div[3]/div/div/input'
            loan_input_field = wait.until(EC.element_to_be_clickable((By.XPATH, loan_input_xpath)))
            loan_input_field.clear()
            loan_input_field.send_keys('75')
            loan.click()


        wait = WebDriverWait(driver, 10)

        # Close the filter tab
        close_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".icon-iconClose.src-app-Search-Header-style__SAkaa__iconClose")))
        close_button.click()
        print('Filters Applied')
    except Exception as e:
        print(f"An error occurred: {e}")
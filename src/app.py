import math
import streamlit as st
from selenium import webdriver
from constants import USERNAME, PASSWORD
from utils import login, utility, filters, extract

## set up Streamlit 
st.set_page_config(page_title="Prop-stream Bot", page_icon="🏢")
st.title("Prop-stream Bot")

city = st.text_input("Enter the City Name:")
option = st.selectbox('Select your search options', ('Standard', 'High Equity'))

if city and option:
    # Initialize the WebDriver 
    driver = webdriver.Chrome()  

    # Login and Search City
    login.login_to_propstream(USERNAME, PASSWORD, driver)
    login.search_city(city, driver)

    # Select Filters
    filters.click_filter_button(driver)
    filters.select_filter_option(driver, False) if option == 'Standard' else filters.select_filter_option(driver, True)

    # Get the total number of listings
    total_listings = utility.get_total_listings(driver)
    listings_per_page = 50  # Assuming 50 listings per page
    total_pages = math.ceil(total_listings / listings_per_page)  # Calculate total pages
    
    all_listings_data = extract.get_search_data(driver, total_pages, total_listings)
    driver.quit()
    
    csv = utility.save_to_csv(all_listings_data)

    st.download_button(
        "Press to Download",
        csv,
        f"{city}_{option}.csv",
        "text/csv",
        key='download-csv'
    )

    st.write("Search Complete")


    
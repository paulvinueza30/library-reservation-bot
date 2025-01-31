from datetime import datetime, timedelta
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


def get_date_one_week_in_advance():
    
    current_date = datetime.now()
    future_date = current_date + timedelta(weeks=1)
    return future_date

def navigate_to_date(driver):
    # Click calendar button to open the date picker
    go_to_date_button = driver.find_element(By.CLASS_NAME, "fc-goToDate-button")
    go_to_date_button.click()

    # Get the current date and calculate the date one week in advance
    target_date = get_date_one_week_in_advance()

    # If the target date is in the next month or year, click the "next" button
    current_month = datetime.now().month
    current_year = datetime.now().year
    
    if target_date.month != current_month or target_date.year != current_year:
        next_button = driver.find_element(By.CLASS_NAME, "next")
        next_button.click()

    # Click the target date
    day_cell = driver.find_elements(By.XPATH, f"//td[contains(@class, 'day') and text()='{target_date.day}']")
    
    if day_cell:
        day_cell[0].click()  # Click the first matching day
        
def select_category(driver, option_value):
    # Locate category element
    select_element = driver.find_element(By.ID, "capacity")
    
    # Create a Select object to interact with the dropdown
    select = Select(select_element)
    
    # Select the option by value (0, 1, or 2)
    select.select_by_value(str(option_value))
    
    
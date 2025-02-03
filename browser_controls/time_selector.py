import time
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

def convert_start_time_to_string(start_time: float):
    """
    Converts the start time (rounded to the nearest hour) into a string.
    """
    # Round to the nearest hour (in case it's already rounded)
    rounded_time = int(start_time)
    
    # Create a datetime object for the rounded time (whole hour)
    time_obj = datetime.strptime(f"{rounded_time}", "%H")
    
    # Return the time in the desired format ('1:00pm', '2:00pm', etc.)
    time_str = time_obj.strftime("%l:%M%p").strip() 
    
    return time_str.lower()

def convert_half_hour_time_to_string(start_time: float):
    """
    Converts the half-hour time into a string (e.g., 1:30 -> '1:30pm').
    """
    # Extract the hour and minutes
    hour = int(start_time)
    minute = 30  # Always half an hour

    # Create a datetime object for the half-hour time
    time_obj = datetime.strptime(f"{hour}:{minute}", "%H:%M")
    
    # Return the time in the desired format ('1:30pm', '2:30pm', etc.)
    time_str = time_obj.strftime("%l:%M%p").strip()

    return time_str.lower()

def scroll_to_time(driver, start_time):
    time_str = convert_start_time_to_string(start_time)
    
    # Wait for the top-left corner element to be present and clickable
    top_left_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='eq-time-grid']/div[2]/div/table/thead/tr/td[3]/div/div/div/table/tbody/tr/th[1]/div/span"))
    )
    ActionChains(driver).move_to_element(top_left_element).click().perform()
    
    # Wait for the grid to load and be in focus
    WebDriverWait(driver, 10).until(
        EC.visibility_of(top_left_element)
    )
    
    # Scroll horizontally until the time span is found
    while True:
        driver.execute_script("window.scrollBy(200, 0);")  # Adjust scroll speed
        time_span = driver.find_elements(By.XPATH, f"//span[contains(text(), '{time_str}')]")
        
        if time_span:
            driver.execute_script("arguments[0].scrollIntoView(true);", time_span[0])
            break

def select_time_block(driver, start_time, end_time, max_retries=5):
    scroll_to_time(driver, start_time)
    retries = 0
    
    while retries < max_retries:
        time_str = convert_start_time_to_string(start_time)
        
        xpath = f"//a[contains(@title, 'Available') and contains(@title, '{time_str}') and contains(@class, 'fc-timeline-event')]"
        try:
            available_slot = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, xpath))
            )
            available_slot.click()
            print(f"Time block {time_str} selected successfully.")
            # Scroll the page by small increments until reaching the bottom
            for _ in range(2):  # You can increase the range if needed
                driver.execute_script("window.scrollBy(0, 1000);")  # Scroll by 1000px down
                time.sleep(1)  # Short pause between scrolls to allow for rendering

            desired_slots = int((end_time - start_time) / .5)
            select_reservation_length(driver, desired_slots)

            submit_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, "submit_times"))
            )
            submit_button.click()
            print("Times submitted successfully.")
            return True
        
        except Exception as e:
            print(f"Error: Could not find or click the time block {time_str}. Details: {str(e)}")
            start_time += 0.5
            print("UPDATED START TIME: " + str(start_time))
            retries += 1
    
    print(f"Could not find an available time block after {max_retries} attempts.")
    return False

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def select_reservation_length(driver, slots):
    """
    Selects the reservation length from the dropdown menu based on the number of slots requested.
    """
    if slots <= 0:
        print("Error: The number of slots must be greater than 0.")
        return
    
    if slots > 16:
        print("Error: The number of slots must be 16 or fewer.")
        return
    
    try:
        # Wait for the dropdown to be visible using Expected Conditions
        dropdown_xpath = "//select[starts-with(@id, 'bookingend')]"
        
        booking_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, dropdown_xpath))
        )
        
        # Scroll the dropdown into view (this can help if it's off-screen or covered by something)
        driver.execute_script("arguments[0].scrollIntoView(true);", booking_input)
        
        # Get all options in the dropdown
        options = driver.find_elements(By.XPATH, "//select[starts-with(@id, 'bookingend')]/option")
        
        # Check available slots
        available_slots = len(options)
        print(f"Available slots: {available_slots}")
        
        # Determine the index to select (indexing starts at 0, so subtract 1 for 1-based index)
        if slots <= available_slots:
            index_to_select = slots - 1  # Slots are 1-based
            print(f"Selecting slot number {slots} ({options[index_to_select].text})")
        else:
            index_to_select = available_slots - 1  # Select max available slot
            print(f"Requested {slots} slots, but only {available_slots} are available. Selecting max available slot.")
        
        # Click the desired option
        options[index_to_select].click()
        print(f"Reservation length of {options[index_to_select].text} selected.")
    
    except Exception as e:
        print(f"Error: Could not select the reservation length. Details: {str(e)}")
        return

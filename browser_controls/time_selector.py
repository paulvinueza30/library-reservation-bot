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
    """
    Scrolls horizontally through the time grid to the right until the desired time span is visible.
    Then performs a specified number of right arrow key presses.
    """
    time_str = convert_start_time_to_string(start_time)
    
    # Locate the top-left corner element and click to focus
    top_left_element = driver.find_element(By.XPATH, "/html/body/div[3]/main/div/div/div/div[4]/div[1]/div[2]/div/table/tbody/tr[1]/td[3]/div/div/div/table/tbody/tr/th[1]")
    ActionChains(driver).move_to_element(top_left_element).click().perform()
    
    # Wait for grid to load and in focus
    time.sleep(1)
    
    # Scroll horizontally until the time span is found
    while True:
        driver.execute_script("window.scrollBy(300, 0);")  # Adjust scroll speed
        time_span = driver.find_elements(By.XPATH, f"//span[contains(text(), '{time_str}')]")
        
        if time_span:
            # Time span found, break the loop
            break
    
    # Perform additional right arrow key presses (if necessary)
    right_arrow_shift = 25
    for _ in range(right_arrow_shift):  
        ActionChains(driver).send_keys(Keys.ARROW_RIGHT).perform()
        time.sleep(0.2)  

def select_time_block(driver, start_time, end_time, max_retries=5):
    """
    Select the time block based on the time slot provided.
    Scrolls to the time slot and clicks on it if it's available.
    
    Retries for max_retries if the time block is not available.
    After successfully selecting the time, clicks on the "Submit Times" button.
    """
    scroll_to_time(driver = driver, start_time = start_time)
    retries = 0
    
    while retries < max_retries:
        
        # Determine if it's a half-hour or whole hour and convert accordingly
        if start_time % 1 == 0:
            time_str = convert_start_time_to_string(start_time)  # Use whole hour
        else:
            time_str = convert_half_hour_time_to_string(start_time)  # Use half hour
        
        # Construct the dynamic XPath with the formatted time string
        xpath = f"//a[contains(@title, 'Available') and contains(@title, '{time_str}')]"
        
        try:
            # Wait for the available slot to be clickable
            available_slot = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, xpath))
            )
            
            # Click the available time slot
            available_slot.click()
            print(f"Time block {time_str} selected successfully.")
            
            # Scroll to the bottom to ensure reservation length dropdown is visible
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            desired_slots = int((end_time - start_time) / .5)
            select_reservation_length(driver = driver, slots = desired_slots)
            
            # After selecting the time block, find and click the "Submit Times" button
            submit_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, "submit_times"))
            )
            submit_button.click()
            print("Times submitted successfully.")
            
            return True  # Exit function once the time block is clicked and submitted
        
        except Exception as e:
            print(f"Error: Could not find or click the time block {time_str}. Details: {str(e)}")
            
            # Increment start_time by 0.5 hours (30 minutes) for the next attempt
            start_time += 0.5
            print("UPDATED START TIME: " + str(start_time))
            retries += 1
    
    print(f"Could not find an available time block after {max_retries} attempts.")
    return False

def select_reservation_length(driver, slots):
    """
    Selects the reservation length from the dropdown menu based on the number of slots requested.
    Ensures that the number of slots is between 1 and 16.
    If the desired slots are not available, selects the maximum available length.
    """
    if slots <= 0:
        print("Error: The number of slots must be greater than 0.")
        return
    
    if slots > 16:
        print("Error: The number of slots must be 16 or fewer.")
        return
    
    try:
        # Wait for the booking end dropdown to be visible and interactable
        booking_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "bookingend_1"))
        )
        
        # Create a Select object to interact with the <select> dropdown
        select = Select(booking_input)
        
        # Get the list of all options in the dropdown
        options = select.options
        
        # If the dropdown has more options than the requested slots, attempt to select the corresponding option
        if len(options) >= slots:
            select.select_by_index(slots - 1)  # Slots are 1-based, so select by index (slots-1)
            print(f"Reservation length of {slots} slots selected.")
        else:
            # If the requested slots are not available, select the maximum available option
            max_length = len(options)  # Maximum available options
            select.select_by_index(max_length - 1)
            print(f"Requested {slots} slots, but only {max_length} slots are available. Max available length selected.")
    
    except Exception as e:
        print(f"Error: Could not select the reservation length. Details: {str(e)}")
import time
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

def convert_start_time_to_string(start_time: float):
    # Determine if it's a half-hour
    is_half_hour = start_time % 1 != 0  
    
    # Round the time to the nearest hour (floor it)
    rounded_time = int(start_time)  

    # Create a datetime object for the rounded time
    time_obj = datetime.strptime(f"{rounded_time}", "%H")
    
    # Return the time in the desired format
    time_str = time_obj.strftime("%l:%M%p").strip() 
    
    return time_str.lower(), is_half_hour

def scroll_to_time(driver, start_time):
    """
    Scrolls horizontally through the time grid to the right until the desired time span is visible.
    Then performs a specified number of right arrow key presses.
    """
    time_str, is_half_hour = convert_start_time_to_string(start_time)
    
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
            # print(f"Found the time block: {time_str}")
            break
    
    # Perform additional right arrow key presses
    right_arrow_shift = 18 if is_half_hour else 16
    for _ in range(right_arrow_shift):  
        ActionChains(driver).send_keys(Keys.ARROW_RIGHT).perform()
        time.sleep(0.2)  


def select_time_block(driver, start_time):
    """
    Select the time block based on the time slot provided.
    """
    scroll_to_time(driver = driver, start_time = start_time)

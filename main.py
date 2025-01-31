from config import get_driver
from preferences import Preferences

from reservation_helper import navigate_to_date, select_category
from time_selector import select_time_block

def main():
    preferences = Preferences()    
    
    driver = get_driver()
    driver.get("https://ucf.libcal.com/reserve/studyroom")
    driver.maximize_window()
   
        
    navigate_to_date(driver = driver)
    select_category(driver = driver, option_value= preferences.get_category_value())

    # Got preferences now scroll all the way down for time selection step
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    select_time_block(driver = driver, start_time = preferences.get_time_slot())

if __name__ == "__main__":
    main()

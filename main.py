from config.config import get_driver
from config.preferences import Preferences

from browser_controls.reservation_selector import navigate_to_date, select_category
from browser_controls.time_selector import select_time_block
from browser_controls.confirm_booking import find_continue, fill_reserver_info, submit_booking
from browser_controls.handle_mfa import handle_mfa

import time
def main():
    preferences = Preferences()    
    
    driver = get_driver()
    driver.get("https://ucf.libcal.com/reserve/studyroom")
    driver.maximize_window()
   
        
    navigate_to_date(driver = driver)
    select_category(driver = driver, option_value= preferences.get_category_value())

    # Got preferences now scroll all the way down for time selection step
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    time_confirmation = select_time_block(driver = driver, start_time = preferences.get_time_slot(), end_time = preferences.get_end_time())

    if time_confirmation:
        time.sleep(5)
        print(driver.current_url)
        if "microsoftonline" in driver.current_url:
            email , password = preferences.get_email_info()
            handle_mfa(driver = driver, email = email, password = password)
            time.sleep(5)
        find_continue(driver = driver)
        fill_reserver_info(driver = driver, public_name = preferences.get_public_name(), ucf_id = preferences.get_ucf_id())
        submit_booking(driver = driver)
        print("Reservation confirmed")
    driver.quit()

if __name__ == "__main__":
    main()

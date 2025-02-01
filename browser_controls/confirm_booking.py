from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


def find_continue(driver):
    continue_button = driver.find_element(By.ID, "terms_accept")
    continue_button.click()

def fill_reserver_info(driver, public_name, ucf_id):
    """
    Fill in the reservation information, such as public name, UCF ID, and select student type.
    """
    # Locate the public name input field by its ID and fill it in
    public_name_input = driver.find_element(By.ID, "nick")
    public_name_input.clear()  # Clear any existing text in the input
    public_name_input.send_keys(public_name)  # Fill the input with the provided public name
    
    # Locate the student type dropdown and select "Undergraduate Student"
    student_type_dropdown = driver.find_element(By.ID, "q2613")
    select = Select(student_type_dropdown)
    select.select_by_visible_text("Undergraduate Student")  # Select "Undergraduate Student" from the options

    # Locate the UCF ID input field by its ID and fill it in
    ucf_id_input = driver.find_element(By.ID, "q2614")
    ucf_id_input.clear()  # Clear any existing text in the input
    ucf_id_input.send_keys(ucf_id)  # Fill the input with the provided UCF ID


def submit_booking(driver):
    submit_booking_button = driver.find_element(By.ID, "btn-form-submit")
    submit_booking_button.click()
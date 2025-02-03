import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

def handle_mfa(driver, email, password):
    try:
        # Step 1: Submit email and password
        
        # Wait for the email input to be present using input[type="email"]
        email_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="email"]'))
        )
        # Clear the field (if needed) and enter the email
        email_input.clear()
        email_input.send_keys(email)
        email_input.send_keys(Keys.RETURN)  # Press Enter to proceed to the next step
        time.sleep(10)  # Give time for the password field to appear

        # Wait for the password input to be present (you can modify this if it's a different selector)
        password_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="password"]'))
        )
        # Clear the password field and enter the password
        password_input.clear()
        password_input.send_keys(password)
        password_input.send_keys(Keys.RETURN)  # Submit the password (Enter)
        print("Email and password submitted successfully.")
        
        # Step 2: Wait for MFA/Flow Token screen (after submitting credentials)
        WebDriverWait(driver, 20).until(
            EC.url_contains("microsoftonline.com")  # Check for MFA-related URL
        )

        # Step 3: Extract the flow token value (e.g., "99")
        flow_token_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "idRichContext_DisplaySign"))
        )
        flow_token_value = flow_token_element.text
        print(f"Flow Token: {flow_token_value}")

        # Step 4: Find and click the "Remember me for 180 days" checkbox (if present)
        try:
            remember_me_checkbox = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//input[@type='checkbox' and @name='KmsiCheckboxField']"))
            )
            if not remember_me_checkbox.is_selected():
                remember_me_checkbox.click()
                print("Remember me checkbox clicked.")
        except Exception as e:
            print("Remember me checkbox not found or error:", e)

        # Step 5: Wait for user approval (simulated with a 30-second delay)
        print("Waiting for your approval... You have 30 seconds to approve the request.")
        time.sleep(30)  # Adjust time for manual approval

        # Step 6: Find and click the submit button with value="Yes"
        yes_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@type='submit' and @value='Yes']"))
        )
        yes_button.click()  # Click the "Yes" submit button to proceed
        print("Submit 'Yes' button clicked.")

    except Exception as e:
        print(f"An error occurred: {e}")

# Usage Example:
# driver = webdriver.Chrome()  # Ensure your WebDriver is properly set up
# handle_mfa(driver, "your_email@example.com", "your_password")
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

def handle_mfa(driver, email, password):
    try:
        # Step 1: Submit email and password
        
        # Wait for the email input to be present using input[type="email"]
        email_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="email"]'))
        )
        # Clear the field (if needed) and enter the email
        email_input.clear()
        email_input.send_keys(email)
        email_input.send_keys(Keys.RETURN)  # Press Enter to proceed to the next step
        time.sleep(10)  # Give time for the password field to appear

        # Wait for the password input to be present (you can modify this if it's a different selector)
        password_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="password"]'))
        )
        # Clear the password field and enter the password
        password_input.clear()
        password_input.send_keys(password)
        password_input.send_keys(Keys.RETURN)  # Submit the password (Enter)
        print("Email and password submitted successfully.")
        
        # Step 2: Wait for MFA/Flow Token screen (after submitting credentials)
        WebDriverWait(driver, 20).until(
            EC.url_contains("microsoftonline.com")  # Check for MFA-related URL
        )

        # Step 3: Extract the flow token value (e.g., "99")
        flow_token_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "idRichContext_DisplaySign"))
        )
        flow_token_value = flow_token_element.text
        print(f"Flow Token: {flow_token_value}")
        time.sleep(15)  # Adjust time for manual approval

        # Step 4: Find and click the "Remember me for 180 days" checkbox (if present)
        try:
            remember_me_checkbox = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//input[@type='checkbox' and @name='KmsiCheckboxField']"))
            )
            if not remember_me_checkbox.is_selected():
                remember_me_checkbox.click()
                print("Remember me checkbox clicked.")
        except Exception as e:
            print("Remember me checkbox not found or error:", e)

        # Step 6: Find and click the submit button with value="Yes"
        yes_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@type='submit' and @value='Yes']"))
        )
        yes_button.click()  # Click the "Yes" submit button to proceed
        print("Submit 'Yes' button clicked.")

    except Exception as e:
        print(f"An error occurred: {e}")

# Usage Example:
# driver = webdriver.Chrome()  # Ensure your WebDriver is properly set up
# handle_mfa(driver, "your_email@example.com", "your_password")

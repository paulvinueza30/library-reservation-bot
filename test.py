from selenium import webdriver

# Set up Chrome options (optional)
chrome_options = webdriver.ChromeOptions()

# You can run Chrome in headless mode (no GUI) by uncommenting the line below
# chrome_options.add_argument("--headless")

# Initialize Chrome WebDriver
driver = webdriver.Chrome(options=chrome_options)

# Open YouTube
driver.get("https://www.youtube.com")

# Optionally, wait for a few seconds to ensure the page loads
import time
time.sleep(5)  # Wait for 5 seconds

# Close the browser after a delay (optional)
driver.quit()

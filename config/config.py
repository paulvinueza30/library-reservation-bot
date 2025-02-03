import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def get_driver():
    # Set up Chrome options
    chrome_options = Options()
    
    # Path to your Chrome binary (MacOS location)
    chrome_options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    
    # Chrome Profile options (optional, remove if not using a specific profile)
    # chrome_options.add_argument("--profile-directory=Default")  # Use your profile name, e.g., "Profile 1"
    
    # Optional: Run Chrome in headless mode (without UI)
    # chrome_options.add_argument("--headless")  # Uncomment if you want headless mode
    
    # Add additional Chrome options
    #chrome_options.add_argument("--no-sandbox")
    #chrome_options.add_argument("--disable-dev-shm-usage")
    #chrome_options.add_argument("--disable-software-rasterizer")  # Disables software rendering
    #chrome_options.add_argument("--start-maximized")  # Optional: Start browser maximized
    #chrome_options.add_argument("--disable-extensions")  # Disable unnecessary extensions
    
    # Path to the user data directory (replace with your actual directory if needed)
    # chrome_profile_dir = "/path/to/your/chrome-profile"  # Specify the correct profile directory if you want to use a specific profile
    # chrome_options.add_argument(f"user-data-dir={chrome_profile_dir}")

    # Path to ChromeDriver (should be installed via Homebrew)
    chromedriver_path = "/usr/local/bin/chromedriver"
    service = Service(chromedriver_path)

    # Create the Chrome driver with the specified options
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    return driver

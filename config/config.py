from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import os

def get_driver():
    # Set up Chrome options
    chrome_options = Options()
    chrome_options.binary_location = "/usr/bin/google-chrome"  # Path to your Chrome binary
    chrome_options.headless = True  # Change this to True if you want headless mode
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")  # Disables GPU acceleration
    chrome_options.add_argument("--disable-software-rasterizer")  # Disables software rendering
    chrome_options.add_argument("--start-maximized")  # Optional: Start browser maximized
    chrome_options.add_argument("--disable-extensions")  # Disable unnecessary extensions

    # Path to your transferred Chrome profile
    profile_path = os.path.expanduser("~/.config/google-chrome/User Data")
    
    # Specify a unique user data directory for Chrome (make sure to point to the correct profile)
    chrome_options.add_argument(f"user-data-dir={profile_path}")  # Use the profile from EC2 instance

    # Path to ChromeDriver (make sure it's in your PATH or provide full path)
    service = Service("/usr/local/bin/chromedriver")

    # Create the Chrome driver with the specified options
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    return driver

import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def get_driver():
    # Set up Chrome options
    chrome_options = Options()
    chrome_options.binary_location = "/usr/bin/google-chrome"  # Path to your Chrome binary
    chrome_options.headless = False  # Set to False to see the browser UI
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")  # Disables GPU acceleration
    chrome_options.add_argument("--disable-software-rasterizer")  # Disables software rendering
    chrome_options.add_argument("--start-maximized")  # Optional: Start browser maximized
    chrome_options.add_argument("--disable-extensions")  # Disable unnecessary extensions

    # Path to the uploaded Chrome profile on EC2 (ensure this is where you extracted it)
    user_data_dir = "/home/ubuntu/Chrome"  # Path where you extracted your Chrome profile on EC2
    profile_directory = "Profile 2"  # The name of your profile folder (e.g., Profile 2)

    # Create a unique user data directory to avoid conflicts
    unique_user_data_dir = f"{user_data_dir}_{int(time.time())}"  # Use current timestamp to make it unique
    os.makedirs(unique_user_data_dir, exist_ok=True)

    # Specify the user data directory and profile directory
    chrome_options.add_argument(f"user-data-dir={unique_user_data_dir}")  # Path to the user data directory
    chrome_options.add_argument(f"profile-directory={profile_directory}")  # Profile name

    # Path to ChromeDriver (make sure it's in your PATH or provide full path)
    service = Service("/usr/local/bin/chromedriver")

    # Create the Chrome driver with the specified options
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    return driver


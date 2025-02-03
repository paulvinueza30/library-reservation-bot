import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def get_driver():
    # Set up Chrome options
    options = Options()
    options.binary_location = "/usr/bin/google-chrome"  # Path to your Chrome binary
    
    options.add_argument("--headless")
    options.add_argument("--profile-directory=Profile 2")  # You can specify Profile 1, Profile 2, etc.

    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")  # Disables GPU acceleration
    options.add_argument("--disable-software-rasterizer")  # Disables software rendering
    options.add_argument("--start-maximized")  # Optional: Start browser maximized
    options.add_argument("--disable-extensions")  # Disable unnecessary extensions

    # Path to the uploaded Chrome profile on EC2 (ensure this is where you extracted it)
    options.add_argument("user-data-dir=/home/ubuntu/bot-profile")  # Path to your extracted Chrome profile

    # Path to ChromeDriver (make sure it's in your PATH or provide full path)
    service = Service("/usr/local/bin/chromedriver")

    # Create the Chrome driver with the specified options
    driver = webdriver.Chrome(service=service, options=options)
    
    return driver

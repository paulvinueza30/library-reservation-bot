from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from config.preferences import Preferences

def get_driver():
    options = Options()
    options.binary_location = "/usr/bin/firefox"
    options.headless = True
    options.log.level = "trace"
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")  # Disables GPU acceleration
    options.add_argument("--disable-software-rasterizer")  # Disables software rendering
    options.add_argument("--start-maximized")  # Optional: Start browser maximized (not in headless mode)
    options.add_argument("--disable-extensions")  # Disable unnecessary extensions

    # Path to the Firefox profile you want to use
    profile_path = Preferences().get_profiile_path()
    
    # Set Firefox profile
    profile = FirefoxProfile(profile_path)
    options.profile = profile

    # Path to the geckodriver
    service = Service("/usr/local/bin/geckodriver")

    # Create the Firefox driver with the specified options and profile
    driver = webdriver.Firefox(service=service, options=options, timeout = 240)
    return driver

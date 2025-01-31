from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

def get_driver():
    options = Options()
    options.binary_location = "/usr/bin/firefox"
    options.headless = True
    options.log.level = "trace"

    service = Service("/usr/local/bin/geckodriver")
    driver = webdriver.Firefox(service=service, options=options)

    return driver

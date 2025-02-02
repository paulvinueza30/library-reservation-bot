Library Reservation Bot
Overview
This Library Reservation Bot is a Python-based automation script that interacts with the library reservation system. It uses Selenium WebDriver with a Firefox profile to reserve a time slot for the user. The bot automates the process of logging in (via cookies saved in a Firefox profile), selecting a time slot, and submitting the reservation details.

Key Features:
Automated Reservation: Select a specific time slot for library reservations.
Customizable Preferences: Set your desired start and end times, public name, UCF ID, and category values.
Firefox Profile Integration: Use your custom Firefox profile to avoid logging in every time by saving session cookies.
Prerequisites
Python 3.9+: Ensure you have Python 3.9 or later installed.
Selenium: Required for automating browser actions.
Geckodriver: Needed to interact with Firefox via Selenium.
Firefox: Required as the browser for this bot.
Install Dependencies:
Make sure to install the necessary libraries by running:

bash
Copy
pip install selenium python-dotenv
Additionally, you'll need to download Geckodriver and ensure it is in the correct directory. You can download it from here.


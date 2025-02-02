# Library Reservation Bot

This project automates the process of reserving library time slots using Selenium WebDriver and a custom Firefox profile. The bot interacts with the library's website, fills in reservation details, and submits the reservation form.

## Table of Contents

1. [Introduction](#introduction)
2. [Prerequisites](#prerequisites)
3. [Setup Instructions](#setup-instructions)
   - [Clone the Repository](#clone-the-repository)
   - [Install Dependencies](#install-dependencies)
4. [Configuring the `.env` File](#configuring-the-env-file)
5. [Running the Bot](#running-the-bot)
6. [Troubleshooting](#troubleshooting)

---

## Introduction

This bot is designed to automatically reserve time slots at the library by using your **UCF ID** and **public name**. It handles login sessions using a **Firefox profile** with stored cookies, so you don't have to log in every time.

The bot is built with **Selenium** for automation and **Firefox** as the browser, with the ability to load a custom profile that is already logged in.

---

## Prerequisites

Before setting up the bot, ensure the following are installed and properly configured on your machine:

1. **Python 3.9+**
    - The bot is built with Python 3.9 or later. You can install it from the [official Python website](https://www.python.org/downloads/).
  
2. **Selenium**
    - The bot uses Selenium to automate interactions with the browser. You can install it via pip:
    
    ```bash
    pip install selenium
    ```

3. **Geckodriver**
    - Geckodriver is required for Selenium to control Firefox. Download it from [Geckodriver releases](https://github.com/mozilla/geckodriver/releases) and place it in a directory of your choice, making sure it is added to your **PATH** or is located at a known location (e.g., `/usr/local/bin/geckodriver`).

4. **Firefox**
    - Ensure you have **Firefox** installed. This bot requires Firefox and a specific Firefox profile that is already logged into the relevant website.

---

## Setup Instructions

### Clone the Repository

If you haven't done so already, clone the repository to your local machine:

```bash
git clone <repository_url>
cd <repository_folder>
```

### Install Dependencies

Install the required Python dependencies:

```bash
pip install -r requirements.txt
```

This will install **Selenium** and **python-dotenv**, which are needed to interact with the browser and manage environment variables.

---

## Configuring the `.env` File

The bot relies on several environment variables that are stored in the `.env` file. You'll need to create and configure this file to match your own settings.

1. **Create the `.env` file**:
    - In the root directory of your project, create a new file named `.env`.

2. **Configure the `.env` file**:
    - Below is a template for the `.env` file. Fill in your own values where necessary.

    ```dotenv
    # Category Value represents the category of the reservation
    CATEGORY_VALUE=2  # 0: Any, 1: 1-2 people, 2: 3 or more

    # Start Time for the reservation (in 24-hour format)
    START_TIME=13  # 13.0 for 1:00 PM, 13.5 for 1:30 PM, etc.

    # End Time for the reservation (in 24-hour format, can use decimals for half hours)
    END_TIME=15.5  # 15.5 represents 3:30 PM

    # Path to the Firefox profile used for the Selenium WebDriver
    PROFILE_PATH="/Users/your_user/Library/Application Support/Firefox/Profiles/your_profile_name"
    # This profile contains the necessary cookies and login information to bypass login

    # Public Name for the reservation form
    PUBLIC_NAME="Your Full Name"
    # This will be the name displayed for the reservation

    # UCF ID for the reservation form
    UCF_ID=1234567  # The UCF ID for the user making the reservation
    ```

3. **How to Obtain Your Firefox Profile Path**:
    - Open Firefox and sign in to your account.
    - Go to `about:profiles` in the address bar.
    - Find the **Profile Folder** for the profile you want to use.
    - Click **Open Folder** next to your active profile.
    - Copy the folder path and paste it into the `PROFILE_PATH` variable in your `.env` file.

---

## Running the Bot

Once you have completed the setup and configured the `.env` file, you can run the bot using the following command:

```bash
python3 main.py
```

This will start the bot, which will attempt to find available time slots for the given **category**, **start time**, and **end time**. The bot will automatically interact with the website, select the time block, and complete the reservation.

---

## Troubleshooting

### Common Issues:

1. **Firefox Profile Not Found**:
    - Make sure the `PROFILE_PATH` in the `.env` file points to the correct Firefox profile that contains your login session and cookies.
    - You can check your profile location by visiting `about:profiles` in Firefox.

2. **Geckodriver Not Found**:
    - Ensure that **Geckodriver** is installed and available in your system's PATH. You can check by running `geckodriver --version` in your terminal.
    - If it's not installed, download it from the [Geckodriver releases](https://github.com/mozilla/geckodriver/releases).

3. **Selenium Timeout Errors**:
    - If the bot fails to find or interact with elements, try increasing the `WebDriverWait` timeout duration in the code.
    - Ensure that the IDs or class names in the code match those on the website, as the web page may have changed.

4. **Firefox Profile Not Using Cookies**:
    - Ensure your Firefox profile is active and logged in to the library website. The bot uses this session to avoid logging in each time.

---

## Conclusion

You should now have everything set up to use the **Library Reservation Bot**. This bot will automate the process of reserving a time slot at the library by filling out forms and interacting with the website.

If you encounter any issues, feel free to contact the repository owner or raise an issue in the repository.

---

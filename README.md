# Selenium Project: Automating Web Page Interactions  

## Project Overview  
This project demonstrates how to use Selenium WebDriver to automate fundamental web page interactions such as opening pages, maximizing windows, verifying URLs, and closing browsers. The goal is to familiarize QA engineers with essential Selenium methods to streamline functional testing.

---

# Selenium Project: Automating Web Form Testing  

## Project Overview  
This project demonstrates the use of **Selenium WebDriver** to automate the testing of web forms. Instead of manually testing registration forms by creating multiple accounts, Selenium provides an efficient, accurate, and repeatable way to perform the same tasks programmatically.

---

## Features of Selenium WebDriver  

### Actions Selenium Can Automate:  
- **Form Interactions**: Fill out input fields, select options, and submit forms.  
- **Element Actions**: Click buttons, checkboxes, radio buttons, and dropdown menus.  
- **Navigation**: Open URLs, refresh pages, and navigate between pages.  
- **Scrolling**: Scroll up, down, or to specific elements on a page.  

### Example Use Case: Testing a Registration Form  
Suppose you need to test a form with fields for "Name," "Last Name," "Password," and "Confirm Password." The fields must only accept Latin characters, numbers, and special symbols. Example test data:

| **Name**   | **Last Name**      | **Password**  | **Confirm Password** |  
|------------|--------------------|---------------|-----------------------|  
| qwerty     | ytrewq             | password      | password             |  
| Arnold     | Schwarzenegger     | IllBeBack     | IllBeBack            |  
| $3^&       | Op463%#            | B45g+1U       | B45g+1U              |  

### Automating This Test Case with Selenium  
Instead of manually creating accounts and verifying field acceptance, Selenium can:  
1. Open the registration form.  
2. Fill in the fields with predefined test data.  
3. Validate form behavior for each dataset.  

---

## Limitations of Selenium WebDriver  

Selenium cannot automate:  
- Two-factor authentication (2FA), as it requires a separate device or email for one-time codes.  
- CAPTCHA testing.  
- File download progress tracking.  
- Access to restricted sites like Gmail (due to terms of service limitations).

---

## Example Code: Automating a Registration Form  
```python
from selenium import webdriver

# Create WebDriver instance
driver = webdriver.Chrome()

# Open the registration page
driver.get("https://example.com/register")

# Fill out the form
driver.find_element_by_name("name").send_keys("Arnold")
driver.find_element_by_name("last_name").send_keys("Schwarzenegger")
driver.find_element_by_name("password").send_keys("IllBeBack")
driver.find_element_by_name("confirm_password").send_keys("IllBeBack")

# Submit the form
driver.find_element_by_name("submit").click()

# Validate successful submission
assert "Welcome, Arnold!" in driver.page_source

# Close the browser
driver.quit()

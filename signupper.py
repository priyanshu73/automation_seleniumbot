from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import random
import string

from webdriver_manager.chrome import ChromeDriverManager

num_range = int(input("Enter the number of accs: "))

for i in range(num_range):  
        
    email= ''.join((random.choices(string.ascii_lowercase + string.digits, k=8))) +"@gmail.com"    
                                            
    # Set up the WebDriver (Chrome)
    options = Options()
    options.add_argument("--incognito")
    driver = webdriver.Chrome(options=options)

    # Open the website
    driver.get('https://open.spotify.com/?')

    

# Click the cookie consent button
    
    
    wait = WebDriverWait(driver, 30)
    sign_up_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.Button-sc-1dqy6lx-0.eqSwxl.sibxBMlr_oxWTfBrEz2G')))
    sign_up_button.click()

       
    # Wait for the registration form to appear
    email_field = wait.until(EC.presence_of_element_located((By.ID, 'email')))
    password_field = driver.find_element(By.ID, 'password')
    username_field = driver.find_element(By.ID, 'displayname')
    dob_month_field = driver.find_element(By.ID, 'month')
    dob_day_field = driver.find_element(By.ID, 'day')
    dob_year_field = driver.find_element(By.ID, 'year')

    # Fill in the registration form fields
    email_field.send_keys(email)
    password_field.send_keys('nepal123')
    username_field.send_keys('you')
    
    dob_month_field.send_keys('June')
    dob_day_field.send_keys('19')
    dob_year_field.send_keys('1990')
    

    gender_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'Indicator-sc-hjfusp-0')))
    driver.execute_script("arguments[0].scrollIntoView();", gender_button)  # Scroll to the element
    gender_button.click()

       # Find all checkboxes with the indicator class
    checkboxes = driver.find_elements(By.CSS_SELECTOR, 'span.Indicator-sc-1airx73-0.jrJQVH')

    # Scroll to each checkbox and click to select it
    for checkbox in checkboxes:
        driver.execute_script("arguments[0].scrollIntoView();", checkbox)
        checkbox.click()

    # Submit the registration form
    signup_button = driver.find_element(By.CSS_SELECTOR, 'span.ButtonInner-sc-14ud5tc-0.dqLIWu.encore-bright-accent-set.SignupButton___StyledButtonPrimary-cjcq5h-1.jazsmO')
    signup_button.click()

    # Wait for successful registration or handle any additional steps
    #profile_button = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'svelte-13ynk3t')))

    # Store login credentials in a text file
    with open('credentials.txt', 'a') as file:
       
        file.write(f'{email}\n')
     # Log out
    #logout_button = driver.find_element(By.CSS_SELECTOR, 'a.mh-subtle.svelte-11h1c9')
    #logout_button.click()
    WebDriverWait(driver, 10).until(EC.url_changes(driver.current_url))
    time.sleep(5)
    # Close the browser and quit the WebDriver
    driver.quit()


from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException

# Create a file named credentials.txt or anything, and add your email to it. You can add multiple accounts also
with open('credentials.txt', 'r') as file:
    lines = file.readlines()

for line in lines:
    options = Options()
    options.add_argument("--incognito")
    driver = webdriver.Chrome(options=options)
    email = line.strip()
    driver.get('https://www.spotify.com/us/account/overview/')
    wait = WebDriverWait(driver, 30)

    # Wait for and click the "Log in" button
    #button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Log in')]")))
    #button.click()

    # Wait for the email/username input field and enter the value
    email_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input#login-username")))
    email_field.send_keys(email)

    # Wait for the password input field and enter the value 
    password_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input#login-password")))
   #change the pass
    password_field.send_keys("nepal123")

    # Wait for the "Don't remember me" checkbox and click it
    donotrem = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".Indicator-sc-acu4qz-0.GuRdu")))
    donotrem.click()

    # Wait for a certain duration (e.g., 10 seconds)


    log_in = driver.find_element(By.XPATH, '//span[text()="Log In"]')
    
    log_in.click()
    
    #if "login" in driver.current_url:
     #   log_in.click()
    

    
    edit_profile_button = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((By.XPATH, '//a[contains(@href, "/account/profile/") and contains(@class, "Button-sc")]'))
    )
    driver.execute_script("arguments[0].scrollIntoView();", edit_profile_button)
# Click the "Edit profile" button
    edit_profile_button.click()
    
    time.sleep(5)
    # Find and click the select dropdown
    select_dropdown = driver.find_element(By.XPATH, '//select[@id="country" and contains(@class, "Select-sc")]')
    driver.execute_script("arguments[0].scrollIntoView();", select_dropdown)
    select_dropdown.click()

# Find and click the "Brazil" option or any country: change the @value & text()
    time.sleep(3)
    norway_option = driver.find_element(By.XPATH,'//option[@value="BR" and text()="Brazil"]')
    driver.execute_script("arguments[0].scrollIntoView();", norway_option)
    norway_option.click()

# Wait for a brief moment
    time.sleep(3)

# Perform the save profile action using JavaScript scroll
    save_profile_button = driver.find_element(By.XPATH,'//span[@class="ButtonInner-sc-14ud5tc-0 bhKQRg encore-bright-accent-set" and text()="Save profile"]')
    driver.execute_script("arguments[0].scrollIntoView();", save_profile_button)
    save_profile_button.click()
    time.sleep(5)
  # Adjust the timeout as needed
    driver.quit()
    
# Close the WebDriver


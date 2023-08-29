import pytest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture

def driver():
    driver = webdriver.Edge()  
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def test_google_login(driver):
    try:
        driver.get("https://auth.myviewboard.com/oidc/v1/auth/identifier?response_type=code&client_id=mvb-core-service&state=dnJ-djRsdEJVc2R-M2ZOMldQc0RRNWtCbjFoc1phUWw0RktQaFcucTIzQmtQ&redirect_uri=https%3A%2F%2Fmyviewboard.com%2Fhome&scope=openid%20profile%20email&code_challenge=eo6Pj8bi64PC1YPXXtF0ElF-_bALdkaMV7VZwc5Sh5U&code_challenge_method=S256&nonce=dnJ-djRsdEJVc2R-M2ZOMldQc0RRNWtCbjFoc1phUWw0RktQaFcucTIzQmtQ")
    
        google_login_button = driver.find_element(By.ID,"google")
        google_login_button.click()

    except NoSuchElementException as e:
        pytest.fail("Google login button not found")
  
def test_existing_account_login(driver):
    try:
        driver.get("https://auth.myviewboard.com/oidc/v1/auth/identifier?response_type=code&client_id=mvb-core-service&state=dnJ-djRsdEJVc2R-M2ZOMldQc0RRNWtCbjFoc1phUWw0RktQaFcucTIzQmtQ&redirect_uri=https%3A%2F%2Fmyviewboard.com%2Fhome&scope=openid%20profile%20email&code_challenge=eo6Pj8bi64PC1YPXXtF0ElF-_bALdkaMV7VZwc5Sh5U&code_challenge_method=S256&nonce=dnJ-djRsdEJVc2R-M2ZOMldQc0RRNWtCbjFoc1phUWw0RktQaFcucTIzQmtQ")
        
        
        email_input = driver.find_element(By.XPATH,"//*[@id='c_main']/input[1]")
        login_button1 = driver.find_element(By.XPATH,"//*[@id='c_main']/button[1]")
       
        email_input.send_keys("wei8801013@yahoo.com.tw")
        login_button1.click()
        
        password_input = driver.find_element(By.XPATH,"//*[@id='c_main']/input[2]")
        login_button2 = driver.find_element(By.XPATH,"//*[@id='c_main']/button[3]")

        password_input.send_keys("Qwert135!")
        login_button2.click()
    except (NoSuchElementException, TimeoutException) as e:
        pytest.fail("Element not found or timeout")

    

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

def create_driver(user_agent, proxy_ip):
    # Configure Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run headless Chrome
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument(f'user-agent={user_agent}')
    
    if proxy_ip:
        chrome_options.add_argument(f'--proxy-server={proxy_ip}')
    
    # Create WebDriver
    driver = webdriver.Chrome(options=chrome_options)
    return driver

def login_to_venmo(email, password, user_agent, proxy_ip):
    driver = create_driver(user_agent, proxy_ip)
    driver.get('https://venmo.com/login')
    
    time.sleep(3)  # Wait for the page to load
    
    # Enter email
    email_input = driver.find_element(By.NAME, 'email')
    email_input.send_keys(email)
    
    # Enter password
    password_input = driver.find_element(By.NAME, 'password')
    password_input.send_keys(password)
    
    # Submit the form
    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    login_button.click()

    # Wait for login to complete and check for success
    time.sleep(5)
    if "home" in driver.current_url:
        print("Login successful")
    else:
        print("Login failed")
    
    driver.quit()

if __name__ == "__main__":
    email = "ritapaulus@live.com"
    password = "Xavage143**"
    user_agent = "Mozilla/5.0 (iPhone; CPU iPhone OS 16_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5 Mobile/15E148 Safari/604.1"
    proxy_ip = "http://174.210.2.88:8080"  # Replace with your proxy IP or leave empty for no proxy
    
    login_to_venmo(email, password, user_agent, proxy_ip)

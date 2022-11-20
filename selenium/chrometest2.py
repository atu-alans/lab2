from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://eezimotorcycles.herokuapp.com/")
driver.maximize_window()


print(driver.title)
print(driver.current_url)
driver.close()


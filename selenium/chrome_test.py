from selenium import webdriver
driver = webdriver.Chrome(executable_path='../drivers/chromedriver.exe')



#Opens URL an maximize window
driver.get("https://eezimotorcycles.herokuapp.com/")
driver.maximize_window()
print(driver.title)
print(driver.current_url)
driver.close()
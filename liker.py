from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException        

options = webdriver.ChromeOptions() 
options.add_argument(r"user-data-dir=C:\Users\faith\AppData\Local\Google\Chrome\User Data")
driver = webdriver.Chrome(chrome_options=options)
# also make ne to automativally bump boards


driver.get("https://www.instagram.com/")
driver.implicitly_wait(20)  # waits to load

for x in range(0, 4): # I just put that it should scroll 5 times before stopping, you can change tho
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") #scrolls
    driver.implicitly_wait(3) # waits to load (I could optimize this but whatever
    likes = driver.find_elements(By.CLASS_NAME, 'fr66n') #list of like button elements
    for i in likes: #clicks through like buttons
        try:
            i.click()
            print('liked')
            driver.implicitly_wait(3) #waits a little so ig doesnt think anything is fishy
        except:
            print('button was not liked') #this is just incase the button was unable to like 

print('done')


driver.implicitly_wait(20)

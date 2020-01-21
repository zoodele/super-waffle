from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException        



options = webdriver.ChromeOptions() 
options.add_argument(r"user-data-dir=C:\Users\faith\AppData\Local\Google\Chrome\User Data")
# put the path to your chrome file here to avoid logging in


driver = webdriver.Chrome(chrome_options=options)


driver.get("https://bumble.com/app")
driver.implicitly_wait(15)  # waits to load

while driver.current_url == "https://bumble.com/app":
    nameAge = driver.find_element_by_class_name('encounters-story-profile__name')
    natxt = nameAge.text
    firstnam, sep, age = natxt.partition(', ')
    dislike_butt = driver.find_element(By.XPATH, '//*[@id="main"]/div/div[1]/main/div[2]/div/div/span/div[2]/div/div[2]/div/div[1]/div')
    like_butt = driver.find_element(By.XPATH, '//*[@id="main"]/div/div[1]/main/div[2]/div/div/span/div[2]/div/div[2]/div/div[3]/div')
    driver.implicitly_wait(4)
    if firstnam == "Kyle" or firstnam == "Kevin":
        dislike_butt.click()
        # left swipe
        # yes i'm left swiping all guys named kyle or kevin might add all J names next
    else:
        like_butt.click() # right swipe
        try:
             pickupline = driver.find_element(By.XPATH, '//*[@id="main"]/div/div[1]/main/div[2]/article/div/footer/div/div[1]/div/div/div[1]/div/input')
             pickupline.send_keys("Merry Christmas!")  # put your message here
             pickupline.send_keys(Keys.ENTER)
        except:
            print("he didnt like you lol")
    # loop back
    # driver.close()

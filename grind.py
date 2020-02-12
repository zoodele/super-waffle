from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException


options = webdriver.ChromeOptions() 
options.add_argument(r"user-data-dir=C:\Users\faith\AppData\Local\Google\Chrome\User Data")
# options.set_headless(headless=True)

# put the path to your chrome file here to avoid logging in
# set_headless(headless=True) options.headless = True
# cd documents\old shit\bot\
driver = webdriver.Chrome(chrome_options=options)

driver.get("https://tinder.com/app/recs")
driver.implicitly_wait(35)  # waits to load

bg = driver.find_element_by_tag_name('body')

while driver.current_url == "https://tinder.com/app/recs":
    driver.implicitly_wait(4)
    try:
        nameObj = driver.find_element(By.XPATH, '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[1]/div[3]/div[6]/div/div[1]/div/div/span')
    except:
        nameObj = driver.find_element_by_class_name("Fxs($flx1) Flw(w) Fz($xl) Fw($bold) Pend(8px)")
        print('name not found')
    firstnam = nameObj.text
    if firstnam == "Kyle" or firstnam == "Kevin":
        bg.send_keys(Keys.LEFT)
        # yes i'm left swiping all guys named kyle or kevin might add all J names next
    else:
        # like_butt.click() # right swipe
        bg.send_keys(Keys.RIGHT)
        driver.implicitly_wait(4)
        try:
            driver.implicitly_wait(10)
            print('match')
            # pickupline = find_element_by_class_name('itsAMatch D(f) Fld(c) CenterAlign Expand Ta(c) Pos(r) C(#fff) Bdrs(4px) Ov(h)')
            # pickupline = driver.findElement(By.xpath("//textarea[@placeholder='Say something nice!']"))
            pickupline = driver.find_element_by_class_name("sendMessageForm__input P(8px) Flx($flx1) As(c) Fz($s) Rsz(n)")
            # I am conducting a field test of how many woman have pierced nipples.
            # Do you wash your panties with Windex? Because I can really see myself in them.
            msg = firstnam + " you pass the vibe check"  # put your message here
            pickupline.click
            pickupline.send_keys(msg)
            pickupline.send_keys(Keys.TAB)
            pickupline.send_keys(Keys.ENTER)
            # cont = driver.find_element(By.XPATH, "//*[text()='Keep Swiping']")
            # cont.click
        except:
            print("he didnt like you lol")
    # loop back
    # driver.close()
    # now wait tilll it has no more people and end loop
    # to check if loop closes assign variable at beginning and at end try catch if variable is created
    # go through new matches and message
    # go through  messages and message based on ai

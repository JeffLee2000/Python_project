from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request

# Connection error sol
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options)

# Searching
driver.get("https://www.google.co.kr/imghp?hl=ko&ogbl")
elem = driver.find_element_by_name("q")
elem.send_keys("조코딩")
elem.send_keys(Keys.RETURN)

# Scrolling
SCROLL_PAUSE_TIME = 1

## Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    ## Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    ## Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    ## Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        try:
            driver.find_element_by_css_selector(".mye4qd").click()
        except:
            break
    last_height = new_height

# downLoad img
count = 1
images = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")
for image in images:
    try:
        image.click()
        time.sleep(2)
        imgUrl = driver.find_element_by_xpath("/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div/div/div/div[3]/div[2]/c-wiz/div[2]/div[1]/div[1]/div[2]/div/a/img").get_attribute("src")
        urllib.request.urlretrieve(imgUrl, "test" + str(count) + ".jpg")
        count = count + 1
    except:
        pass

driver.close()
from selenium import webdriver
import time

username=""
password=""

driver = webdriver.Chrome()

driver.get("https://www.twitter.com")

login = driver.find_element_by_link_text("Log In")
login.click()

usernameField=element=driver.find_element_by_css_selector("div#page-container > div > div > form > fieldset > div > input")
usernameField.send_keys(username)

passwordField=driver.find_element_by_css_selector("div#page-container > div > div > form > fieldset > div:nth-of-type(2) > input")
passwordField.send_keys(password)

login=driver.find_element_by_tag_name("button")
login.click()

driver.get("https://www.twitter.com/{uname}/likes".format(uname=username))

# likesPage=driver.find_element_by_xpath("/html/body/div/div/div/div/main/div/div/div/div/div/div[2]/div/div/nav/div[2]/div[4]/a")
# likesPage.click()

for j in range(1,10):
    # likesPage=driver.find_element_by_xpath("/html/body/div/div/div/div/main/div/div/div/div/div/div[2]/div/div/nav/div[2]/div[4]/a")
    # likesPage.click()
    driver.get("https://www.twitter.com/{uname}/likes".format(uname=username))
    time.sleep(5)
    for i in range(1,10):
        try:
            k=3
            path="/html/body/div/div/div/div/main/div/div/div/div/div/div[2]/div/div/div[2]/section/div/div/div/div[{pos}]/div/article/div/div[2]/div[2]/div[{sec}]/div[3]/div/div/div[1]".format(pos=i,sec=k)
            print("1-"+path)
            like1=driver.find_element_by_xpath(path)
            like1.click()
            time.sleep(2)
            print("Trying first - "+(j*10+i))
        except Exception:
            print("Caught exception")
            time.sleep(1)
        try:    
            k=4
            path="/html/body/div/div/div/div/main/div/div/div/div/div/div[2]/div/div/div[2]/section/div/div/div/div[{pos}]/div/article/div/div[2]/div[2]/div[{sec}]/div[3]/div/div/div[1]".format(pos=i,sec=k)
            print("2-"+path)
            like2=driver.find_element_by_xpath(path)
            like2.click()
            print("Trying second - " +(j*10+i))
            time.sleep(2)
        except Exception:
            print("Caught exception 2")
            time.sleep(1)

# "/html/body/div/div/div/div/main/div/div/div/div/div/div[2]/div/div/div[2]/section/div/div/div/div[1]/div/article/div/div[2]/div[2]/div[3]/div[3]/div/div/div[1]"
# "/html/body/div/div/div/div/main/div/div/div/div/div/div[2]/div/div/div[2]/section/div/div/div/div[2]/div/article/div/div[2]/div[2]/div[4]/div[3]/div/div/div[1]"
# /html/body/div/div/div/div/main/div/div/div/div/div/div[2]/div/div/div[2]/section/div/div/div/div[3]/div/article/div/div[2]/div[2]/div[3]/div[3]/div/div/div[1]
# /html/body/div/div/div/div/main/div/div/div/div/div/div[2]/div/div/div[2]/section/div/div/div/div[4]/div/article/div/div[2]/div[2]/div[3]/div[3]/div/div/div[1]


time.sleep(10)
driver.close()
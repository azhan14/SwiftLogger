# Modules to be imported.
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def google(email,password):
    e = email
    p = password
    driver = webdriver.Chrome()
    driver.get("http://www.gmail.com")
    time.sleep(2)
    username=driver.find_element_by_xpath("//*[@id='identifierId']")
    username.send_keys(e)
    time.sleep(2)
    next =driver.find_element_by_xpath("//*[@id='identifierNext']/span/span")
    next.click()
    time.sleep(2)
    password=driver.find_element_by_xpath("//*[@id='password']/div[1]/div/div[1]/input")
    password.send_keys(p)
    time.sleep(2)
    login=driver.find_element_by_xpath("//*[@id='passwordNext']/span/span")
    login.click()
    time.sleep(3)
    return()
 
def yahoo(email,password):
    driver = webdriver.Chrome()
    driver.get("https://login.yahoo.com/?.src=ym&.lang=en-IN&.intl=in&.done=https%3A%2F%2Fmail.yahoo.com%2Fd")
    time.sleep(2)
    e = email
    p = password
    username=driver.find_element_by_xpath("//*[@id='login-username']")
    username.send_keys(e)
    time.sleep(2)
    nextbtn = driver.find_element_by_xpath("//*[@id='login-signin']")
    nextbtn.click()
    time.sleep(3)
    password=driver.find_element_by_xpath("//*[@id='login-passwd']")
    password.send_keys(p)
    time.sleep(2)
    loginbtn =driver.find_element_by_id("login-signin")
    loginbtn.click()
    time.sleep(3)
    return()

def studyL(email,password):
    e = email
    p = password
    driver = webdriver.Chrome()
    driver.get("http://www.studyleagueit.com/cpanel")
    time.sleep(2)
    username=driver.find_element_by_xpath("//*[@id='user']")
    username.send_keys(e)
    time.sleep(2)
    password=driver.find_element_by_xpath("//*[@id='pass']")
    password.send_keys(p)
    time.sleep(2)
    login=driver.find_element_by_xpath("//*[@id='login_submit']")
    login.click()
    time.sleep(5)
    return()

def pmart(email,password):
    e = email
    p = password
    driver = webdriver.Chrome()
    driver.get("http://www.pmart.in/index.php")
    time.sleep(2)
    enter=driver.find_element_by_xpath("/html/body/div[1]/span")
    enter.click()
    time.sleep(2)
    login=driver.find_element_by_xpath("/html/body/div[3]/div[1]/div/div/div/ul/li[1]/a/i")
    login.click()
    time.sleep(2)
    username=driver.find_element_by_xpath("/html/body/div[13]/div/div[3]/form/div[1]/input")
    username.send_keys(e)
    time.sleep(2)
    password=driver.find_element_by_xpath("/html/body/div[13]/div/div[3]/form/div[2]/input")
    password.send_keys(p)
    time.sleep(2)
    login1=driver.find_element_by_xpath("/html/body/div[13]/div/div[3]/form/div[3]/input")
    login1.click()
    time.sleep(2)
    return()

def instagram(email,password):
    e = email
    p = password
    driver = webdriver.Chrome()
    driver.get("https://www.instagram.com/accounts/login/?hl=en")
    time.sleep(2)
    username=driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input")
    username.send_keys(e)
    time.sleep(2)
    password=driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input")
    password.send_keys(p)
    time.sleep(2)
    login=driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/article/div/div[1]/div/form/div[4]")
    login.click()
    time.sleep(5)
    return()

def gdrive(email,password):
    e = email
    p = password
    driver = webdriver.Chrome()
    driver.get("http://www.gmail.com")
    time.sleep(2)
    username=driver.find_element_by_xpath("//*[@id='identifierId']")
    username.send_keys(e)
    time.sleep(2)
    next =driver.find_element_by_xpath("//*[@id='identifierNext']/span/span")
    next.click()
    time.sleep(2)
    password=driver.find_element_by_xpath("//*[@id='password']/div[1]/div/div[1]/input")
    password.send_keys(p)
    time.sleep(2)
    login=driver.find_element_by_xpath("//*[@id='passwordNext']/span/span")
    login.click()
    time.sleep(3)
    option=driver.find_element_by_xpath("//*[@id='gbwa']/div")
    option.click()
    time.sleep(3)
    gd=driver.find_element_by_xpath(" //*[@id='gb49']")
    gd.click()
    time.sleep(3)
    return()

def facebook(email,password):
    e = email
    p = password
    driver = webdriver.Chrome()
    driver.get("https://en-gb.facebook.com/login/")
    time.sleep(2)
    username=driver.find_element_by_xpath("//*[@id='email']")
    username.send_keys(e)
    time.sleep(2)
    password=driver.find_element_by_xpath("//*[@id='pass']")
    password.send_keys(p)
    time.sleep(2)
    login=driver.find_element_by_xpath("//*[@id='loginbutton']")
    login.click()
    time.sleep(5)
    return()

def linkedin(email,password):
    e = email
    p = password
    driver = webdriver.Chrome()
    driver.get("https://www.linkedin.com/login")
    time.sleep(2)
    username=driver.find_element_by_xpath("//*[@id='username']")
    username.send_keys(e)
    time.sleep(2)
    password=driver.find_element_by_xpath("//*[@id='password']")
    password.send_keys(p)
    time.sleep(2)
    login=driver.find_element_by_xpath("//*[@id='app__container']/main/div/form/div[3]/button")
    login.click()
    time.sleep(5)
    return()
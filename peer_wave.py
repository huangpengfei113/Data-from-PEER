from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# The list RSNlist gives the RSN number of the ground motion you want to download.
RSNlist = [4101, 4126, 4482, 461, 496]
for i in RSNlist:
    browser = webdriver.Chrome('D:/chromedriver')  # you need install the chromedriver with the right version matching your Chrome explorer, 'D:/chromedriver' is the direction where you install the chromedriver
    browser.get('https://ngawest2.berkeley.edu/')
    browser.find_element_by_xpath('//*[@id="content"]/table[1]/tbody/tr[1]/td[2]/a/img').click()
    for handle in browser.window_handles:
        browser.switch_to.window(handle)
    usernameBox = browser.find_element_by_name('user[email]')
    usernameBox.send_keys('****@tongji.edu.cn')  # where '****@tongji.edu.cn' is the username of the account you registered on PEER
    password = browser.find_element_by_name('user[password]')
    password.send_keys('******')  # '******' is the passwork of your account
    browser.find_element_by_id('user_submit').click()
    browser.find_element_by_xpath('//*[@id="buttons"]/button').click()
    time.sleep(5)
    searchRecordNumber = browser.find_element_by_xpath('//*[@id="search_search_nga_number"]')
    RSN = i
    searchRecordNumber.send_keys('\b\b\b\b')
    searchRecordNumber.send_keys(RSN)
    browser.find_element_by_xpath('//*[@id="new_search"]/div[2]/fieldset/button').click()
    time.sleep(5)
    browser.find_element_by_xpath('//*[@id="middle_submit"]/fieldset[3]/button[2]').click()
    time.sleep(5)
    WebDriverWait(browser, 10).until(EC.alert_is_present())
    alert1 = browser.switch_to.alert
    print(alert1.text)
    alert1.accept()
    WebDriverWait(browser, 10).until(EC.alert_is_present())
    alert2 = browser.switch_to.alert
    print(alert2.text)
    alert2.accept()
    time.sleep(20)
    browser.quit()


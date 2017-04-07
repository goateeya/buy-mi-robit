from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import datetime

def has_page_loaded(driver, elem):
    timeout = 10
    WebDriverWait(driver, timeout).until(EC.presence_of_element_located(elem))
    return driver.find_element(elem[0], elem[1])
    
def refresh(driver):
    driver.refresh();
    return
    
def main():
    fb_username = 'username'
    fb_password = 'password'    
    
    driver.set_page_load_timeout(30)
    driver.get("http://event.mi.com/tw/mff2017")

    # login in
##    btn = driver.find_element_by_xpath("//a[@data-stat-id='5a69116f1d924ff6']")
    btn = driver.find_element_by_xpath("//div[@class='seckill-list']//li[@class='item-2']//div[@class='seckill-text']//a")
    btn.click()

    # choose fb oauth
    elem = (By.CSS_SELECTOR, '.btnadpt.btn_facebook.sns-login-link')
    btn = has_page_loaded(driver, elem)
    btn.click()

    # facebook login
    elem = (By.ID, 'email')
    username = has_page_loaded(driver, elem)
    password = driver.find_element_by_id('pass')
    username.send_keys(fb_username)
    password.send_keys(fb_password)
    password.send_keys(Keys.RETURN)

    # wait to time come & click button
##    elem = (By.XPATH, "//a[@data-stat-id='5a69116f1d924ff6']")
    elem = (By.XPATH, "//div[@class='seckill-list']//li[@class='item-2']//div[@class='seckill-text']//a")
    btn = has_page_loaded(driver, elem)
    target_datetime_str = '2017/4/7 20:00:00'
    target_datetime = datetime.datetime.strptime(target_datetime_str,'%Y/%m/%d %H:%M:%S')
    print('start listening...')
    while True:
        now_datetime = datetime.datetime.now()
        if now_datetime.timestamp() >= target_datetime.timestamp():
            btn.click()
            print('button clicked.')
            break

    # checkout
    elem = (By.ID, 'mi_checkout')
    btn = has_page_loaded(driver, elem)
    btn.click();

    # submit order
    elem = (By.ID, 'checkoutFormBtn')
    btn = has_page_loaded(driver, elem)
    btn.click();
##    driver.close()
    print('program end.')
    return True
    
if __name__ == "__main__":
    # browser driver switcher
    #driver = webdriver.Firefox(executable_path='F:/py/geckodriver.exe') #replace where driver located
    driver = webdriver.Chrome('D:/py/chromedriver')
    while(True):
        try:
            if main() == True:
                break
        except TimeoutException  as e:
            print('web timeout')
        except Exception as e:
            #refresh(driver);
            print(str(e))
            break

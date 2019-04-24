import pickle

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def send_alert( msg ):
    options = webdriver.ChromeOptions()
    options.add_argument("user-data-dir=/Users/s0s03br/Documents/chrome")  # Path to your chrome profile

    #path to the webdriver executable file
    driver = webdriver.Chrome(executable_path="/Users/s0s03br/Downloads/chromedriver", options=options)

    driver.get("https://web.whatsapp.com/")

    wait = WebDriverWait(driver, 600)

    # Replace 'Friend's Name' with the name of your friend
    # or the name of a group
    target = '"Swiggy"'

    # Replace the below string with your own message
    string = msg

    x_arg = '//span[contains(@title,' + target + ')]'
    group_title = wait.until(EC.presence_of_element_located((
        By.XPATH, x_arg)))
    group_title.click()

    message = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')[0]

    message.send_keys(string)

    sendbutton = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')[0]
    pickle.dump(driver.get_cookies(), open("cookies.pkl", "wb"))
    sendbutton.click()

    driver.close()




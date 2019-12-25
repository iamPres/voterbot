from selenium import webdriver
import time
import os

browser = webdriver.Chrome(os.path.join(os.getcwd(), 'chromedriver'))
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
while True:
    try:
        browser.get('https://www.shreveporttimes.com/story/sports/2019/12/22/11-nw-la-prep-athletes-16th-times-athlete-week-ballot/2706550001/?utm_source=AMP&utm_medium=UpNext')
        browser.implicitly_wait(1)
        browser.execute_script("window.scrollTo(0, 1500)")
        browser.implicitly_wait(1)
        print('Voting...')
        button = browser.find_elements_by_xpath("//span[contains(@class, 'css-answer-group')]")[6]
        button.click()
        browser.implicitly_wait(1)
        browser.find_elements_by_xpath("//a[contains(@id, 'pd-vote-button10481327')]")[0].click()
        browser.implicitly_wait(1)
    except Exception as e:
        print(e)
        browser.quit()
        time.sleep(5)
        browser = webdriver.Chrome(os.path.join(os.getcwd(), 'chromedriver'))

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from getpass import getpass

gmailId = input('Enter emailId:')
pwd = input('Enter Password:')
try:
    s = Service('C:/chromedriver.exe')
    url = 'https://accounts.google.com/signin/v2/identifier?continue=' + \
          'https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1' + \
          '&flowName=GlifWebSignIn&flowEntry = ServiceLogin'
    driver = webdriver.Chrome(service=s)
    driver.get(url)
    driver.implicitly_wait(15)
    driver.find_element('//*[@id ="identifierId"]').send_keys(gmailId)
    driver.find_elements('//*[@class ="VfPpkd-RLmnJb"]').click()
    driver.find_elements('//*[@type ="password"]').send_keys(pwd)
    driver.find_elements('//*[@class ="VfPpkd-RLmnJb"]').click()
    driver.implicitly_wait(15)
#Click on compose
    driver.find_elements('//div[contains(text(),"Compose")]').click()
    driver.find_element('//textarea[@id=":18v"]').send_keys(gmailId)
    driver.find_element('//textarea[@id=":19j"]').send_keys("Test Email Content")
    driver.find_elements('//div[@id=":`183"]').click()
    driver.close()

except:
    print('Login Failed')

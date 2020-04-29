import time, sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# input from command
email = sys.argv[1]
subject = sys.argv[2]
message = ' '.join(sys.argv[3:])

# load email client in the browser
browser = webdriver.Firefox()
browser.get('https://accounts.google.com/signin/v2/identifier?service=mail')
emailElem = browser.find_element_by_name('identifier')
emailElem.send_keys('sompodsign@gmail.com')
emailElem.send_keys(Keys.ENTER)
time.sleep(3)
passElem = browser.find_element_by_name('password')
passElem.send_keys('4423445946644S')
passElem.send_keys(Keys.ENTER)
time.sleep(5)

# Compose Element
composeElem = browser.find_element_by_class_name('z0')
composeElem.click()
time.sleep(5)

# Recepient
rpEmail = browser.find_element_by_name('to')
rpEmail.send_keys(email)

# subject
subjectElem = browser.find_element_by_name('subjectbox')
subjectElem.send_keys(subject)

# Message
subjectElem.send_keys(Keys.TAB + message + Keys.TAB + Keys.ENTER)
time.sleep(5)


browser.quit()





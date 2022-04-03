import pandas as pd
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser=webdriver.Chrome("chromedriver.exe")
browser.get("https://www.linkedin.com")

username=browser.find_element_by_id("session_key")
username.send_keys("laskshi032017@gmail.com")
password=browser.find_element_by_id("session_password")
password.send_keys("divya0309")



login_button=browser.find_element_by_class_name("sign-in-form__submit-button")
login_button.click()

browser.get("https://www.linkedin.com/jobs/")

time.sleep(4)
job=browser.find_elements_by_class_name("job-card-list__title")
c=[]
for i in job:
    #print(i.text)
    c.append(i.text)

job_title=[]
for i in range(len(c)):
    job_title.append(c[i].strip("Job Title\n"))
print("----Job Title----")
print(job_title)
print()
print()

job2=browser.find_elements_by_class_name("job-card-container__company-name")
comp_name=[]
for i in job2:
    #print(i.text)
    comp_name.append(i.text)
print("----Company Name----")
print(comp_name)
print()
print()
comp_name.append(" ")
comp_name.append(" ")

len(comp_name)


job3 = browser.find_elements_by_class_name("job-card-container__metadata-item")
loc_name=[]
for i in job3:
    #print(i.text)
    if i.text=='Remote' or i.text=='On-site':
    	pass
    else:
    	loc_name.append(i.text)
print("----Job Location----")
print(loc_name)
print()
print()
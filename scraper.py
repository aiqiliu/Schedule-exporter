#!/usr/bin/env ruby
#scrape class schedule from caesar
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#login to caesar
print("Please type in your netID: ")
netid = raw_input()
print("Please type in your Caesar password")
pwd = raw_input()

chromedriver = "/Users/john/Downloads/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)

driver.get('https://ses.ent.northwestern.edu/psp/s9prod/?cmd=login')
driver.find_element_by_id('userid').send_keys(netid)
driver.find_element_by_id("pwd").send_keys(pwd)

driver.find_element_by_name("Submit").click()

#get to class selection page
driver = driver.get('https://ses.ent.northwestern.edu/psp/caesar_5/EMPLOYEE/HRMS/c/SA_LEARNER_SERVICES.SSR_SSENRL_APPT.GBL?Page=SSR_SSENRL_APPT&Action=A&EMPLID=2870114&TargetFrameName=None')
print(driver)
# driver.find_element_by_name("SSR_DUMMY_RECV1$sels$0").click()
# driver.find_element_by_name("DERIVED_SSS_SCT_SSR_PB_GO").click()

















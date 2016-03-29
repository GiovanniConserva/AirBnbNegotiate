# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
import unittest, time, re
import time
import random
import pandas as pd
import os

class SendOffer(unittest.TestCase):
    def setUp(self):
        #self.driver = webdriver.Firefox()
        chromedriver = "C:\Users\user\Desktop\Harvard\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = chromedriver        
        #path_to_chromedriver = '/Users/yourname/Desktop/chromedriver' # change path as needed        
        self.driver = webdriver.Chrome(chromedriver)
        self.base_url = "https://www.airbnb.it/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def login(self ,user_name, signin_password ):
        self.driver.get(self.base_url + "")
        time.sleep(random.uniform(0.5, 1)+1)
        self.driver.find_element_by_link_text("Accedi").click()
        time.sleep(random.uniform(0.5, 1)+1)
        self.driver.find_element_by_id("signin_email").clear()
        time.sleep(random.uniform(0.5, 1))
        self.driver.find_element_by_id("signin_email").send_keys(user_name)
        time.sleep(random.uniform(0.5, 1))
        self.driver.find_element_by_id("signin_password").clear()
        time.sleep(random.uniform(0.5, 1))
        self.driver.find_element_by_id("signin_password").send_keys(signin_password)
        time.sleep(random.uniform(0.5, 3)+1)
        self.driver.find_element_by_id("user-login-btn").click()


    def test_send_offer(self):
        driver = self.driver 
        bucket = "days2_weeks1"
        user_name = "michelenuzzo1990@outlook.it"
        signin_password = "HardttoInvent16"       
        ids = []
        responses = []
        actions= []
        prices = []
        outputFile= "retrieved/"+ bucket + "_retrieved" + '.json'                

        #for starting at position "starting" in the list
        test = pd.read_json('results/'+bucket+ "_result"+ '.json')
        self.login(user_name,signin_password)
        time.sleep(6)
        driver.get(self.base_url)
        
        #driver.find_element_by_id("user-login-btn").click()
        time.sleep(5)
        driver.get(self.base_url)
        time.sleep(3)
         
        counter=0
        
        for index,row in test.iterrows():
            wait = WebDriverWait(driver, 15)
            if not row['successfuls']:
                continue
            
            driver.get("https://www.airbnb.it/rooms/" + str(row['id']))
            #time.sleep(7)
            print "iteration number: "+ str(counter)
            counter= counter+1
            print "host number: " + "https://www.airbnb.it/rooms/" + str(row['id'])
            #driver.find_element_by_xpath("//button[@class='btn btn-link']").click()
            #wait.until()
            
             
            wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@class='btn-link btn-link--bold']")))
            try:
                driver.find_element_by_xpath("//button[@class='btn-link btn-link--bold']").click()
            except:
                
                time.sleep(2)
                print "second click bold"
                driver.find_element_by_xpath("//button[@class='btn-link btn-link--bold']").click()
            try:
            #time.sleep(7)
                wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"div.contacted-before > a > span")))
            except:
                print "not really contacted"
                continue
            try:  
                driver.find_element_by_css_selector("div.contacted-before > a > span").click()
            except:
                print "second click before"
                time.sleep(2)
                driver.find_element_by_css_selector("div.contacted-before > a > span").click()
            time.sleep(5)        
            html = driver.page_source
            soup = BeautifulSoup(html)
            messages = soup.findAll('span', {"class" : "message-text"})            
            action= soup.findAll('span', {"class": "horizontal-rule-wrapper"})
            ids.append(row['id'])
            if action is not None:               
                actions.append (str(action))
                
            else:
                actions.append("")
            price_found=False
            try:
                nightly_price =  driver.find_element_by_xpath("//span[@data-reactid='.7.3.4.0.0.0.0.$0.0']")
                price_found=True
            except:
                pass
            #                  driver.find_element_by_xpath("//span[@data-reactid='.7.3.4.0.0.0.0.$0.0']")
            if not price_found:
                try:
                    nightly_price =  driver.find_element_by_xpath("//span[@data-reactid='.8.3.4.0.0.0.0.$0.0']")
                    price_found=True
                except:
                    pass
            #print "price " + nightly_price.text
            print nightly_price
            if not price_found:
                print "price not found"
                driver.quit()
            
            prices.append(nightly_price.text)
            res = ""
            
            for msg in messages:
                res = res +  msg.get_text() + " *************** "                         
            
            #print res
            try:
                mes = str(res)
            except:
                mes= ""     
            responses.append(str(mes))
            time.sleep(random.uniform(0.5, 5))
            time.sleep(5)
            res_df = pd.DataFrame({'id': ids, 'responses': responses, 'actions': actions, 'prices': prices})
        #print res_df.values
        #print res_df.columns
        
            res_df.to_json(outputFile)
        print "correctly executed"

        
        
         
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()

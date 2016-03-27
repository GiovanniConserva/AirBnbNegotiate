# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
import time
import random
import pandas as pd
import numpy as np
import pickle
import os
import urllib2
import json
import traceback
import sys




class SendOffer(unittest.TestCase):

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
        
        
    
    
    def setUp(self):
        #self.driver = webdriver.Firefox()
        chromedriver = "C:\Users\user\Desktop\Harvard\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = chromedriver        
        self.driver = webdriver.Chrome(chromedriver)
        #self.driver.implicitly_wait(0)
        self.base_url = "https://www.airbnb.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_send_offer(self):
        driver = self.driver        
        user_name = "michele.piazza@aol.com"
        signin_password = "CrazyPassword123"       
        bucket = "days2_weeks2"
        test = pd.read_json('buckets/'+bucket+ '.json')
        #print test['property_id']
        #test = test.ix[11:] 
        #print test['property_id']
        #sys.exit(0)
        
        count = 0         
        ids= []
        urls= []
        successfuls= []
        reasons= []        
        num_output = ""
        outputFile= "results/" + bucket + "_result" + num_output+ '.json'                
        
        bucket_max=20
        #for starting at position "starting" in the list
        starting = 0
        test = test.ix[starting:]  
        total_succ = 0
        
        #test = test[:2]      
        self.login(user_name,signin_password)
        time.sleep(5)
        driver.get(self.base_url)
        time.sleep(random.uniform(0.5, 2))                
        for index, row in test.iterrows():
            
            count= count+1    
	        
            try:
                
                time.sleep(random.uniform(0.5, 5))
                current_url= "https://www.airbnb.com/rooms/"+ str(row['property_id'])+ "?check_in="+ str(row['start'])+ "&guests="+str(row['bed'])+"&check_out="+str(row['end'])
                driver.get(current_url)            
                time.sleep(random.uniform(0.5, 7)+2)
                
                exit= False
                
                #id updating
                urls.append(current_url)
                ids.append(row['property_id'])
                exit = self.is_element_present(By.XPATH,"//p[contains(.,'These dates are not available')]" )
                exit = exit or self.is_element_present(By.XPATH,"//p[contains(.,'Queste date non sono disponibili')]" )
                if exit:
                    #reason updating
                    reasons.append("These dates are not available") 
                    successfuls.append(False)
                    res_df = pd.DataFrame({'id': ids, 'successfuls': successfuls, 'reasons': reasons})                
                    res_df.to_json(outputFile)                                                        
                    continue                

                exit =  self.is_element_present(By.XPATH,"//p[contains(.,'Minimum stay is')]" )
                exit = exit or self.is_element_present(By.XPATH,"//p[contains(.,'minimo di notti')]" )                
                if exit:
                    #reason updating
                    reasons.append("Minimum stay is")
                    successfuls.append(False)
                    res_df = pd.DataFrame({'id': ids, 'successfuls': successfuls, 'reasons': reasons})                
                    res_df.to_json(outputFile)                                    
                    continue                
                #if self.is_alert_present():
                #    print self.close_alert_and_get_its_text()
                time.sleep(1)
                #OLD SELECTOR
                #driver.find_element_by_css_selector("a > strong > span").click()
                
                #driver.find_element_by_xpath("//button[@class='btn btn-link']").click()
                
                driver.find_element_by_xpath("//button[@class='btn-link btn-link--bold']").click()
                
                time.sleep(random.uniform(0.5, 6)+5)              
                exit = self.is_element_present(By.CLASS_NAME,"contacted-before" )
                
                if exit:
                    exit=driver.find_element(by=By.CLASS_NAME, value="contacted-before").is_displayed()
                if exit:                                        
                    reasons.append("contacted-before")
                    successfuls.append(False) 
                    res_df = pd.DataFrame({'id': ids, 'successfuls': successfuls, 'reasons': reasons})                
                    res_df.to_json(outputFile)                
                    continue
                print "Iteration number " + str(count)

                driver.find_element_by_xpath("//textarea[@name='question']").clear()
               
                time.sleep(random.uniform(0.5, 3)+2)
                driver.find_element_by_xpath("//textarea[@name='question']").send_keys(row['messages'])
                os.system("start batman.wav")
                
                time.sleep(random.uniform(0.5, 6)+5)
                                                
                driver.find_element_by_xpath("(//button[@type='submit'])[4]").click()                                
                time.sleep(random.uniform(0.5, 1)+5)
                time.sleep(3)
                #sound = self.is_element_present(By.XPATH,"//strong[contains(@data-reactid,'modal.0.0.0.0.5.0.0.0')]" )
                
                #if not exit: 
                    #os.system("start C:/Users/user/Anaconda2/Lib/batman.wav")                                       
                    
                    #reasons.append("Blocked by airbnb")
                    #successfuls.append(False) 
                    #res_df = pd.DataFrame({'id': ids, 'successfuls': successfuls, 'reasons': reasons})                
                    #res_df.to_json(outputFile)                
                    #continue
                
                time.sleep(random.uniform(0.5, 7)+2)
                
                successfuls.append(True)
                
                total_succ= total_succ+1   
                print "Successful " + str(total_succ)                                 
                reasons.append("")                                  
                
                res_df = pd.DataFrame({'id': ids, 'urls': urls, 'successfuls': successfuls, 'reasons': reasons})
                res_df.to_json(outputFile)  
                time.sleep(random.uniform(0.5, 15)+35)
                
                if total_succ >= bucket_max:
                    sys.exit(0)              
                
            #except urllib2.URLError as e:
            except Exception as e:
                os.system("start batman.wav")
                print "exception" + str(e.args)
                print "stack " + str(traceback.format_exc())
                if len(reasons) == len(ids):
                    reasons.pop()
                if len(successfuls) == len(ids):
                    successfuls.pop()

                reasons.append(str(str(e.args) + " ******** " + str(traceback.format_exc()))) #e.args
                successfuls.append(False) 
                res_df = pd.DataFrame({'id': ids, 'successfuls': successfuls, 'reasons': reasons})
                res_df.to_json(outputFile)                
                pass
 
 
    
    
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

import sys
#from date import datetime, time
import time
sys.path.append(sys.path[0] + "../..")

from ProjectTest.TScripts.challenge3Script import *
from playwright.sync_api import sync_playwright
from ProjectTest.TestConfig.basicConfig import *

'''
Scenarios to achieve End to end functionalities of Challenge 3 Task.
Exception handling is Not implemented and Logger class is not Implemented.
Reporting Modules is also not Implemented
'''

with sync_playwright() as playwright:

    try:
        playwright = Challange3Test(playwright)
        playwright.launchWebUI()
        playwright.loginUsername(login_user_name)
        playwright.loginPassword(login_passwd)
        playwright.clickLoginSubmitChal3()
        #time.sleep(5)
        welcomemsg = playwright.getWelcomeMsgCha3()
        print(welcomemsg)
        assert welcomemsg == 'Success!'
        ## Assert can be used
        # if welcomemsg == 'Welcome!':
        #     pass
        welcomemsgfull = playwright.getWelcomeMsgFullCha3()
        print(welcomemsgfull)
        assert welcomemsgfull == 'Logged in successfully!'

        loginusernametext = playwright.getLoginNameChal3()
        print(loginusernametext)
        assert loginusernametext == 'Email: '+ login_user_name

        passwordtext = playwright.getPasswdDetailsForChal3()
        print(passwordtext)
        assert passwordtext == 'Password: ' + login_passwd

        playwright.captureScreenPostLoginChall3()
        playwright.clickCloseBtnChal2()
        time.sleep(2)
        playwright.getSuccessStatus()
    except:
        playwright.getFailedStatus()

    playwright.closeBrowser()
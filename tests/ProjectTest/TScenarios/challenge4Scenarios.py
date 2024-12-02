import sys
#from date import datetime, time
import time
sys.path.append(sys.path[0] + "../..")

from ProjectTest.TScripts.challenge4Script import *
from playwright.sync_api import sync_playwright
from ProjectTest.TestConfig.basicConfig import *

'''
Scenarios to achieve End to end functionalities of Challenge 4 Task.
Exception handling is Not implemented and Logger class is not Implemented.
Reporting Modules is also not Implemented
'''
with sync_playwright() as playwright:

    try:
        playwright = Challange4Test(playwright)
        playwright.launchWebUI()
        time.sleep(2)
        playwright.loginUsername(login_user_name)
        playwright.loginPassword(login_passwd)
        time.sleep(2)
        playwright.clickLoginSubmitChal4()
        time.sleep(5)
        # dashboardmsg = playwright.getDashboardMsgCha4()
        # print(dashboardmsg)
        # assert dashboardmsg == 'Dashboard'

        loginusernamedetails = playwright.getLoginUserNameChal4()
        print(loginusernamedetails)
        assert loginusernamedetails == login_user_name

        playwright.clickdropDownBtnChal4()
        time.sleep(2)
        playwright.captureScreenPostLoginChall4()
        playwright.clickSignOutBtnChal4()

        playwright.getSuccessStatus()
    except:
        playwright.getFailedStatus()

    playwright.closeBrowser()
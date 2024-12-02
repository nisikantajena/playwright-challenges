import sys
#from date import datetime, time
import time
sys.path.append(sys.path[0] + "../..")

from ProjectTest.TScripts.challenge2Script import *
from playwright.sync_api import sync_playwright
from ProjectTest.TestConfig.basicConfig import *

'''
Scenarios to achieve End to end functionalities of Challenge 2 Task.
Exception handling is Not implemented and Logger class is not Implemented.
Reporting Modules is also not Implemented
'''
with sync_playwright() as playwright:

    try:
        playwright = Challange2Test(playwright)
        playwright.launchWebUI()
        playwright.loginUsername(login_user_name)
        playwright.loginPassword(login_passwd)
        playwright.clickLoginSubmit()
        welcomemsg = playwright.getWelcomeMsgCha2()
        print(welcomemsg)
        ## Assert can be used
        if welcomemsg == 'Welcome!':
            pass
        #userinfodetails = playwright.getUserInfoMsgCha2()
        #print(userinfodetails)
        playwright.clickAccMenuBtnChal2()
        time.sleep(2)
        playwright.captureScreenPostLoginChall2()
        ## Assert can be used
        profiletext = playwright.getprofileMsgCha2()
        print(profiletext)
        ## Assert can be used
        settingtext = playwright.getSettingsMsgCha2()
        print(settingtext)
        ## Assert can be used
        prefrencetext = playwright.getPreferenceMsgCha2()
        print(prefrencetext)
        playwright.clickLogoutBtnChal2()
        playwright.getSuccessStatus()
    except:
        playwright.getFailedStatus()

    playwright.closeBrowser()
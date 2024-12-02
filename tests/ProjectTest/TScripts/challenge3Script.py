from playwright.sync_api import sync_playwright
import sys
sys.path.append(sys.path[0] + "/..")

from ProjectTest.ElementLocator.commonLocators import *
from ProjectTest.ElementLocator.coreReusabilityLib import *
from ProjectTest.ElementLocator.postLoginInfoDetails import *
from ProjectTest.TestCapabilities.testCap import testCapabilities


select = elementSelector()

capability = testCapabilities()


def set_test_status(page, status, remark):
    page.evaluate("_ => {}",
                  "PlayW Status: {\"action\": \"setTestStatus\", \"arguments\": {\"status\":\"" + status + "\", \"remark\": \"" + remark + "\"}}")

class Challange3Test:
    '''
        Class and method Declaration for the action functionality for Challenge 3 Task.

        Initiate browser and call the required URL for the Action

        Exception handling is Not implemented and Logger class is not Implemented.
        Reporting Modules is also not Implemented
        '''
    def __init__(self, playwright) -> None:
        #self.browser = playwright.chromium.launch(headless=True)
        self.browser = playwright.chromium.launch(headless=False)
        #self.browser = playwright.chromium.connect(capability.Chrome())
        page = self.browser.new_page()
        self.page = page
    def launchWebUI(self):
        self.page.goto(select.challange3Url())
        title = self.page.title()
        print(title)

    def loginUsername(self, data):
        self.page.locator(select.loginUName()).fill(data)

    def loginPassword(self, data):
        self.page.locator(select.loginPwd()).fill(data)

    def clickLoginSubmitChal3(self):
        self.page.locator(select.signinBtnChal3()).click()

    def captureScreenPostLoginChall3(self):
        self.page.screenshot(path="../ScreenProof/postloginChallenge3Screen.png", full_page=True)
        #self.page.locator(select.loginSuccessMsg()).

    def clickLogoutSubmit(self):
        self.page.locator(select.signOutBtn()).click()
        #self.page.locator(select.signOutBtn()).ispresent()

    def clickCloseBtnChal2(self):
        self.page.locator(select.clickCloseBtn()).click()

    def getWelcomeMsgCha3(self):
        text = self.page.locator(select.getWelcomemsgChal3()).inner_text()
        return text
    def getWelcomeMsgFullCha3(self):
        text = self.page.locator(select.getWelcomemsgFullChal3()).inner_text()
        return text
    def getLoginNameChal3(self):
        text = self.page.locator(select.getUserloginNameChal3()).inner_text()
        return text
    def getPasswdDetailsForChal3(self):
        text = self.page.locator(select.getPasswordDetailsChal3()).inner_text()
        return text

    def getSuccessStatus(self):
        return set_test_status(self.page, "passed", "Success")

    def getFailedStatus(self):
        return set_test_status(self.page, "failed", "Test failed")

    def closeBrowser(self):
        self.browser.close()
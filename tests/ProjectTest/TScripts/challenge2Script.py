from playwright.sync_api import sync_playwright
import sys
sys.path.append(sys.path[0] + "/..")

from ProjectTest.ElementLocator.commonLocators import *
from ProjectTest.ElementLocator.coreReusabilityLib import *
from ProjectTest.ElementLocator.postLoginActionDetails import *
from ProjectTest.TestCapabilities.testCap import testCapabilities


select = elementSelector()

capability = testCapabilities()


def set_test_status(page, status, remark):
    page.evaluate("_ => {}",
                  "PlayW Status: {\"action\": \"setTestStatus\", \"arguments\": {\"status\":\"" + status + "\", \"remark\": \"" + remark + "\"}}")

class Challange2Test:
    '''
        Class and method Declaration for the action functionality for Challenge 2 Task.

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
        self.page.goto(select.challange2Url())
        title = self.page.title()
        print(title)

    def loginUsername(self, data):
        self.page.locator(select.loginUName()).fill(data)

    def loginPassword(self, data):
        self.page.locator(select.loginPwd()).fill(data)

    def clickLoginSubmit(self):
        self.page.locator(select.signInBtn()).click()

    def captureScreenPostLoginChall2(self):
        self.page.screenshot(path="../ScreenProof/postloginChallenge2Screen.png", full_page=True)
        #self.page.locator(select.loginSuccessMsg()).

    def clickLogoutSubmit(self):
        self.page.locator(select.signOutBtn()).click()
        #self.page.locator(select.signOutBtn()).ispresent()

    def clickLogoutBtnChal2(self):
        self.page.locator(select.clickLogoutBtnChallange2()).click()

    def clickAccMenuBtnChal2(self):
        self.page.locator(select.clickMyAccountBtn()).click()
    def getWelcomeMsgCha2(self):
        text = self.page.locator(select.getWelcomeMsg()).inner_text()
        return text
    def getUserInfoMsgCha2(self):
        text = self.page.locator(select.getUserMsg()).inner_text()
        return text
    def getprofileMsgCha2(self):
        text = self.page.locator(select.getprofileElement()).inner_text()
        return text
    def getSettingsMsgCha2(self):
        text = self.page.locator(select.getSettingElements()).inner_text()
        return text
    def getPreferenceMsgCha2(self):
        text = self.page.locator(select.getPreferenceElement()).inner_text()
        return text

    def getSuccessStatus(self):
        return set_test_status(self.page, "passed", "Success")

    def getFailedStatus(self):
        return set_test_status(self.page, "failed", "Test failed")

    def closeBrowser(self):
        self.browser.close()
from ProjectTest.ElementLocator.commonLocators import *
from ProjectTest.ElementLocator.dashBoardPage import *
from ProjectTest.ElementLocator.loginPageSuccess import *
from ProjectTest.ElementLocator.postLoginInfoDetails import *
from ProjectTest.ElementLocator.postLoginActionDetails import *

class elementSelector:
    '''
    Access the Xpath or IDs (Locators) of the Web Element from POM

    Selector will be used to access Identifiers at Runtime and Used by Test Scripts
    '''
    def __init__(self) -> None:
        self.chal1Url = commonwebElements["chal1Url"]
        self.chal2Url = commonwebElements["chal2Url"]
        self.chal3Url = commonwebElements["chal3Url"]
        self.chal4Url = commonwebElements["chal4Url"]
        self.loginusername = commonwebElements["loginusername"]
        self.loginpasswd = commonwebElements["loginpasswd"]
        self.signinbtn = commonwebElements["signinbtn"]
        self.signoutbtn = commonwebElements["signoutbtn"]
        self.signinbtnChal3 = commonwebElements["signinbtnChal3"]

        self.loginSuccessMessage = loginSuccessWebElements["loginSuccessMessage"]

        self.welcomeMsg = postloginChal2webElements["welcomeMsg"]
        self.userinfo = postloginChal2webElements["userinfo"]
        self.myAccountBtn = postloginChal2webElements["myAccountBtn"]
        self.profile = postloginChal2webElements["profile"]
        self.settings = postloginChal2webElements["settings"]
        self.preference = postloginChal2webElements["preference"]
        self.logout = postloginChal2webElements["logout"]

        self.welcomeMsgCha3 = postloginChal3webElements["welcomeMsgCha3"]
        self.welcomefullmsgcha3 = postloginChal3webElements["welcomefullmsgcha3"]
        self.userdetailsChal3 = postloginChal3webElements["userdetailsChal3"]
        self.passworddetailsChal3 = postloginChal3webElements["passworddetailsChal3"]
        self.closebtnChal3 = postloginChal3webElements["closebtnChal3"]

        self.BoardPage = dashboardwebElements["BoardPage"]
        self.UserDetails = dashboardwebElements["UserDetails"]
        self.dropdownClick = dashboardwebElements["dropdownClick"]
        self.SignoutbtnDboard = dashboardwebElements["SignoutbtnDboard"]

    def challange1Url(self):
        return self.chal1Url
    def challange2Url(self):
        return self.chal2Url
    def challange3Url(self):
        return self.chal3Url
    def challange4Url(self):
        return self.chal4Url

    def loginUName(self):
        return self.loginusername
    def loginPwd(self):
        return self.loginpasswd
    def signInBtn(self):
        return self.signinbtn
    def signOutBtn(self):
        return self.signoutbtn

    def loginSuccessMsg(self):
        return self.loginSuccessMessage

    def getWelcomeMsg(self):
        return self.welcomeMsg
    def getUserMsg(self):
        return self.userinfo
    def clickMyAccountBtn(self):
        return self.myAccountBtn
    def getprofileElement(self):
        return self.profile
    def getSettingElements(self):
        return self.settings
    def getPreferenceElement(self):
        return self.preference
    def clickLogoutBtnChallange2(self):
        return self.logout

    def signinBtnChal3(self):
        return self.signinbtnChal3
    def getWelcomemsgChal3(self):
        return self.welcomeMsgCha3
    def getWelcomemsgFullChal3(self):
        return self.welcomefullmsgcha3
    def getUserloginNameChal3(self):
        return self.userdetailsChal3
    def getPasswordDetailsChal3(self):
        return self.passworddetailsChal3
    def clickCloseBtn(self):
        return self.closebtnChal3


    def dashBoardPage(self):
        return self.BoardPage
    def dashBoardUserData(self):
        return self.UserDetails
    def dashBoardSignOutBtn(self):
        return self.SignoutbtnDboard
    def dashBoardDropDownClick(self):
        return self.dropdownClick

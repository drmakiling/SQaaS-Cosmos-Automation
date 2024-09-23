from datetime import time
from playwright.sync_api import Page, expect
from utils.wait_helpers import wait_and_click_element, wait_for_element

class VisitsFeaturePage:
    def __init__(self, page):
        self.page = page
        self.Visits_Tab = "//p[contains(text(), 'Visits')]"
        self.Add_A_Visit_Button = "//button[contains(text(), 'Add a visit')]"
        self.Schedule_Code = "(//input[contains(@class, 'MuiSelect')])[1]/parent::*"
        self.Visit_Id = "//input[@name='GeneralSection-visitId']"
        self.Visit_Variant = "(//input[contains(@class, 'MuiSelect')])[2]/parent::*"
        self.Location_Type = "(//input[contains(@class, 'MuiSelect')])[3]/parent::*"
        self.Save_Button = "(//button[contains(text(), 'Save')])[1]"
        self.Close_Button = "//button[contains(text(), 'Close')]"
        self.Cancel_Button = "//button[contains(text(), 'Cancel')]"

        # Information tab in add visit modal
        self.Information_Tab = "//button[@id='Information-1']"
        self.Visit_Title = "//input[@name='InformationSection-visitTitle']"
        self.Visit_Type = "//div[@data-testid='InformationSection-visitType']"
        self.Visit_Purpose = "//textarea[@name='InformationSection-visitPurpose']"
        self.Patient_Description = "//textarea[@name='InformationSection-patientDescription']"
        self.Patient_Pre_Activities_Description = "//textarea[@name='InformationSection-patientPreActivitiesDescription']"
        self.Version = "//input[@name='InformationSection-version']"
        self.Visits_Record = "(//div/div[@data-field='visitId'])[last()]"

        # Confirmation, questionnaires, medical device tab
        self.Confirmation_Questionnaires_Medical_Device_Tab = "//button[contains(text(), 'Confirmation, questionnaires, medical device')]"
        self.Edit_Questionnaires_Button = "(//button[contains(text(), 'Edit')])[2]"
        self.Group_Name = "//input[@name='QuestionnairesSection-groupName']"
        self.Questionnaire_Codes = "//div[@data-testid='QuestionnairesSection-questionnaireCodes']"

        # Window tab
        self.Window_Tab = "//button[contains(text(), 'Window')]"
        self.Edit_Visit_Window_Button = "(//button[contains(text(), 'Edit')])[1]"
        self.Protocol_Rule = "//input[@name='protocolRule']"
        self.Visit_Day_Not_Available = "(//input[@value='Not available'])[1]"
        self.Visit_Window_Start_Not_Available = "(//input[@value='Not available'])[3]"
        self.Visit_Window_End_Not_Available = "(//input[@value='Not available'])[5]"
        self.Calculate_Date_Not_Available = "(//input[@value='Not Available'])[1]"

        # Scheduling tab
        self.Scheduling_Tab = "//button[contains(text(), 'Scheduling')]"
        self.Start_Action_Not_Available = "(//input[@value='Not available'])[1]"
        self.End_Action_Not_Available = "(//input[@value='Not available'])[2]"
        self.While_Action_Not_Available = "(//input[@value='Not available'])[5]"
        self.Status_Type = "//input[@name='statusType']"
        self.Edit_Scheduling = "(//button[contains(text(), 'Edit')])[1]"

        # Bio sampling tab
        self.Bio_Sampling_Tab = "//button[contains(text(), 'Bio sampling')]"
        self.Edit_Bio_Sample = "(//button[contains(text(), 'Edit')])[1]"

        # Notification tab
        self.Notifications_Tab = "//button[contains(text(), 'Notifications')]"
        self.Edit_Notif = "(//button[contains(text(), 'Edit')])[1]"
        self.Notif_Last_Option = "(//ul/li[@role='option'])[last()]"

        # Notification 1
        self.Visit_Notif1 = "//div[@data-testid='Notification1-visitsNotification1']"
        self.Notif_1_Num_Offset = "//input[@name='Notification1-notificationOffset1-field1']"
        self.Notif_1_Period_Offset = "(//div[@id='undefined-select'])[2]"

        # Notification 2
        self.Visit_Notif2 = "//div[@data-testid='Notification2-visitsNotification2']"
        self.Notif_2_Num_Offset = "//input[@name='Notification2-notificationOffset1-field2']"
        self.Notif_2_Period_Offset = "(//div[@id='undefined-select'])[4]"

        # Notification 3
        self.Visit_Notif3 = "//div[@data-testid='Notification3-visitsNotification3']"
        self.Notif_3_Num_Offset = "//input[@name='Notification3-notificationOffset1-field3']"
        self.Notif_3_Period_Offset = "(//div[@id='undefined-select'])[6]"

        # Notification 4
        self.Visit_Notif4 = "//div[@data-testid='Notification4-visitsNotification4']"
        self.Notif_4_Num_Offset = "//input[@name='Notification4-notificationOffset1-field4']"
        self.Notif_4_Period_Offset = "(//div[@id='undefined-select'])[8]"

        # Notification 5
        self.Visit_Notif5 = "//div[@data-testid='Notification5-visitsNotification5']"
        self.Notif_5_Num_Offset = "//input[@name='Notification5-notificationOffset1-field5']"
        self.Notif_5_Period_Offset = "(//div[@id='undefined-select'])[10]"


def create_visits_general_card_only(self):
    self.page.locator(self.Visits_Tab).click()
    self.page.locator(self.Add_A_Visit_Button).click()

    self.page.locator(self.Schedule_Code).click()
    self.page.keyboard.press("ArrowDown")
    self.page.keyboard.press("Enter")

    self.page.locator(self.Visit_Id).fill(str(time.time()))

    self.page.locator(self.Visit_Variant).click()
    self.page.keyboard.press("ArrowDown")
    self.page.keyboard.press("Enter")

    self.page.locator(self.Location_Type).click()
    self.page.keyboard.press("ArrowDown")
    self.page.keyboard.press("Enter")

    self.page.locator(self.Save_Button).click()
    self.page.locator(self.Close_Button).click()


def create_visits_general_card_only(self):
    self.page.locator(self.Visits_Tab).click()
    self.page.locator(self.Add_A_Visit_Button).click()

    self.page.locator(self.Schedule_Code).click()
    self.page.keyboard.press("ArrowDown")
    self.page.keyboard.press("Enter")

    self.page.locator(self.Visit_Id).fill(str(time.time()))

    self.page.locator(self.Visit_Variant).click()
    self.page.keyboard.press("ArrowDown")
    self.page.keyboard.press("Enter")

    self.page.locator(self.Location_Type).click()
    self.page.keyboard.press("ArrowDown")
    self.page.keyboard.press("Enter")

    self.page.locator(self.Save_Button).click()
    self.page.locator(self.Close_Button).click()


def create_visits_all_cards(self):
    self.page.locator(self.Visits_Tab).click()
    self.page.locator(self.Add_A_Visit_Button).click()

    # General tab
    self.page.locator(self.Schedule_Code).click()
    self.page.keyboard.press("ArrowDown")
    self.page.keyboard.press("Enter")

    self.page.locator(self.Visit_Id).fill(str(time.time()))

    self.page.locator(self.Visit_Variant).click()
    self.page.keyboard.press("ArrowDown")
    self.page.keyboard.press("Enter")

    self.page.locator(self.Location_Type).click()
    self.page.keyboard.press("ArrowDown")
    self.page.keyboard.press("Enter")

    self.page.locator(self.Save_Button).click()

    # Information tab
    self.page.locator(self.Information_Tab).click()

    self.page.locator(self.Visit_Title).fill(str(time.time()))

    self.page.locator(self.Visit_Type).click()
    self.page.keyboard.press("ArrowDown")
    self.page.keyboard.press("Enter")

    self.page.locator(self.Visit_Purpose).fill(str(time.time()))

    self.page.locator(self.Patient_Description).fill(str(time.time()))

    self.page.locator(self.Patient_Pre_Activities_Description).fill(str(time.time()))

    self.page.locator(self.Version).fill(str(1.0))

    self.page.locator(self.Save_Button).click()
    self.page.locator(self.Close_Button).click()

    # Confirmation, Questionnaires, medical devices tab
    self.page.locator(self.Visits_Record).click()
    self.page.locator(self.Confirmation_Questionnaires_Medical_Device_Tab).click()
    self.page.locator(self.Edit_Questionnaires_Button).click()

    self.page.locator(self.Group_Name).fill(str(time.time()))

    # Requires questionnaire code from Questionnaires feature
    wait_and_click_element(self.page, self.Questionnaire_Codes)
    self.page.keyboard.press("ArrowDown")
    self.page.keyboard.press("Enter")

    self.page.locator(self.Save_Button).click()
    self.page.locator(self.Close_Button).click()

    # Window tab
    self.page.locator(self.Window_Tab).click()
    self.page.locator(self.Edit_Visit_Window_Button).click()

    self.page.locator(self.Protocol_Rule).fill(str(time.time()))

    """These locators at time of writing may not be necessary as defaults values of window card is NA"""
    self.page.locator(self.Visit_Day_Not_Available).click()
    self.page.locator(self.Visit_Window_Start_Not_Available).click()
    self.page.locator(self.Visit_Window_End_Not_Available).click()
    self.page.locator(self.Calculate_Date_Not_Available).click()

    self.page.locator(self.Save_Button).click()

    # Scheduling tab
    self.page.locator(self.Scheduling_Tab).click()
    self.page.locator(self.Edit_Scheduling).click()
    self.page.locator(self.Start_Action_Not_Available).click()
    self.page.locator(self.End_Action_Not_Available).click()
    wait_and_click_element(self.page, self.While_Action_Not_Available)
    self.page.locator(self.Status_Type).fill(str(time.time()))
    self.page.locator(self.Save_Button).click()

    # Bio sampling tab
    self.page.locator(self.Bio_Sampling_Tab).click()
    self.page.locator(self.Edit_Bio_Sample).click()
    self.page.locator(self.Cancel_Button).click()

    # Notifications tab
    self.page.locator(self.Notifications_Tab).click()
    self.page.locator(self.Edit_Notif).click()

    # Notification 1
    wait_and_click_element(self.page, self.Visit_Notif1)
    self.page.locator(self.Notif_Last_Option).click()
    self.page.locator(self.Notif_1_Num_Offset).fill(str(time.time()))
    self.page.locator(self.Notif_1_Period_Offset).click()
    self.page.keyboard.press("ArrowDown")
    self.page.keyboard.press("Enter")

    # Notification 2
    wait_and_click_element(self.page, self.Visit_Notif2)
    self.page.locator(self.Notif_Last_Option).click()
    self.page.locator(self.Notif_2_Num_Offset).fill(str(time.time()))
    self.page.locator(self.Notif_2_Period_Offset).click()
    self.page.keyboard.press("ArrowDown")
    self.page.keyboard.press("Enter")

    wait_and_click_element(self.page, self.Visit_Notif3)
    self.page.locator(self.Notif_Last_Option).click()
    self.page.locator(self.Notif_3_Num_Offset).fill(str(time.time()))
    self.page.locator(self.Notif_3_Period_Offset).click()
    self.page.keyboard.press("ArrowDown")
    self.page.keyboard.press("Enter")

    wait_and_click_element(self.page, self.Visit_Notif4)
    self.page.locator(self.Notif_Last_Option).click()
    self.page.locator(self.Notif_4_Num_Offset).fill(str(time.time()))
    self.page.locator(self.Notif_4_Period_Offset).click()
    self.page.keyboard.press("ArrowDown")
    self.page.keyboard.press("Enter")

    wait_and_click_element(self.page, self.Visit_Notif5)
    self.page.locator(self.Notif_Last_Option).click()
    self.page.locator(self.Notif_5_Num_Offset).fill(str(time.time()))
    self.page.locator(self.Notif_5_Period_Offset).click()
    self.page.keyboard.press("ArrowDown")
    self.page.keyboard.press("Enter")

    self.page.locator(self.Save_Button).click()


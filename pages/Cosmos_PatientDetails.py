import time

from playwright.sync_api import Page, expect
from utils.wait_helpers import wait_and_click_element, wait_for_element

class Cosmos_PatientDetails:
    def __init__(self, page: Page):
        self.page = page  # Ensure page is set
        self.Patient_Details_feature = "//p[contains(text(), 'Patient details')]"
        #Universal save, cancel, close 
        self.Save_Button="//button[contains(text(), 'Save')]"
        self.Cancel_button="//button[contains(text(), 'Cancel')]"
        self.Close_button="//button[contains(text(), 'Close')]"
        
        #Date of birth card/tile
        self.DOB_card_edit_button = "//div[@data-testid='date-of-birth-card']//button[@class='MuiTypography-root MuiTypography-inherit MuiLink-root MuiLink-underlineAlways MuiLink-button css-95lpad'][normalize-space()='Edit']"
        self.DOB_Card_Title = "//span[contains(text(), 'Date of birth')]"
        self.DOB_card_Included_in_study = "//div[@data-testid='date-of-birth-card']//p[contains(text(), 'Included in study')]"
        self.DOB_card_Included_in_study_value = "//div[@data-testid='date-of-birth-card']//p[contains(text(), 'Included in study')]//parent::div/following-sibling::div/p"
        self.DOB_card_Source = "//div[@data-testid='date-of-birth-card']//p[contains(text(), 'Source')]"
        self.DOB_card_Source_value = "//div[@data-testid='date-of-birth-card']//p[contains(text(), 'Source')]//parent::div/following-sibling::div/p"
         #needed if nothing is seleced can be used for study values and mandatory in study if needed
        self.DOB_card_Source_value_Mandatory = "//div[@data-testid='date-of-birth-card']//p[contains(text(), 'Source')]//parent::div/following-sibling::div[normalize-space()='Mandatory']"
        self.DOB_card_Study_Values = "//div[@data-testid='date-of-birth-card']//p[contains(text(), 'Study values')]"
        self.DOB_card_Study_Values_value = "//div[@data-testid='date-of-birth-card']//p[contains(text(), 'Study values')]//parent::div/following-sibling::div/p"
        self.DOB_card_Madatory_in_study = "//div[@data-testid='date-of-birth-card']//p[contains(text(), 'Mandatory in study')]"
        self.DOB_card_Madatory_in_study_value = "//div[@data-testid='date-of-birth-card']//p[contains(text(), 'Mandatory in study')]//parent::div/following-sibling::div/p"
        self.DOB_card_Visible_for_CRA = "//div[@data-testid='date-of-birth-card']//p[contains(text(), 'Visible for CRA')]"
        self.DOB_card_Visible_for_CRA_value = "//div[@data-testid='date-of-birth-card']//p[contains(text(), 'Visible for CRA')]//parent::div/following-sibling::div/p"
        self.DOB_card_Visible_for_support_role = "//div[@data-testid='date-of-birth-card']//p[contains(text(), 'Visible for support role')]"
        self.DOB_card_Visible_for_support_role_value = "//div[@data-testid='date-of-birth-card']//p[contains(text(), 'Visible for support role')]//parent::div/following-sibling::div/p"
        self.DOB_card_Visible_for_GST = "//div[@data-testid='date-of-birth-card']//p[contains(text(), 'Visible for GST')]"
        self.DOB_card_Visible_for_GST_value = "//div[@data-testid='date-of-birth-card']//p[contains(text(), 'Visible for GST')]//parent::div/following-sibling::div/p"

        #Date of birth modal/tab
        self.Gender_tab = "//button[@id='DateOfBirth-0']"
        self.DOB_Modal_Include_in_study = "//div[@id='DateOfBirth-0']//div[@data-testid='featureFormComponent-includedInStudy']//label/h6"
        self.DOB_Modal_Include_in_study_value = "//p[@data-testid='DateOfBirthSection-includedInStudy']"
        self.DOB_Modal_Source = "//div[@id='DateOfBirth-0']//div[@data-testid='featureFormComponent-source']//label/h6"
        self.DOB_Modal_Source_Manual_radio_button = "//input[@name ='DateOfBirthSection-source' and  @value='Manual']"
        self.DOB_Modal_Source_RTSM_radio_button = "//input[@name ='DateOfBirthSection-source' and  @value='RTSM']"
        self.DOB_Modal_Study_values = "//div[@id='DateOfBirth-0']//div[@data-testid='featureFormComponent-studyValues']//label/h6"
        self.DOB_Modal_Study_values_Link = "//a[@target='_blank']"
        self.DOB_Modal_Mandatory_in_study = "//div[@id='DateOfBirth-0']//div[@data-testid='featureFormComponent-mandatoryInStudy']//label/h6"
        self.DOB_Modal_Mandatory_in_study_value = "//p[@data-testid='DateOfBirthSection-mandatoryInStudy']"
        self.DOB_Modal_Visible_for_CRA = "//div[@id='DateOfBirth-0']//div[@data-testid='featureFormComponent-visibleForCRA']//label/h6"
        self.DOB_Modal_Visible_for_CRA_Yes_radio_button = "//input[@name ='DateOfBirthSection-visibleForCRA' and  @value='Yes']"
        self.DOB_Modal_Visible_for_CRA_No_radio_button = "//input[@name ='DateOfBirthSection-visibleForCRA' and  @value='No']"
        self.DOB_Modal_Visible_for_support_role = "//div[@id='DateOfBirth-0']//div[@data-testid='featureFormComponent-visibleForSupportRole']//label/h6"
        self.DOB_Modal_Visible_for_support_role_Yes_radio_button = "//input[@name ='DateOfBirthSection-visibleForSupportRole' and  @value='Yes']"
        self.DOB_Modal_Visible_for_support_role_No_radio_button = "//input[@name ='DateOfBirthSection-visibleForSupportRole' and  @value='No']"
        self.DOB_Modal_Visible_for_GST = "//div[@id='DateOfBirth-0']//div[@data-testid='featureFormComponent-visibleForGST']//label/h6"
        self.DOB_Modal_Visible_for_GST_Yes_radio_button = "//input[@name ='DateOfBirthSection-visibleForGST' and  @value='Yes']"
        self.DOB_Modal_Visible_for_GST_No_radio_button = "//input[@name ='DateOfBirthSection-visibleForGST' and  @value='No']"
        self.DOB_Modal_decsription_1 ="//div[@id='DateOfBirth-0']//div[@class='css-rfflj']/p[contains(text(), 'Set the details')]"
        self.DOB_Modal_decsription_2 ="//div[@id='DateOfBirth-0']//div[@class='css-rfflj']/p[contains(text(), 'save form')]"

        #Gender card/tile
        self.Gender_card_edit_button = "//div[@data-testid='gender-card']//button[@class='MuiTypography-root MuiTypography-inherit MuiLink-root MuiLink-underlineAlways MuiLink-button css-95lpad'][normalize-space()='Edit']"
        self.Gender_Card_Title = "//span[contains(text(), 'Gender')]"
        self.Gender_card_Included_in_study = "//div[@data-testid='gender-card']//p[contains(text(), 'Included in study')]"
        self.Gender_card_Included_in_study_value = "//div[@data-testid='gender-card']//p[contains(text(), 'Included in study')]//parent::div/following-sibling::div/p"
        self.Gender_card_Source = "//div[@data-testid='gender-card']//p[contains(text(), 'Source')]"
        self.Gender_card_Source_value = "//div[@data-testid='gender-card']//p[contains(text(), 'Source')]//parent::div/following-sibling::div/p"
         #needed if nothing is seleced can be used for study values and mandatory in study if needed
        self.Gender_card_Source_value_Mandatory = "//div[@data-testid='gender-card']//p[contains(text(), 'Source')]//parent::div/following-sibling::div[normalize-space()='Mandatory']"
        self.Gender_card_Study_Values = "//div[@data-testid='gender-card']//p[contains(text(), 'Study values')]"
        self.Gender_card_Study_Values_value = "//div[@data-testid='gender-card']//p[contains(text(), 'Study values')]//parent::div/following-sibling::div/p"
        self.Gender_card_Madatory_in_study = "//div[@data-testid='gender-card']//p[contains(text(), 'Mandatory in study')]"
        self.Gender_card_Madatory_in_study_value = "//div[@data-testid='gender-card']//p[contains(text(), 'Mandatory in study')]//parent::div/following-sibling::div/p"
        self.Gender_card_Visible_for_CRA = "//div[@data-testid='gender-card']//p[contains(text(), 'Visible for CRA')]"
        self.Gender_card_Visible_for_CRA_value = "//div[@data-testid='gender-card']//p[contains(text(), 'Visible for CRA')]//parent::div/following-sibling::div/p"
        self.Gender_card_Visible_for_support_role = "//div[@data-testid='gender-card']//p[contains(text(), 'Visible for support role')]"
        self.Gender_card_Visible_for_support_role_value = "//div[@data-testid='gender-card']//p[contains(text(), 'Visible for support role')]//parent::div/following-sibling::div/p"
        self.Gender_card_Visible_for_GST = "//div[@data-testid='gender-card']//p[contains(text(), 'Visible for GST')]"
        self.Gender_card_Visible_for_GST_value = "//div[@data-testid='gender-card']//p[contains(text(), 'Visible for GST')]//parent::div/following-sibling::div/p"

        #Gender modal/tab
        self.Gender_tab = "//button[@id='Gender-1']"
        self.Gender_Modal_Include_in_study = "//div[@id='Gender-1']//div[@data-testid='featureFormComponent-includedInStudy']//label/h6"
        self.Gender_Modal_Include_in_study_Yes_radio_button = "//input[@name ='GenderSection-includedInStudy' and  @value='Yes']"
        self.Gender_Modal_Include_in_study_No_radio_button = "//input[@name ='GenderSection-includedInStudy' and  @value='No']"
        self.Gender_Modal_Source = "//div[@id='Gender-1']//div[@data-testid='featureFormComponent-source']//label/h6"
        self.Gender_Modal_Source_Manual_radio_button = "//input[@name ='GenderSection-source' and  @value='Manual']"
        self.Gender_Modal_Source_RTSM_radio_button = "//input[@name ='GenderSection-source' and  @value='RTSM']"
        self.Gender_Modal_Study_values = "//div[@id='Gender-1']//div[@data-testid='featureFormComponent-studyValues']//label/h6"
        self.Gender_Modal_Study_values_Dropdown = "//input[@placeholder='E.g. Male']"
        self.Gender_Modal_Mandatory_in_study = "//div[@id='Gender-1']//div[@data-testid='featureFormComponent-mandatoryInStudy']//label/h6"
        self.Gender_Modal_Mandatory_in_study_Yes_radio_button = "//input[@name ='GenderSection-mandatoryInStudy' and  @value='Yes']"
        self.Gender_Modal_Mandatory_in_study_No_radio_button = "//input[@name ='GenderSection-mandatoryInStudy' and  @value='No']"
        self.Gender_Modal_Visible_for_CRA = "//div[@id='Gender-1']//div[@data-testid='featureFormComponent-visibleForCRA']//label/h6"
        self.Gender_Modal_Visible_for_CRA_Yes_radio_button = "//input[@name ='GenderSection-visibleForCRA' and  @value='Yes']"
        self.Gender_Modal_Visible_for_CRA_No_radio_button = "//input[@name ='GenderSection-visibleForCRA' and  @value='No']"
        self.Gender_Modal_Visible_for_support_role = "//div[@id='Gender-1']//div[@data-testid='featureFormComponent-visibleForSupportRole']//label/h6"
        self.Gender_Modal_Visible_for_support_role_Yes_radio_button = "//input[@name ='GenderSection-visibleForSupportRole' and  @value='Yes']"
        self.Gender_Modal_Visible_for_support_role_No_radio_button = "//input[@name ='GenderSection-visibleForSupportRole' and  @value='No']"
        self.Gender_Modal_Visible_for_GST = "//div[@id='Gender-1']//div[@data-testid='featureFormComponent-visibleForGST']//label/h6"
        self.Gender_Modal_Visible_for_GST_Yes_radio_button = "//input[@name ='GenderSection-visibleForGST' and  @value='Yes']"
        self.Gender_Modal_Visible_for_GST_No_radio_button = "//input[@name ='GenderSection-visibleForGST' and  @value='No']"
        self.Gender_Modal_decsription_1 ="//div[@id='Gender-1']//div[@class='css-rfflj']/p[contains(text(), 'Set the details')]"
        self.Gender_Modal_decsription_2 ="//div[@id='Gender-1']//div[@class='css-rfflj']/p[contains(text(), 'save form')]"


        

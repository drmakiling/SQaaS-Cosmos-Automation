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
         #needed if nothing is selected can be used for study values and mandatory in study if needed
        self.DOB_card_Source_value_Mandatory = "//div[@data-testid='date-of-birth-card']//p[contains(text(), 'Source')]//parent::div/following-sibling::div[normalize-space()='Mandatory']"
        self.DOB_card_Study_Values = "//div[@data-testid='date-of-birth-card']//p[contains(text(), 'Study values')]"
        self.DOB_card_Study_Values_value = "//div[@data-testid='date-of-birth-card']//p[contains(text(), 'Study values')]//parent::div/following-sibling::div/p"
        self.DOB_card_Mandatory_in_study = "//div[@data-testid='date-of-birth-card']//p[contains(text(), 'Mandatory in study')]"
        self.DOB_card_Mandatory_in_study_value = "//div[@data-testid='date-of-birth-card']//p[contains(text(), 'Mandatory in study')]//parent::div/following-sibling::div/p"
        self.DOB_card_Visible_for_CRA = "//div[@data-testid='date-of-birth-card']//p[contains(text(), 'Visible for CRA')]"
        self.DOB_card_Visible_for_CRA_value = "//div[@data-testid='date-of-birth-card']//p[contains(text(), 'Visible for CRA')]//parent::div/following-sibling::div/p"
        self.DOB_card_Visible_for_support_role = "//div[@data-testid='date-of-birth-card']//p[contains(text(), 'Visible for support role')]"
        self.DOB_card_Visible_for_support_role_value = "//div[@data-testid='date-of-birth-card']//p[contains(text(), 'Visible for support role')]//parent::div/following-sibling::div/p"
        self.DOB_card_Visible_for_GST = "//div[@data-testid='date-of-birth-card']//p[contains(text(), 'Visible for GST')]"
        self.DOB_card_Visible_for_GST_value = "//div[@data-testid='date-of-birth-card']//p[contains(text(), 'Visible for GST')]//parent::div/following-sibling::div/p"

        #Date of birth modal/tab
        self.DOB_tab = "//button[@id='DateOfBirth-0']"
        self.DOB_Modal_title = "//div[@id='DateOfBirth-0']/descendant::span[text()='Date of birth']"
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
        self.Gender_card_Mandatory_in_study = "//div[@data-testid='gender-card']//p[contains(text(), 'Mandatory in study')]"
        self.Gender_card_Mandatory_in_study_value = "//div[@data-testid='gender-card']//p[contains(text(), 'Mandatory in study')]//parent::div/following-sibling::div/p"
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
        self.Gender_Modal_Study_values_Dropdown_choice_X_button = "//div[@id='Gender-1']//div[@data-testid='GenderSection-studyValues']//div//div[@role='button']/span[@class='MuiChip-deleteIcon MuiChip-deleteIconSmall MuiChip-deleteIconColorDefault MuiChip-deleteIconFilledColorDefault MuiBox-root css-10usvc8']"
        self.Gender_Modal_Mandatory_in_study = "//div[@id='Gender-1']//div[@data-testid='featureFormComponent-mandatoryInStudy']//label/h6"
        self.Gender_Modal_Mandatory_in_study_Mandatory_radio_button = "//input[@name ='GenderSection-mandatoryInStudy' and  @value='Mandatory']"
        self.Gender_Modal_Mandatory_in_study_Optional_radio_button = "//input[@name ='GenderSection-mandatoryInStudy' and  @value='Optional']"
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

        #Weight card/tile
        self.Weight_card_edit_button = "//div[@data-testid='weight-card']//button[@class='MuiTypography-root MuiTypography-inherit MuiLink-root MuiLink-underlineAlways MuiLink-button css-95lpad'][normalize-space()='Edit']"
        self.Weight_Card_Title = "//span[contains(text(), 'Weight')]"
        self.Weight_card_Included_in_study = "//div[@data-testid='weight-card']//p[contains(text(), 'Included in study')]"
        self.Weight_card_Included_in_study_value = "//div[@data-testid='weight-card']//p[contains(text(), 'Included in study')]//parent::div/following-sibling::div/p"
        self.Weight_card_Source = "//div[@data-testid='weight-card']//p[contains(text(), 'Source')]"
        self.Weight_card_Source_value = "//div[@data-testid='weight-card']//p[contains(text(), 'Source')]//parent::div/following-sibling::div/p"
         #needed if nothing is seleced can be used for study values and mandatory in study if needed
        self.Weight_card_Source_value_Mandatory = "//div[@data-testid='weight-card']//p[contains(text(), 'Source')]//parent::div/following-sibling::div[normalize-space()='Mandatory']"
        self.Weight_card_Study_Values = "//div[@data-testid='weight-card']//p[contains(text(), 'Study values')]"
        self.Weight_card_Study_Values_value = "//div[@data-testid='weight-card']//p[contains(text(), 'Study values')]//parent::div/following-sibling::div/p"
        self.Weight_card_Madatory_in_study = "//div[@data-testid='weight-card']//p[contains(text(), 'Mandatory in study')]"
        self.Weight_card_Madatory_in_study_value = "//div[@data-testid='weight-card']//p[contains(text(), 'Mandatory in study')]//parent::div/following-sibling::div/p"
        self.Weight_card_Visible_for_CRA = "//div[@data-testid='weight-card']//p[contains(text(), 'Visible for CRA')]"
        self.Weight_card_Visible_for_CRA_value = "//div[@data-testid='weight-card']//p[contains(text(), 'Visible for CRA')]//parent::div/following-sibling::div/p"
        self.Weight_card_Visible_for_support_role = "//div[@data-testid='weight-card']//p[contains(text(), 'Visible for support role')]"
        self.Weight_card_Visible_for_support_role_value = "//div[@data-testid='weight-card']//p[contains(text(), 'Visible for support role')]//parent::div/following-sibling::div/p"
        self.Weight_card_Visible_for_GST = "//div[@data-testid='weight-card']//p[contains(text(), 'Visible for GST')]"
        self.Weight_card_Visible_for_GST_value = "//div[@data-testid='weight-card']//p[contains(text(), 'Visible for GST')]//parent::div/following-sibling::div/p"

        #Weight modal/tab
        self.Weight_tab = "//button[@id='Weight-2']"
        self.Weight_Modal_Include_in_study = "//div[@id='Weight-2']//div[@data-testid='featureFormComponent-includedInStudy']//label/h6"
        self.Weight_Modal_Include_in_study_Yes_radio_button = "//input[@name ='WeightSection-includedInStudy' and  @value='Yes']"
        self.Weight_Modal_Include_in_study_No_radio_button = "//input[@name ='WeightSection-includedInStudy' and  @value='No']"
        self.Weight_Modal_Source = "//div[@id='Weight-2']//div[@data-testid='featureFormComponent-source']//label/h6"
        self.Weight_Modal_Source_Value = "//div[@id='Weight-2']//div[@data-testid='featureFormComponent-source']//label/p"
        self.Weight_Modal_Source_Manual_radio_button = "//input[@name ='WeightSection-source' and  @value='Manual']"
        self.Weight_Modal_Source_RTSM_radio_button = "//input[@name ='WeightSection-source' and  @value='RTSM']"
        self.Weight_Modal_Study_values = "//div[@id='Weight-2']//div[@data-testid='featureFormComponent-studyValues']//label/h6"
        self.Weight_Modal_Study_values_Value= "//div[@id='Weight-2']//div[@data-testid='featureFormComponent-studyValues']//label/p"
        self.Weight_Modal_Mandatory_in_study = "//div[@id='Weight-2']//div[@data-testid='featureFormComponent-mandatoryInStudy']//label/h6"
        self.Weight_Modal_Mandatory_in_study_Yes_radio_button = "//input[@name ='WeightSection-mandatoryInStudy' and  @value='Yes']"
        self.Weight_Modal_Mandatory_in_study_No_radio_button = "//input[@name ='WeightSection-mandatoryInStudy' and  @value='No']"
        self.Weight_Modal_Visible_for_CRA = "//div[@id='Weight-2']//div[@data-testid='featureFormComponent-visibleForCRA']//label/h6"
        self.Weight_Modal_Visible_for_CRA_Yes_radio_button = "//input[@name ='WeightSection-visibleForCRA' and  @value='Yes']"
        self.Weight_Modal_Visible_for_CRA_No_radio_button = "//input[@name ='WeightSection-visibleForCRA' and  @value='No']"
        self.Weight_Modal_Visible_for_support_role = "//div[@id='Weight-2']//div[@data-testid='featureFormComponent-visibleForSupportRole']//label/h6"
        self.Weight_Modal_Visible_for_support_role_Yes_radio_button = "//input[@name ='WeightSection-visibleForSupportRole' and  @value='Yes']"
        self.Weight_Modal_Visible_for_support_role_No_radio_button = "//input[@name ='WeightSection-visibleForSupportRole' and  @value='No']"
        self.Weight_Modal_Visible_for_GST = "//div[@id='Weight-2']//div[@data-testid='featureFormComponent-visibleForGST']//label/h6"
        self.Weight_Modal_Visible_for_GST_Yes_radio_button = "//input[@name ='WeightSection-visibleForGST' and  @value='Yes']"
        self.Weight_Modal_Visible_for_GST_No_radio_button = "//input[@name ='WeightSection-visibleForGST' and  @value='No']"
        self.Weight_Modal_decsription_1 ="//div[@id='Weight-2']//div[@class='css-rfflj']/p[contains(text(), 'Set the details')]"
        self.Weight_Modal_decsription_2 ="//div[@id='Weight-2']//div[@class='css-rfflj']/p[contains(text(), 'save form')]"


        #Height card/tile
        self.Height_card_edit_button = "//div[@data-testid='height-card']//button[@class='MuiTypography-root MuiTypography-inherit MuiLink-root MuiLink-underlineAlways MuiLink-button css-95lpad'][normalize-space()='Edit']"
        self.Height_Card_Title = "//span[contains(text(), 'Height')]"
        self.Height_card_Included_in_study = "//div[@data-testid='height-card']//p[contains(text(), 'Included in study')]"
        self.Height_card_Included_in_study_value = "//div[@data-testid='height-card']//p[contains(text(), 'Included in study')]//parent::div/following-sibling::div/p"
        self.Height_card_Source = "//div[@data-testid='height-card']//p[contains(text(), 'Source')]"
        self.Height_card_Source_value = "//div[@data-testid='height-card']//p[contains(text(), 'Source')]//parent::div/following-sibling::div/p"
         #needed if nothing is seleced can be used for study values and mandatory in study if needed
        self.Height_card_Source_value_Mandatory = "//div[@data-testid='height-card']//p[contains(text(), 'Source')]//parent::div/following-sibling::div[normalize-space()='Mandatory']"
        self.Height_card_Study_Values = "//div[@data-testid='height-card']//p[contains(text(), 'Study values')]"
        self.Height_card_Study_Values_value = "//div[@data-testid='height-card']//p[contains(text(), 'Study values')]//parent::div/following-sibling::div/p"
        self.Height_card_Madatory_in_study = "//div[@data-testid='height-card']//p[contains(text(), 'Mandatory in study')]"
        self.Height_card_Madatory_in_study_value = "//div[@data-testid='height-card']//p[contains(text(), 'Mandatory in study')]//parent::div/following-sibling::div/p"
        self.Height_card_Visible_for_CRA = "//div[@data-testid='height-card']//p[contains(text(), 'Visible for CRA')]"
        self.Height_card_Visible_for_CRA_value = "//div[@data-testid='height-card']//p[contains(text(), 'Visible for CRA')]//parent::div/following-sibling::div/p"
        self.Height_card_Visible_for_support_role = "//div[@data-testid='height-card']//p[contains(text(), 'Visible for support role')]"
        self.Height_card_Visible_for_support_role_value = "//div[@data-testid='height-card']//p[contains(text(), 'Visible for support role')]//parent::div/following-sibling::div/p"
        self.Height_card_Visible_for_GST = "//div[@data-testid='height-card']//p[contains(text(), 'Visible for GST')]"
        self.Height_card_Visible_for_GST_value = "//div[@data-testid='height-card']//p[contains(text(), 'Visible for GST')]//parent::div/following-sibling::div/p"

        #Height modal/tab
        self.Height_tab = "//button[@id='Height-3']"
        self.Height_Modal_Include_in_study = "//div[@id='Height-3']//div[@data-testid='featureFormComponent-includedInStudy']//label/h6"
        self.Height_Modal_Include_in_study_Yes_radio_button = "//input[@name ='HeightSection-includedInStudy' and  @value='Yes']"
        self.Height_Modal_Include_in_study_No_radio_button = "//input[@name ='HeightSection-includedInStudy' and  @value='No']"
        self.Height_Modal_Source = "//div[@id='Height-3']//div[@data-testid='featureFormComponent-source']//label/h6"
        self.Height_Modal_Source_Value = "//div[@id='height-3']//div[@data-testid='featureFormComponent-source']//label/p"
        self.Height_Modal_Source_Manual_radio_button = "//input[@name ='HeightSection-source' and  @value='Manual']"
        self.Height_Modal_Source_RTSM_radio_button = "//input[@name ='HeightSection-source' and  @value='RTSM']"
        self.Height_Modal_Study_values = "//div[@id='Height-3']//div[@data-testid='featureFormComponent-studyValues']//label/h6"
        self.Height_Modal_Study_values_Value = "//div[@id='Height-3']//div[@data-testid='featureFormComponent-studyValues']//label/p"
        self.Height_Modal_Mandatory_in_study = "//div[@id='Height-3']//div[@data-testid='featureFormComponent-mandatoryInStudy']//label/h6"
        self.Height_Modal_Mandatory_in_study_Yes_radio_button = "//input[@name ='HeightSection-mandatoryInStudy' and  @value='Yes']"
        self.Height_Modal_Mandatory_in_study_No_radio_button = "//input[@name ='HeightSection-mandatoryInStudy' and  @value='No']"
        self.Height_Modal_Visible_for_CRA = "//div[@id='Height-3']//div[@data-testid='featureFormComponent-visibleForCRA']//label/h6"
        self.Height_Modal_Visible_for_CRA_Yes_radio_button = "//input[@name ='HeightSection-visibleForCRA' and  @value='Yes']"
        self.Height_Modal_Visible_for_CRA_No_radio_button = "//input[@name ='HeightSection-visibleForCRA' and  @value='No']"
        self.Height_Modal_Visible_for_support_role = "//div[@id='Height-3']//div[@data-testid='featureFormComponent-visibleForSupportRole']//label/h6"
        self.Height_Modal_Visible_for_support_role_Yes_radio_button = "//input[@name ='HeightSection-visibleForSupportRole' and  @value='Yes']"
        self.Height_Modal_Visible_for_support_role_No_radio_button = "//input[@name ='HeightSection-visibleForSupportRole' and  @value='No']"
        self.Height_Modal_Visible_for_GST = "//div[@id='Height-3']//div[@data-testid='featureFormComponent-visibleForGST']//label/h6"
        self.Height_Modal_Visible_for_GST_Yes_radio_button = "//input[@name ='HeightSection-visibleForGST' and  @value='Yes']"
        self.Height_Modal_Visible_for_GST_No_radio_button = "//input[@name ='HeightSection-visibleForGST' and  @value='No']"
        self.Height_Modal_decsription_1 ="//div[@id='Height-3']//div[@class='css-rfflj']/p[contains(text(), 'Set the details')]"
        self.Height_Modal_decsription_2 ="//div[@id='Height-3']//div[@class='css-rfflj']/p[contains(text(), 'save form')]"

        #Race card/tile
        self.Race_card_edit_button = "//div[@data-testid='race-card']//button[@class='MuiTypography-root MuiTypography-inherit MuiLink-root MuiLink-underlineAlways MuiLink-button css-95lpad'][normalize-space()='Edit']"
        self.Race_Card_Title = "//span[contains(text(), 'Race')]"
        self.Race_card_Included_in_study = "//div[@data-testid='race-card']//p[contains(text(), 'Included in study')]"
        self.Race_card_Included_in_study_value = "//div[@data-testid='race-card']//p[contains(text(), 'Included in study')]//parent::div/following-sibling::div/p"
        self.Race_card_Source = "//div[@data-testid='race-card']//p[contains(text(), 'Source')]"
        self.Race_card_Source_value = "//div[@data-testid='race-card']//p[contains(text(), 'Source')]//parent::div/following-sibling::div/p"
         #needed if nothing is seleced can be used for study values and mandatory in study if needed
        self.Race_card_Source_value_Mandatory = "//div[@data-testid='race-card']//p[contains(text(), 'Source')]//parent::div/following-sibling::div[normalize-space()='Mandatory']"
        self.Race_card_Study_Values = "//div[@data-testid='race-card']//p[contains(text(), 'Study values')]"
        self.Race_card_Study_Values_value = "//div[@data-testid='race-card']//p[contains(text(), 'Study values')]//parent::div/following-sibling::div/p"
        self.Race_card_Madatory_in_study = "//div[@data-testid='race-card']//p[contains(text(), 'Mandatory in study')]"
        self.Race_card_Madatory_in_study_value = "//div[@data-testid='race-card']//p[contains(text(), 'Mandatory in study')]//parent::div/following-sibling::div/p"
        self.Race_card_Visible_for_CRA = "//div[@data-testid='race-card']//p[contains(text(), 'Visible for CRA')]"
        self.Race_card_Visible_for_CRA_value = "//div[@data-testid='race-card']//p[contains(text(), 'Visible for CRA')]//parent::div/following-sibling::div/p"
        self.Race_card_Visible_for_support_role = "//div[@data-testid='race-card']//p[contains(text(), 'Visible for support role')]"
        self.Race_card_Visible_for_support_role_value = "//div[@data-testid='race-card']//p[contains(text(), 'Visible for support role')]//parent::div/following-sibling::div/p"
        self.Race_card_Visible_for_GST = "//div[@data-testid='race-card']//p[contains(text(), 'Visible for GST')]"
        self.Race_card_Visible_for_GST_value = "//div[@data-testid='race-card']//p[contains(text(), 'Visible for GST')]//parent::div/following-sibling::div/p"

        #Race modal/tab
        self.Race_tab = "//button[@id='Race-4']"
        self.Race_Modal_Include_in_study = "//div[@id='Race-4']//div[@data-testid='featureFormComponent-includedInStudy']//label/h6"
        self.Race_Modal_Include_in_study_Yes_radio_button = "//input[@name ='RaceSection-includedInStudy' and  @value='Yes']"
        self.Race_Modal_Include_in_study_No_radio_button = "//input[@name ='RaceSection-includedInStudy' and  @value='No']"
        self.Race_Modal_Source = "//div[@id='Race-4']//div[@data-testid='featureFormComponent-source']//label/h6"
        self.Race_Modal_Source_value = "//div[@id='Race-4']//div[@data-testid='featureFormComponent-source']//label/p"
        self.Race_Modal_Source_Manual_radio_button = "//input[@name ='RaceSection-source' and  @value='Manual']"
        self.Race_Modal_Source_RTSM_radio_button = "//input[@name ='RaceSection-source' and  @value='RTSM']"
        self.Race_Modal_Study_values = "//div[@id='Race-4']//div[@data-testid='featureFormComponent-studyValues']//label/h6"
        self.Race_Modal_Study_values_Dropdown = "//input[@placeholder='E.g. Caucasian']"
        self.Race_Modal_Mandatory_in_study = "//div[@id='Race-4']//div[@data-testid='featureFormComponent-mandatoryInStudy']//label/h6"
        self.Race_Modal_Mandatory_in_study_Yes_radio_button = "//input[@name ='RaceSection-mandatoryInStudy' and  @value='Yes']"
        self.Race_Modal_Mandatory_in_study_No_radio_button = "//input[@name ='RaceSection-mandatoryInStudy' and  @value='No']"
        self.Race_Modal_Visible_for_CRA = "//div[@id='Race-4']//div[@data-testid='featureFormComponent-visibleForCRA']//label/h6"
        self.Race_Modal_Visible_for_CRA_Yes_radio_button = "//input[@name ='RaceSection-visibleForCRA' and  @value='Yes']"
        self.Race_Modal_Visible_for_CRA_No_radio_button = "//input[@name ='RaceSection-visibleForCRA' and  @value='No']"
        self.Race_Modal_Visible_for_support_role = "//div[@id='Race-4']//div[@data-testid='featureFormComponent-visibleForSupportRole']//label/h6"
        self.Race_Modal_Visible_for_support_role_Yes_radio_button = "//input[@name ='RaceSection-visibleForSupportRole' and  @value='Yes']"
        self.Race_Modal_Visible_for_support_role_No_radio_button = "//input[@name ='RaceSection-visibleForSupportRole' and  @value='No']"
        self.Race_Modal_Visible_for_GST = "//div[@id='Race-4']//div[@data-testid='featureFormComponent-visibleForGST']//label/h6"
        self.Race_Modal_Visible_for_GST_Yes_radio_button = "//input[@name ='RaceSection-visibleForGST' and  @value='Yes']"
        self.Race_Modal_Visible_for_GST_No_radio_button = "//input[@name ='RaceSection-visibleForGST' and  @value='No']"
        self.Race_Modal_decsription_1 ="//div[@id='Race-4']//div[@class='css-rfflj']/p[contains(text(), 'Set the details')]"
        self.Race_Modal_decsription_2 ="//div[@id='Race-4']//div[@class='css-rfflj']/p[contains(text(), 'save form')]"

        #Participant ID card/tile
        self.Participant_ID_card_edit_button = "//div[@data-testid='participant-id-card']//button[@class='MuiTypography-root MuiTypography-inherit MuiLink-root MuiLink-underlineAlways MuiLink-button css-95lpad'][normalize-space()='Edit']"
        self.Participant_ID_Card_Title = "//span[contains(text(), 'Participant ID')]"
        self.Participant_ID_card_Format_type = "//div[@data-testid='participant-id-card']//p[contains(text(), 'Participant ID format type')]"
        self.Participant_ID_card_Format_typevalue = "//div[@data-testid='participant-id-card']//p[contains(text(), 'Participant ID format type')]//parent::div/following-sibling::div/p"
        self.Participant_ID_card_format_pattern_description = "//div[@data-testid='participant-id-card']//p[contains(text(), 'Participant ID format pattern description')]"
        self.Participant_ID_card_format_pattern_description_value = "//div[@data-testid='participant-id-card']//p[contains(text(), 'Participant ID format pattern description')]//parent::div/following-sibling::div/p"
        self.Participant_ID_card_helper_text = "//div[@data-testid='participant-id-card']//p[contains(text(), 'Participant ID helper text')]"
        self.Participant_ID_card_helper_text_value = "//div[@data-testid='participant-id-card']//p[contains(text(), 'Participant ID helper text')]//parent::div/following-sibling::div/p"
        self.Participant_ID_card_validation_error_text = "//div[@data-testid='participant-id-card']//p[contains(text(), 'Participant ID validation error text')]"
        self.Participant_ID_card_validation_error_text_value = "//div[@data-testid='participant-id-card']//p[contains(text(), 'Participant ID validation error text')]//parent::div/following-sibling::div/p"
        
        #Participant ID modal/tab
        self.Participant_ID_tab = "//button[@id='ParticipantID-5']"
        self.Participant_ID_Modal_Format_type = "//div[@id='ParticipantID-5']//div[@data-testid='featureFormComponent-participantIDFormatType']//label/h6"
        self.Participant_ID_Modal_Format_type_ECODE_radio_button = "//input[@name ='featureFormComponent-participantIDFormatType' and  @value='ECODE']"
        self.Participant_ID_Modal_Format_type_Custom_radio_button = "//input[@name ='featureFormComponent-participantIDFormatType' and  @value='CUSTOM']"
        self.Participant_ID_Modal_format_pattern_description = "//div[@id='ParticipantID-5']//div[@data-testid='featureFormComponent-participantIDFormatPatternDescription']//label/h6"
        self.Participant_ID_Modal_format_pattern_description_textBox  = "//div[@id='ParticipantID-5']//textarea[@name='ParticipantIDFormatSection-participantIDFormatPatternDescription']"
        self.Participant_ID_Modal_helper_text= "//div[@id='ParticipantID-5']//div[@data-testid='featureFormComponent-participantIDHelperText']//label/h6"
        self.Participant_ID_Modal_helper_text_textBox  = "//div[@id='ParticipantID-5']//textarea[@name='ParticipantIDMessageSection-participantIDHelperText']"
        self.Participant_ID_Modal_validation_error_text = "//div[@id='ParticipantID-5']//div[@data-testid='featureFormComponent-participantIDValidationErrorText']//label/h6"
        self.Participant_ID_Modal_validation_error_text_textBox  = "//div[@id='ParticipantID-5']//textarea[@name='ParticipantIDMessageSection-participantIDValidationErrorText']"
    
    def click_patient_details_nav_option(self):
        # Click on the 'Patient details' nav menu option
        self.page.locator(self.Patient_Details_feature).click()
    
    def verify_dob_card(self, case):
        # Verify Date of birth card parameters, default values and Edit button
        expect(self.page.locator(self.DOB_Card_Title)).to_be_visible()
        expect(self.page.locator(self.DOB_Card_Title)).to_have_text("Date of birth")
        expect(self.page.locator(self.DOB_card_Included_in_study)).to_be_visible()
        expect(self.page.locator(self.DOB_card_Included_in_study)).to_have_text("Included in study")
        expect(self.page.locator(self.DOB_card_Included_in_study_value)).to_be_visible()
        expect(self.page.locator(self.DOB_card_Included_in_study_value)).to_have_text("Yes")
        expect(self.page.locator(self.DOB_card_Source)).to_be_visible()
        expect(self.page.locator(self.DOB_card_Source)).to_have_text("Source")
        expect(self.page.locator(self.DOB_card_Source_value_Mandatory)).to_be_visible()
        expect(self.page.locator(self.DOB_card_Source_value_Mandatory)).to_have_text("Mandatory")
        expect(self.page.locator(self.DOB_card_Study_Values)).to_be_visible()
        expect(self.page.locator(self.DOB_card_Study_Values)).to_have_text("Study values")
        expect(self.page.locator(self.DOB_card_Study_Values_value)).to_be_visible()
        expect(self.page.locator(self.DOB_card_Study_Values_value)).to_have_text("View Countries")
        expect(self.page.locator(self.DOB_card_Mandatory_in_study)).to_be_visible()
        expect(self.page.locator(self.DOB_card_Mandatory_in_study)).to_have_text("Mandatory in study")
        expect(self.page.locator(self.DOB_card_Mandatory_in_study_value)).to_be_visible()
        expect(self.page.locator(self.DOB_card_Mandatory_in_study_value)).to_have_text("Mandatory")
        expect(self.page.locator(self.DOB_card_Visible_for_CRA)).to_be_visible()
        expect(self.page.locator(self.DOB_card_Visible_for_CRA)).to_have_text("Visible for CRA")
        expect(self.page.locator(self.DOB_card_Visible_for_CRA_value)).to_be_visible()
        expect(self.page.locator(self.DOB_card_Visible_for_CRA_value)).to_have_text("No")
        expect(self.page.locator(self.DOB_card_Visible_for_support_role)).to_be_visible()
        expect(self.page.locator(self.DOB_card_Visible_for_support_role)).to_have_text("Visible for support role")
        expect(self.page.locator(self.DOB_card_Visible_for_support_role_value)).to_be_visible()
        expect(self.page.locator(self.DOB_card_Visible_for_support_role_value)).to_have_text("No")
        expect(self.page.locator(self.DOB_card_Visible_for_GST)).to_be_visible()
        expect(self.page.locator(self.DOB_card_Visible_for_GST)).to_have_text("Visible for GST")
        expect(self.page.locator(self.DOB_card_Visible_for_GST_value)).to_be_visible()
        expect(self.page.locator(self.DOB_card_Visible_for_GST_value)).to_have_text("No")
        if case == "2977" or case == "11278" or case == "2991" or case == "2992":
            expect(self.page.locator(self.DOB_card_edit_button)).to_be_visible()
            expect(self.page.locator(self.DOB_card_edit_button)).to_have_text("Edit")
        else:
            expect(self.page.locator(self.DOB_card_edit_button)).to_be_hidden()

    def verify_patient_details_page(self):
        # Verify all other cards on Patient details feature page
        expect(self.page.locator(self.Gender_Card_Title)).to_be_visible()
        expect(self.page.locator(self.Gender_Card_Title)).to_have_text("Gender")
        expect(self.page.locator(self.Gender_card_Included_in_study)).to_be_visible()
        expect(self.page.locator(self.Gender_card_Included_in_study)).to_have_text("Included in study")
        expect(self.page.locator(self.Gender_card_edit_button)).to_be_visible()
        expect(self.page.locator(self.Gender_card_edit_button)).to_have_text("Edit")

        expect(self.page.locator(self.Weight_Card_Title)).to_be_visible()
        expect(self.page.locator(self.Weight_Card_Title)).to_have_text("Weight")
        expect(self.page.locator(self.Weight_card_Included_in_study)).to_be_visible()
        expect(self.page.locator(self.Weight_card_Included_in_study)).to_have_text("Included in study")
        expect(self.page.locator(self.Weight_card_edit_button)).to_be_visible()
        expect(self.page.locator(self.Weight_card_edit_button)).to_have_text("Edit")

        expect(self.page.locator(self.Height_Card_Title)).to_be_visible()
        expect(self.page.locator(self.Height_Card_Title)).to_have_text("Height")
        expect(self.page.locator(self.Height_card_Included_in_study)).to_be_visible()
        expect(self.page.locator(self.Height_card_Included_in_study)).to_have_text("Included in study")
        expect(self.page.locator(self.Height_card_edit_button)).to_be_visible()
        expect(self.page.locator(self.Height_card_edit_button)).to_have_text("Edit")

        expect(self.page.locator(self.Race_Card_Title)).to_be_visible()
        expect(self.page.locator(self.Race_Card_Title)).to_have_text("Race")
        expect(self.page.locator(self.Race_card_Included_in_study)).to_be_visible()
        expect(self.page.locator(self.Race_card_Included_in_study)).to_have_text("Included in study")
        expect(self.page.locator(self.Race_card_edit_button)).to_be_visible()
        expect(self.page.locator(self.Race_card_edit_button)).to_have_text("Edit")
    
    def click_dob_edit_button(self):
        # Click the Date of birth card 'Edit' button
        self.page.locator(self.DOB_card_edit_button).click()
    
    def verify_dob_modal_tab(self):
        # Verify Date of birth modal/tab is displayed
        assert self.page.locator(self.DOB_tab).get_attribute("aria-selected") == "true"
        expect(self.page.locator(self.DOB_tab)).to_have_text("Date of birth")
        expect(self.page.locator(self.DOB_Modal_title)).to_be_visible()
        expect(self.page.locator(self.DOB_Modal_decsription_1)).to_have_text("Set the details of how the Date of birth for Patient Information will be configured for Unify.")
        expect(self.page.locator(self.DOB_Modal_decsription_2)).to_contain_text("* Mandatory to save form")
        expect(self.page.locator(self.DOB_Modal_decsription_2)).to_contain_text("♦ Mandatory for configuration approval")
        expect(self.page.locator(self.DOB_Modal_Include_in_study)).to_have_text("Included in study")
        expect(self.page.locator(self.DOB_Modal_Include_in_study_value)).to_have_text("Yes")
        expect(self.page.locator(self.DOB_Modal_Source)).to_have_text("Source⬥")
        expect(self.page.locator(self.DOB_Modal_Source_Manual_radio_button)).not_to_be_checked()
        expect(self.page.locator(self.DOB_Modal_Source_RTSM_radio_button)).not_to_be_checked()
        expect(self.page.locator(self.DOB_Modal_Study_values)).to_have_text("Study values")
        expect(self.page.locator(self.DOB_Modal_Study_values_Link)).to_have_text("View Countries")
        expect(self.page.locator(self.DOB_Modal_Mandatory_in_study)).to_have_text("Mandatory in study")
        expect(self.page.locator(self.DOB_Modal_Mandatory_in_study_value)).to_have_text("Mandatory")
        expect(self.page.locator(self.DOB_Modal_Visible_for_CRA)).to_have_text("Visible for CRA⬥")
        expect(self.page.locator(self.DOB_Modal_Visible_for_CRA_Yes_radio_button)).not_to_be_checked()
        expect(self.page.locator(self.DOB_Modal_Visible_for_CRA_No_radio_button)).to_be_checked()
        expect(self.page.locator(self.DOB_Modal_Visible_for_support_role)).to_have_text("Visible for support role⬥")
        expect(self.page.locator(self.DOB_Modal_Visible_for_support_role_Yes_radio_button)).not_to_be_checked()
        expect(self.page.locator(self.DOB_Modal_Visible_for_support_role_No_radio_button)).to_be_checked()
        expect(self.page.locator(self.DOB_Modal_Visible_for_GST)).to_have_text("Visible for GST⬥")
        expect(self.page.locator(self.DOB_Modal_Visible_for_GST_Yes_radio_button)).not_to_be_checked()
        expect(self.page.locator(self.DOB_Modal_Visible_for_GST_No_radio_button)).to_be_checked()
        expect(self.page.locator(self.Cancel_button)).to_be_visible()
        expect(self.page.locator(self.Close_button)).to_be_visible()
        expect(self.page.locator(self.Save_Button)).to_be_visible()
        expect(self.page.locator(self.Save_Button)).to_be_disabled()   
        
    def clickEditbuttonForCard(self, card : str):
        selectedCard = card.lower().strip('"').replace(" ", "-")
        self.page.locator("//div[@data-testid='"+ selectedCard + "-card']//button[@class='MuiTypography-root MuiTypography-inherit MuiLink-root MuiLink-underlineAlways MuiLink-button css-95lpad'][normalize-space()='Edit']").click()

    def checkSavedIndicatorIsVisible(self,tab : str) -> bool:
        tab = tab.strip('"')
        return self.page.locator("//button[text() = '" + tab.capitalize()+ "']/*[@data-testid = 'CircleIcon']").is_visible()
    
    def selectIncludeInStudyOption(self,card:str, option:str):
        selectedCard = card.strip('"').capitalize()
        selectedOption = option.strip('"').capitalize()
        self.page.locator("//input[@name ='"+ selectedCard +"Section-includedInStudy' and  @value='"+ selectedOption + "']").click()       
    
    def click_view_countries_link(self, context):
        # Click the 'View Countries' link
        with self.page.context.expect_page() as new_page_info:
            self.page.locator(self.DOB_Modal_Study_values_Link).click()
        context.countries = new_page_info.value
    def clickTabFromPatientDetailsModal(self, tab : str):
        tab = tab.strip('"').capitalize()
        self.page.locator("//div[@aria-label = 'Study Tabs']//button[text() = '" + tab + "']").click()

    def verify_countries_page(self, context):
        # Verify Countries feature page is displayed in a new browser tab
        assert "COUNTRIES" in context.countries.url.upper()
        expect(context.countries.get_by_test_id("landing-header")).to_have_text("Countries")

        expect(self.page.locator(self.Save_Button)).to_be_disabled()

    def Fill_out_DOB_modal(self):
        #fills out source = manual 
        self.page.locator(self.DOB_Modal_Source_Manual_radio_button).click()
        #fills out visible for CRA = No
        self.page.locator(self.DOB_Modal_Visible_for_CRA_No_radio_button).click()
        #fills out visible for Support Role = No
        self.page.locator(self.DOB_Modal_Visible_for_support_role_No_radio_button).click()
        #fills out visible for GST = No
        self.page.locator(self.DOB_Modal_Visible_for_GST_No_radio_button).click()

    def click_save_button(self):
        #clicks save button for any modal
        self.page.locator(self.Save_Button).click()

    def click_close_button(self):
        #clicks close button for any modal
        self.page.locator(self.Close_button).click()

    def verify_date_of_birth_modal_saved(self):
        #verifies data saved from the date of birth modal are reflected on the date of birth card
        expect(self.page.locator(self.DOB_card_Included_in_study_value)).to_be_visible()
        expect(self.page.locator(self.DOB_card_Included_in_study_value)).to_have_text("Yes")
        expect(self.page.locator(self.DOB_card_Source_value)).to_be_visible()
        expect(self.page.locator(self.DOB_card_Source_value)).to_have_text("Manual")
        expect(self.page.locator(self.DOB_card_Study_Values_value)).to_be_visible()
        expect(self.page.locator(self.DOB_card_Study_Values_value)).to_have_text("View Countries")
        expect(self.page.locator(self.DOB_card_Mandatory_in_study_value)).to_be_visible()
        expect(self.page.locator(self.DOB_card_Mandatory_in_study_value)).to_have_text("Mandatory")
        expect(self.page.locator(self.DOB_card_Visible_for_CRA_value)).to_be_visible()
        expect(self.page.locator(self.DOB_card_Visible_for_CRA_value)).to_have_text("No")
        expect(self.page.locator(self.DOB_card_Visible_for_support_role_value)).to_be_visible()
        expect(self.page.locator(self.DOB_card_Visible_for_support_role_value)).to_have_text("No")
        expect(self.page.locator(self.DOB_card_Visible_for_GST_value)).to_be_visible()
        expect(self.page.locator(self.DOB_card_Visible_for_GST_value)).to_have_text("No")


    def verify_gender_not_included_in_study(self):
        expect(self.page.locator(self.Gender_card_Included_in_study)).to_be_visible()
        expect(self.page.locator(self.Gender_card_Included_in_study_value)).to_have_text("No")

    def fill_out_gender_modal(self):
        #fills out included in study = yes 
        self.page.locator(self.Gender_Modal_Include_in_study_Yes_radio_button).click()
         #fills out source = manual 
        self.page.locator(self.Gender_Modal_Source_Manual_radio_button).click()
        #fills out study values = female if something is chose it will delete it and save then choose female
        if (self.page.locator(self.Gender_Modal_Study_values_Dropdown_choice_X_button).is_visible):
            self.page.locator(self.Gender_Modal_Study_values_Dropdown_choice_X_button).click()
            self.page.locator(self.Save_Button).click()
            time.sleep(3)
            self.page.locator(self.Gender_Modal_Study_values_Dropdown).click()
            self.page.keyboard.press("ArrowDown")
            self.page.keyboard.press("Enter")
        else:
            self.page.locator(self.Gender_Modal_Study_values_Dropdown).click()
            self.page.keyboard.press("ArrowDown")
            self.page.keyboard.press("Enter")
        #fills out madatory in study = Mandatory
        self.page.locator(self.Gender_Modal_Mandatory_in_study_Mandatory_radio_button).click()
        #fills out visible for CRA = No
        self.page.locator(self.Gender_Modal_Visible_for_CRA_No_radio_button).click()
        #fills out visible for Support Role = No
        self.page.locator(self.Gender_Modal_Visible_for_support_role_No_radio_button).click()
        #fills out visible for GST = No
        self.page.locator(self.Gender_Modal_Visible_for_GST_No_radio_button).click()
        

    def verify_gender_data_is_saved(self):
        #verifies data saved from the Gender modal are reflected on the date of birth card
        expect(self.page.locator(self.Gender_card_Included_in_study_value)).to_be_visible()
        expect(self.page.locator(self.Gender_card_Included_in_study_value)).to_have_text("Yes")
        expect(self.page.locator(self.Gender_card_Source_value)).to_be_visible()
        expect(self.page.locator(self.Gender_card_Source_value)).to_have_text("Manual")
        expect(self.page.locator(self.Gender_card_Study_Values_value)).to_be_visible()
        expect(self.page.locator(self.Gender_card_Study_Values_value)).to_have_text("Female")
        expect(self.page.locator(self.Gender_card_Mandatory_in_study_value)).to_be_visible()
        expect(self.page.locator(self.Gender_card_Mandatory_in_study_value)).to_have_text("Mandatory")
        expect(self.page.locator(self.Gender_card_Visible_for_CRA_value)).to_be_visible()
        expect(self.page.locator(self.Gender_card_Visible_for_CRA_value)).to_have_text("No")
        expect(self.page.locator(self.Gender_card_Visible_for_support_role_value)).to_be_visible()
        expect(self.page.locator(self.Gender_card_Visible_for_support_role_value)).to_have_text("No")
        expect(self.page.locator(self.Gender_card_Visible_for_GST_value)).to_be_visible()
        expect(self.page.locator(self.Gender_card_Visible_for_GST_value)).to_have_text("No")



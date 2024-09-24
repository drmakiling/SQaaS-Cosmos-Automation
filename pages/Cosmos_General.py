import time

from playwright.sync_api import Page, expect
from utils.wait_helpers import wait_and_click_element, wait_for_element


class Cosmos_General:
    def __init__(self, page: Page):
        self.page = page  # Ensure page is set
        self.General_feature = "//p[contains(text(), 'General')]"
        self.featurePageTitle = "//h6[text()='General']"
        #Universal save, cancel, close 
        self.Save_Button="//button[contains(text(), 'Save')]"
        self.Cancel_button="//button[contains(text(), 'Cancel')]"
       
        #Minimum number of patients to show card
        self.Min_num_of_patients_to_show_edit_button = "//div[@data-testid='general-min-number-of-patients-card']//button[@class='MuiTypography-root MuiTypography-inherit MuiLink-root MuiLink-underlineAlways MuiLink-button css-95lpad'][normalize-space()='Edit']"
        self.Min_num_screen_metrics_title = "//div[@data-testid='general-min-number-of-patients-card']//p[normalize-space()='Screened metrics']"
        self.Min_num_screen_metrics_Value_Mandatory = "//div[@data-testid='general-min-number-of-patients-card']//p[normalize-space()='Screened metrics']//parent::div/following-sibling::div/p"
        self.Min_num_screen_metrics_Value_Mandatory = "//div[@data-testid='general-min-number-of-patients-card']//p[normalize-space()='Screened metrics']//parent::div/following-sibling::div[normalize-space()='Mandatory']"
        self.Min_num_Randomized_metrics_title = "//div[@data-testid='general-min-number-of-patients-card']//p[normalize-space()='Randomized metrics']"
        self.Min_num_Randomized_metrics_Mandatory = "//div[@data-testid='general-min-number-of-patients-card']//p[normalize-space()='Randomized metrics']//parent::div/following-sibling::div/p"
        self.Min_num_Randomized_metrics_Mandatory = "//div[@data-testid='general-min-number-of-patients-card']//p[normalize-space()='Randomized metrics']//parent::div/following-sibling::div[normalize-space()='Mandatory']"
        #Study overview card
        self.Study_overview_edit_button = "//div[@data-testid='general-study-overview-card']//button[@class='MuiTypography-root MuiTypography-inherit MuiLink-root MuiLink-underlineAlways MuiLink-button css-95lpad'][normalize-space()='Edit']"
        self.Study_overview_Brief_overview_of_study_title = "//div[@data-testid='general-study-overview-card']//p[normalize-space()='Brief overview of study']"
        self.Study_overview_Brief_overview_of_study_Mandatory = "//div[@data-testid='general-study-overview-card']//p[normalize-space()='Brief overview of study']//parent::div/following-sibling::div/p"
        self.Study_overview_Brief_overview_of_study_Mandatory = "//div[@data-testid='general-study-overview-card']//p[normalize-space()='Brief overview of study']//parent::div/following-sibling::div[normalize-space()='Mandatory']"
        self.Study_overview_Description_of_the_Study_title = "//div[@data-testid='general-study-overview-card']//p[normalize-space()='Description of the study']"
        self.Study_overview_Description_of_the_Study_Mandatory = "//div[@data-testid='general-study-overview-card']//p[normalize-space()='Description of the study']//parent::div/following-sibling::div/p"
        self.Study_overview_Description_of_the_Study_Mandatory = "//div[@data-testid='general-study-overview-card']//p[normalize-space()='Description of the study']//parent::div/following-sibling::div[normalize-space()='Mandatory']"
        #Minimum number of patients to show modal
        self.Min_Num_Modal_screened_metrics_text_box = "//div[@data-testid='featureFormComponent-screenedMetrics']//input[@name='screenedMetrics']"
        self.Min_Num_Modal_screened_metrics_Config_On_message = "//div[@data-testid='featureFormComponent-screenedMetrics']//div[contains(text(), 'This field is mandatory to ')]"
        self.Min_Num_Modal_Randomized_metrics_text_box = "//div[@data-testid='featureFormComponent-randomizedMetrics']//input[@name='randomizedMetrics']"
        self.Min_Num_Modal_Randomized_metrics_Config_On_message = "//div[@data-testid='featureFormComponent-randomizedMetrics']//div[contains(text(), 'This field is mandatory to ')]"
        self.Min_Num_Modal_description_1 = "//div[@class='Dialog-container MuiBox-root css-0']//span[contains(text(), 'Recruitment data')]"
        self.Min_Num_Modal_description_2 = "//div[@class='Dialog-container MuiBox-root css-0']//p[contains(text(), 'Provide general')]"
        self.Min_Num_Modal_description_3 = "//div[@class='Dialog-container MuiBox-root css-0']//p[contains(text(), 'Mandatory to save form')]"
        #Study overview modal
        self.Study_overview_Modal_Brief_overview_of_study_text_area = "//div[@data-testid='featureFormComponent-briefOverview']//textarea[@name='briefOverview']"
        self.Study_overview_Modal_Brief_overview_of_study_Config_on_message= "//div[@data-testid='featureFormComponent-briefOverview']//div[contains(text(), 'This field is mandatory to ')]"
        self.Study_overview_Modal_Description_of_the_Study_text_area = "//div[@data-testid='featureFormComponent-studyDescription']//textarea[@name='studyDescription']"
        self.Study_overview_Modal_Description_of_the_Study_Config_on_message= "//div[@data-testid='featureFormComponent-studyDescription']//div[contains(text(), 'This field is mandatory to ')]"
        self.Study_overview_Modal_description_1 = "//div[@class='Dialog-container MuiBox-root css-0']//span[contains(text(), 'Overview of study')]"
        self.Study_overview_Modal_description_2 = "//div[@class='Dialog-container MuiBox-root css-0']//p[contains(text(), 'Enter information that describes')]"
        self.Study_overview_Modal_description_3 = "//div[@class='Dialog-container MuiBox-root css-0']//p[contains(text(), 'Mandatory to save form')]"

        #comment section pop out
        self.Comment_button_pop_out_side_Panel = "//div[@class ='MuiBox-root css-13o7eu2']"
        self.Comment_side_panel_add_comment_text_Box = "//textarea[@name='comment']"
        self.Comment_side_panel_no_comments = "//div[@class='MuiBox-root css-am8j60']/p[contains(text(), 'No Comments Added')]"
        self.Comment_side_panel_submit_button = "//div[@class='MuiBox-root css-1d0psfv']/button"
        self.Comment_side_panel_word_count = "//div[@class='MuiBox-root css-d2oo9m']/p"
        self.Comment_side_panel_first_user= "//div[@class='feature-group MuiBox-root css-9qn5ji']/div/div/p"
        self.Comment_side_panel_first_comment = "//div[@class='feature-group MuiBox-root css-9qn5ji']/div/div/div/pre"
        self.Comment_side_panel_first_date = "(//div[@class='feature-group MuiBox-root css-9qn5ji']/div/div/div/div)[1]"
        

    def clickEditbuttonForCard(self, card : str):
        selectedCard = card.lower().strip('"').replace(" ", "-")
        self.page.locator("//div[@data-testid='general-"+ selectedCard + "-card']//button[@class='MuiTypography-root MuiTypography-inherit MuiLink-root MuiLink-underlineAlways MuiLink-button css-95lpad'][normalize-space()='Edit']").click()

    def verifyMinNumPatientModal(self):
        expect(self.page.locator(self.Min_Num_Modal_screened_metrics_text_box)).to_be_visible()
        expect(self.page.locator(self.Min_Num_Modal_screened_metrics_Config_On_message)).to_be_visible()
        expect(self.page.locator(self.Min_Num_Modal_screened_metrics_Config_On_message)).to_have_text("This field is mandatory to save form")
        expect(self.page.locator(self.Min_Num_Modal_Randomized_metrics_text_box)).to_be_visible()
        expect(self.page.locator(self.Min_Num_Modal_Randomized_metrics_Config_On_message)).to_be_visible()
        expect(self.page.locator(self.Min_Num_Modal_Randomized_metrics_Config_On_message)).to_have_text("This field is mandatory to save form")
        expect(self.page.locator(self.Min_Num_Modal_description_1)).to_be_visible()
        expect(self.page.locator(self.Min_Num_Modal_description_1)).to_have_text("Recruitment data")
        expect(self.page.locator(self.Min_Num_Modal_description_2)).to_be_visible()
        expect(self.page.locator(self.Min_Num_Modal_description_2)).to_have_text("Provide general details for the study.")
        expect(self.page.locator(self.Min_Num_Modal_description_3)).to_be_visible()
        expect(self.page.locator(self.Min_Num_Modal_description_3)).to_have_text("* Mandatory to save form ♦ Mandatory for configuration approval")
        expect(self.page.locator(self.Save_Button)).to_be_visible()
        expect(self.page.locator(self.Cancel_button)).to_be_visible()

    def verifyStudyOverviewModal(self):
        expect(self.page.locator(self.Study_overview_Modal_Brief_overview_of_study_text_area)).to_be_visible()
        expect(self.page.locator(self.Study_overview_Modal_Brief_overview_of_study_Config_on_message)).to_be_visible()
        expect(self.page.locator(self.Study_overview_Modal_Brief_overview_of_study_Config_on_message)).to_have_text("This field is mandatory to save form")
        expect(self.page.locator(self.Study_overview_Modal_Description_of_the_Study_text_area)).to_be_visible()
        expect(self.page.locator(self.Study_overview_Modal_Description_of_the_Study_Config_on_message)).to_be_visible()
        expect(self.page.locator(self.Study_overview_Modal_Description_of_the_Study_Config_on_message)).to_have_text("This field is mandatory to save form")
        expect(self.page.locator(self.Study_overview_Modal_description_1)).to_be_visible()
        expect(self.page.locator(self.Study_overview_Modal_description_1)).to_have_text("Overview of study")
        expect(self.page.locator(self.Study_overview_Modal_description_2)).to_be_visible()
        expect(self.page.locator(self.Study_overview_Modal_description_2)).to_have_text("Enter information that describes the overview of the study which will be displayed in Unify.")
        expect(self.page.locator(self.Study_overview_Modal_description_3)).to_be_visible()
        expect(self.page.locator(self.Study_overview_Modal_description_3)).to_have_text("* Mandatory to save form ♦ Mandatory for configuration approval")
        expect(self.page.locator(self.Save_Button)).to_be_visible()
        expect(self.page.locator(self.Cancel_button)).to_be_visible()

    def clickCommentPanel_button(self):
        self.page.locator(self.Comment_button_pop_out_side_Panel).click()

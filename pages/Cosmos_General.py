import time
from utils.wait_helpers import wait_and_click_element, wait_for_element


class GeneralFeaturePage():
    def __init__(self, page):
        self.page = page
        # Feature page locators
        self.general_tab = "//p[contains(text(), 'General')]"
        self.min_num_of_patients_edit_button = "(//button[contains(text(), 'Edit')])[1]"
        self.screened_metric_textbox = "//input[@name='screenedMetrics']"
        self.randomized_metric_textbox = "//input[@name='randomizedMetrics']"
        self.save_button = "//button[contains(text(), 'Save')]"
        self.study_overview_edit_button = "(//button[contains(text(), 'Edit')])[2]"
        self.brief_overview_study_text_area = "//textarea[@name='briefOverview']"
        self.description_of_study = "//textarea[@name='studyDescription']"

    def fill_out_general_feature(self):
        wait_and_click_element(self.page, self.general_tab)
        wait_and_click_element(self.page, self.min_num_of_patients_edit_button)
        wait_for_element(self.page, self.screened_metric_textbox)  # Ensure the textbox is visible
        self.page.fill(self.screened_metric_textbox, "26")
        self.page.fill(self.randomized_metric_textbox, "79")
        wait_and_click_element(self.page, self.save_button)

        time.sleep(1)  # Consider replacing this with a wait_for_element if necessary

        wait_and_click_element(self.page, self.study_overview_edit_button)
        wait_for_element(self.page, self.brief_overview_study_text_area)  # Ensure the text area is visible
        self.page.fill(self.brief_overview_study_text_area, "test1")
        self.page.fill(self.description_of_study, "test2")
        wait_and_click_element(self.page, self.save_button)

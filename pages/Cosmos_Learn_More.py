from utils.wait_helpers import wait_and_click_element, wait_for_element

class LearnMoreFeaturePage():
    def __init__(self, page):
        self.page = page
        self.learn_more_tab = "//p[contains(text(), 'Learn more')]"
        self.edit_button = "(//button[contains(text(), 'Edit')])[1]"
        self.occo_yes_button = "(//input[@value='Yes'])[1]"
        self.save_button = "(//button[contains(text(), 'Save')])[1]"
        self.close_button = "//button[contains(text(), 'Close')]"
        self.dcco_tab = "//button[@id='detailedComplianceComplianceOverview-1']"
        self.dcco_yes_button = "(//input[@value='Yes'])[3]"
        self.health_event_tab = "//button[@id='healthEvent-2']"
        self.health_event_yes_button = "(//input[@value='Yes'])[5]"
        self.health_event_ufcc_button = "(//input[@value='Use fallback content config'])[1]"
        self.symptom_notice_details_tab = "//button[@id='symptomNoticeDetails-3']"
        self.symptom_notice_details_yes_button = "(//input[@value='Yes'])[6]"
        self.symptom_notice_details_ufcc_button = "(//input[@value='Use fallback content config'])[2]"
        self.spirometry_section_tab = "//button[@id='spirometrySectionVisits-4']"
        self.spirometry_section_yes_button = "(//input[@value='Yes'])[7]"
        self.spirometry_section_ufcc_button = "(//input[@value='Use fallback content config'])[3]"

    def fill_learn_more_cards_partial_data(self):
        wait_and_click_element(self.page, self.learn_more_tab)
        wait_and_click_element(self.page, self.edit_button)

        wait_and_click_element(self.page, self.occo_yes_button)
        wait_and_click_element(self.page, self.save_button)

        wait_and_click_element(self.page, self.dcco_tab)
        wait_and_click_element(self.page, self.dcco_yes_button)
        wait_and_click_element(self.page, self.save_button)

        wait_and_click_element(self.page, self.health_event_tab)
        wait_and_click_element(self.page, self.health_event_yes_button)
        wait_and_click_element(self.page, self.save_button)

        wait_and_click_element(self.page, self.symptom_notice_details_tab)
        wait_and_click_element(self.page, self.symptom_notice_details_yes_button)
        wait_and_click_element(self.page, self.save_button)

        wait_and_click_element(self.page, self.spirometry_section_tab)
        wait_and_click_element(self.page, self.spirometry_section_yes_button)
        wait_and_click_element(self.page, self.save_button)

        wait_and_click_element(self.page, self.close_button)

    def fill_learn_more_cards_full_data(self):
        wait_and_click_element(self.page, self.learn_more_tab)
        wait_and_click_element(self.page, self.edit_button)

        wait_and_click_element(self.page, self.occo_yes_button)
        wait_and_click_element(self.page, self.save_button)

        wait_and_click_element(self.page, self.dcco_tab)
        wait_and_click_element(self.page, self.dcco_yes_button)
        wait_and_click_element(self.page, self.save_button)

        wait_and_click_element(self.page, self.health_event_tab)
        wait_and_click_element(self.page, self.health_event_yes_button)
        wait_and_click_element(self.page, self.health_event_ufcc_button)
        wait_and_click_element(self.page, self.save_button)

        wait_and_click_element(self.page, self.symptom_notice_details_tab)
        wait_and_click_element(self.page, self.symptom_notice_details_yes_button)
        wait_and_click_element(self.page, self.symptom_notice_details_ufcc_button)
        wait_and_click_element(self.page, self.save_button)

        wait_and_click_element(self.page, self.spirometry_section_tab)
        wait_and_click_element(self.page, self.spirometry_section_yes_button)
        wait_and_click_element(self.page, self.spirometry_section_ufcc_button)
        wait_and_click_element(self.page, self.save_button)

        wait_and_click_element(self.page, self.close_button)

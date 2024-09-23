import time
from playwright.sync_api import Page, expect
from utils.wait_helpers import wait_and_click_element, wait_for_element

class TechnicalSupportFAQsFeaturePage():
    def __init__(self, page):
        self.page = page
        # Locators stored directly as XPath strings
        self.technical_support_faqs_tab = "//p[contains(text(), 'Technical support FAQs')]"
        self.account_access_question_1 = "(//input[@type='checkbox'])[2]"
        self.account_access_question_2 = "(//input[@type='checkbox'])[3]"
        self.account_access_question_3 = "(//input[@type='checkbox'])[4]"
        self.account_access_question_3_adolescent = "(//input[@type='checkbox'])[5]"
        self.account_access_question_4 = "(//input[@type='checkbox'])[6]"
        self.account_access_question_5 = "(//input[@type='checkbox'])[7]"
        self.account_access_question_6 = "(//input[@type='checkbox'])[8]"
        self.activity_help_question_2_generic = "(//input[@type='checkbox'])[9]"
        self.activity_help_question_3_generic = "(//input[@type='checkbox'])[10]"
        self.activity_help_question_4 = "(//input[@type='checkbox'])[11]"
        self.activity_help_question_6 = "(//input[@type='checkbox'])[12]"
        self.activity_help_question_8 = "(//input[@type='checkbox'])[13]"
        self.activity_help_question_9 = "(//input[@type='checkbox'])[14]"
        self.activity_help_question_10_generic = "(//input[@type='checkbox'])[15]"
        self.phone_settings_question_1_wifi = "(//input[@type='checkbox'])[16]"
        self.phone_settings_question_1_cellular = "(//input[@type='checkbox'])[17]"
        self.phone_settings_question_2 = "(//input[@type='checkbox'])[18]"
        self.phone_settings_question_3 = "(//input[@type='checkbox'])[19]"
        self.phone_settings_question_4_generic = "(//input[@type='checkbox'])[20]"
        self.phone_settings_question_5_generic = "(//input[@type='checkbox'])[21]"
        self.phone_settings_question_6_generic = "(//input[@type='checkbox'])[22]"
        self.phone_settings_question_7_generic = "(//input[@type='checkbox'])[23]"
        self.using_unify_question_1 = "(//input[@type='checkbox'])[24]"
        self.using_unify_question_2_generic = "(//input[@type='checkbox'])[25]"
        self.using_unify_question_5 = "(//input[@type='checkbox'])[26]"
        self.using_unify_question_6 = "(//input[@type='checkbox'])[27]"
        self.using_unify_question_7 = "(//input[@type='checkbox'])[28]"
        self.using_unify_question_8 = "(//input[@type='checkbox'])[29]"
        self.using_unify_question_9 = "(//input[@type='checkbox'])[30]"
        self.using_unify_question_10 = "(//input[@type='checkbox'])[31]"
        self.using_unify_question_11 = "(//input[@type='checkbox'])[32]"
        self.using_unify_question_12 = "(//input[@type='checkbox'])[33]"
        self.using_unify_question_13 = "(//input[@type='checkbox'])[34]"
        self.using_unify_question_14 = "(//input[@type='checkbox'])[35]"
        self.using_unify_question_15 = "(//input[@type='checkbox'])[36]"
        self.using_unify_question_16 = "(//input[@type='checkbox'])[37]"
        self.using_unify_question_19 = "(//input[@type='checkbox'])[38]"
        self.using_unify_question_18 = "(//input[@type='checkbox'])[39]"
        self.using_unify_question_21 = "(//input[@type='checkbox'])[40]"
        self.using_unify_question_22 = "(//input[@type='checkbox'])[41]"
        self.using_unify_question_23 = "(//input[@type='checkbox'])[42]"
        self.using_unify_question_24 = "(//input[@type='checkbox'])[43]"
        self.using_unify_question_25 = "(//input[@type='checkbox'])[44]"

    def toggle_all_fields(self):
        wait_and_click_element(self.page, self.technical_support_faqs_tab)
        wait_and_click_element(self.page, self.account_access_question_1)
        wait_and_click_element(self.page, self.account_access_question_2)
        wait_and_click_element(self.page, self.account_access_question_3)
        wait_and_click_element(self.page, self.account_access_question_3_adolescent)
        wait_and_click_element(self.page, self.account_access_question_4)
        wait_and_click_element(self.page, self.account_access_question_5)
        wait_and_click_element(self.page, self.account_access_question_6)
        wait_and_click_element(self.page, self.activity_help_question_2_generic)
        wait_and_click_element(self.page, self.activity_help_question_3_generic)
        wait_and_click_element(self.page, self.activity_help_question_4)
        wait_and_click_element(self.page, self.activity_help_question_6)
        wait_and_click_element(self.page, self.activity_help_question_8)
        wait_and_click_element(self.page, self.activity_help_question_9)
        wait_and_click_element(self.page, self.activity_help_question_10_generic)
        wait_and_click_element(self.page, self.phone_settings_question_1_wifi)
        wait_and_click_element(self.page, self.phone_settings_question_1_cellular)
        wait_and_click_element(self.page, self.phone_settings_question_2)
        wait_and_click_element(self.page, self.phone_settings_question_3)
        wait_and_click_element(self.page, self.phone_settings_question_4_generic)
        wait_and_click_element(self.page, self.phone_settings_question_5_generic)
        wait_and_click_element(self.page, self.phone_settings_question_6_generic)
        wait_and_click_element(self.page, self.phone_settings_question_7_generic)
        wait_and_click_element(self.page, self.using_unify_question_1)
        wait_and_click_element(self.page, self.using_unify_question_2_generic)
        wait_and_click_element(self.page, self.using_unify_question_5)
        wait_and_click_element(self.page, self.using_unify_question_6)
        wait_and_click_element(self.page, self.using_unify_question_7)
        wait_and_click_element(self.page, self.using_unify_question_8)
        wait_and_click_element(self.page, self.using_unify_question_9)
        wait_and_click_element(self.page, self.using_unify_question_10)
        wait_and_click_element(self.page, self.using_unify_question_11)
        wait_and_click_element(self.page, self.using_unify_question_12)
        wait_and_click_element(self.page, self.using_unify_question_13)
        wait_and_click_element(self.page, self.using_unify_question_14)
        wait_and_click_element(self.page, self.using_unify_question_15)
        wait_and_click_element(self.page, self.using_unify_question_16)
        wait_and_click_element(self.page, self.using_unify_question_19)
        wait_and_click_element(self.page, self.using_unify_question_18)
        wait_and_click_element(self.page, self.using_unify_question_21)
        wait_and_click_element(self.page, self.using_unify_question_22)
        wait_and_click_element(self.page, self.using_unify_question_23)
        wait_and_click_element(self.page, self.using_unify_question_24)
        wait_and_click_element(self.page, self.using_unify_question_25)

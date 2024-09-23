import time
from utils.wait_helpers import wait_and_click_element, wait_for_element

class ContactSupportFeaturePage():
    def __init__(self, page):
        self.page = page
        # Feature page locators using specific XPaths
        self.contact_support_tab = "//p[contains(text(), 'Contact support')]"
        self.include_argentina = "((//div[@data-field='country']//p[text()='Argentina'])/preceding::input[@type='checkbox'][1])"
        self.include_australia = "((//div[@data-field='country']//p[text()='Australia'])/preceding::input[@type='checkbox'][1])"
        self.include_austria = "((//div[@data-field='country']//p[text()='Austria'])/preceding::input[@type='checkbox'][1])"
        self.include_belgium = "((//div[@data-field='country']//p[text()='Belgium'])/preceding::input[@type='checkbox'][1])"
        self.include_bulgaria = "((//div[@data-field='country']//p[text()='Bulgaria'])/preceding::input[@type='checkbox'][1])"
        self.include_brazil = "((//div[@data-field='country']//p[text()='Brazil'])/preceding::input[@type='checkbox'][1])"
        self.include_canada = "((//div[@data-field='country']//p[text()='Canada'])/preceding::input[@type='checkbox'][1])"
        self.include_china = "((//div[@data-field='country']//p[text()='China'])/preceding::input[@type='checkbox'][1])"
        self.include_czech_republic = "((//div[@data-field='country']//p[text()='Czech Republic'])/preceding::input[@type='checkbox'][1])"
        self.include_denmark = "((//div[@data-field='country']//p[text()='Denmark'])/preceding::input[@type='checkbox'][1])"
        self.include_france = "((//div[@data-field='country']//p[text()='France'])/preceding::input[@type='checkbox'][1])"
        self.include_germany = "((//div[@data-field='country']//p[text()='Germany'])/preceding::input[@type='checkbox'][1])"
        self.include_great_britain = "((//div[@data-field='country']//p[text()='Great Britain'])/preceding::input[@type='checkbox'][1])"
        self.include_hungary = "((//div[@data-field='country']//p[text()='Hungary'])/preceding::input[@type='checkbox'][1])"
        self.include_israel = "((//div[@data-field='country']//p[text()='Israel'])/preceding::input[@type='checkbox'][1])"
        self.include_italy = "((//div[@data-field='country']//p[text()='Italy'])/preceding::input[@type='checkbox'][1])"
        self.include_japan = "((//div[@data-field='country']//p[text()='Japan'])/preceding::input[@type='checkbox'][1])"
        self.include_mexico = "((//div[@data-field='country']//p[text()='Mexico'])/preceding::input[@type='checkbox'][1])"
        self.include_netherlands = "((//div[@data-field='country']//p[text()='Netherlands'])/preceding::input[@type='checkbox'][1])"
        self.include_peru = "((//div[@data-field='country']//p[text()='Peru'])/preceding::input[@type='checkbox'][1])"
        self.include_poland = "((//div[@data-field='country']//p[text()='Poland'])/preceding::input[@type='checkbox'][1])"
        self.include_russian_federation = "((//div[@data-field='country']//p[text()='Russian Federation'])/preceding::input[@type='checkbox'][1])"
        self.include_slovakia = "((//div[@data-field='country']//p[text()='Slovakia'])/preceding::input[@type='checkbox'][1])"
        self.include_spain = "((//div[@data-field='country']//p[text()='Spain'])/preceding::input[@type='checkbox'][1])"
        self.include_sweden = "((//div[@data-field='country']//p[text()='Sweden'])/preceding::input[@type='checkbox'][1])"
        self.include_switzerland = "((//div[@data-field='country']//p[text()='Switzerland'])/preceding::input[@type='checkbox'][1])"
        self.include_taiwan = "((//div[@data-field='country']//p[text()='Taiwan'])/preceding::input[@type='checkbox'][1])"
        self.include_ukraine = "((//div[@data-field='country']//p[text()='Ukraine'])/preceding::input[@type='checkbox'][1])"
        self.include_united_states = "((//div[@data-field='country']//p[text()='United States'])/preceding::input[@type='checkbox'][1])"
        self.include_vietnam = "((//div[@data-field='country']//p[text()='Vietnam'])/preceding::input[@type='checkbox'][1])"

    def toggle_all_fields(self):
        wait_and_click_element(self.page, self.contact_support_tab)

        # List of locators for each checkbox
        checkboxes = [
            self.include_argentina,
            self.include_australia,
            self.include_austria,
            self.include_belgium,
            self.include_bulgaria,
            self.include_brazil,
            self.include_canada,
            self.include_china,
            self.include_czech_republic,
            self.include_denmark,
            self.include_france,
            self.include_germany,
            self.include_great_britain,
            self.include_hungary,
            self.include_israel,
            self.include_italy,
            self.include_japan,
            self.include_mexico,
            self.include_netherlands,
            self.include_peru,
            self.include_poland,
            self.include_russian_federation,
            self.include_slovakia,
            self.include_spain,
            self.include_sweden,
            self.include_switzerland,
            self.include_taiwan,
            self.include_ukraine,
            self.include_united_states,
            self.include_vietnam,
        ]

        # Toggle each checkbox
        for checkbox in checkboxes:
            wait_and_click_element(self.page, checkbox)


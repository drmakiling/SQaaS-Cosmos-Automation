import re, time
from playwright.sync_api import Page, expect
from pages.Cosmos_Main import Cosmos_Main
from pages.Heroku_File_Download import Heroku_File_Download_Page
from pages.Heroku_File_Upload import Heroku_File_Upload_Page
from pages.common_Login import Cosmos_Login_Page
from pages.Cosmos_Country import Cosmos_Country


def test_verify_a_file_is_downloaded(page: Page):
    main_page = Cosmos_Main(page)
    main_page.navigate_to_main_page()
    main_page.navigate_to_page("File Download Link")

    download_page = Heroku_File_Download_Page(page)
    time.sleep(2)
    download_page.click_on_download_link()
    time.sleep(2)
    download_page.verify_file_is_downloaded()


def test_verify_a_file_is_uploaded(page: Page):
    main_page = Cosmos_Main(page)
    main_page.navigate_to_main_page()
    main_page.navigate_to_page("File Upload Link")

    upload_page = Heroku_File_Upload_Page(page)
    time.sleep(2)
    upload_page.click_on_upload_link("UploadTextFile.txt")
    time.sleep(2)
    upload_page.verify_file_is_uploaded()


def test_verify_user_is_able_to_login(page: Page):
    main_page = Cosmos_Main(page)
    main_page.navigate_to_main_page()
    main_page.navigate_to_page("Basic Auth link")

    login_page = Cosmos_Login_Page(page)
    time.sleep(2)
    login_page.login_to_page()
    time.sleep(2)
    login_page.verify_login_is_successful()


def test_verify_user_opens_new_window(page: Page):
    main_page = Cosmos_Main(page)
    main_page.navigate_to_main_page()
    main_page.navigate_to_page("Multiple Windows link")

    multiple_pages = Cosmos_Country(page)
    multiple_pages.click_and_navigate_to_new_page()
    multiple_pages.verify_text_in_new_window()


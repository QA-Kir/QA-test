from playwright.sync_api import Page, expect
from config import *

def test_login_page(page: Page):
    page.goto(url_demo_playwright)
    page.fill('input#input-username', 'demo')
    page.fill('input#input-password', 'demo')
    page.click('button[type=submit]')
    #page.click('button:text("Login")')
    #page.wait_for_timeout(10000)
    page.wait_for_load_state('load')
    expect(page.get_by_role("heading", name="Dashboard")).to_be_visible()

#HW case (v1)
def test_google_search(page: Page):
    page.goto('https://www.google.com')
    page.get_by_label('Найти').fill('Playwright Python')
    page.click('.gNO89b')

#HW case (v2)
def test_google_search_2(page: Page):
    page.goto('https://www.google.com')
    page.fill('#APjFqb', 'Playwright Python')
    page.press('input', 'Enter')


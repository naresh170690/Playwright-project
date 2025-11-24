import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://practicetestautomation.com/practice-test-login/")
    page.get_by_role("textbox", name="Username").click()
    page.get_by_role("textbox", name="Username").fill("student", delay=100)
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").fill("Password123", delay=100)
    page.get_by_role("button", name="Submit").click()
    try :
        page.get_by_text("Logged In Successfully").wait_for(timeout=3000)
        print("Login successful")   
    except Exception:
        print("Login failed")   
    
    page.get_by_role("link", name="Log out").click()
    expect(page.get_by_role("textbox", name="Username")).to_be_visible()
    expect(page.get_by_role("textbox", name="Password")).to_be_visible()
    expect(page.get_by_role("button", name="Submit")).to_be_visible()

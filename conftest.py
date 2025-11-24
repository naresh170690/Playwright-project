import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()

@pytest.fixture
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()


    """
    This gives every test a fresh page object using chromium browser.
    
    Here the fixure Browser:
    - Launches the browser at the start of the test session.
    - Closes the browser at the end of the test session.    
    The fixture Page:
    - Creates a new browser context for each test.  
    - Provides a new page object for each test.
    - Closes the context after each test to ensure isolation.   
       
    """
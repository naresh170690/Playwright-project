import os, re, time
from playwright.sync_api import expect


def test_google_search(page):

    # Set Accept-Language header before navigation
    page.set_extra_http_headers({"Accept-Language": "en-US,en;q=0.9"})

    # Navigate to Google 
    page.goto("https://www.google.co.in/ncr")

    try:
        page.get_by_role("button", name="Accept all").click(timeout=3000)
        print("Popup is accepted")
    except Exception:
        print("No popup to accept")
        
# Use human-like typing with a small delay instead of instant fill
    page.get_by_role("combobox", name="Search").click()
    page.get_by_role("combobox", name="Search").type("Playwright", delay=100)  # 100ms per char
    page.keyboard.press("Enter")

    # Wait for results to load
    page.wait_for_timeout(5000)
    
    # Verify the title contains "Playwright"    
    expect(page).to_have_title(re.compile("playwright", re.IGNORECASE))





from playwright.sync_api import sync_playwright

with sync_playwright() as p:
   browser = p.chromium.launch(headless=False)
   page = browser.new_page()
   page.goto('https://google.com')
   print( page.url)
   print(page.title())
   page.wait_for_timeout(5000)  # Wait for 3 seconds to see the browser
   browser.close()
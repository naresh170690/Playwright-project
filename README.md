<!--
Project: Playright-project — Playwright Python test suite for Google.

Summary:
- Contains a simple automated test (tests/test_google.py) that opens https://www.google.com,
    asserts the page title contains "Google", and verifies the main search input is present.

Quick setup (PowerShell workflow shown as an example):
1. Create and activate a virtual environment (recommended).
2. Install dependencies from requirements.txt using pip.
3. Install Playwright browsers so tests can run headless or headed.
4. Execute the test suite with pytest.

Notes:
- Ensure Python and pip are installed on the system.
- Run the Playwright browser installation step at least once after adding the dependency.
- Tests are located in the tests/ directory and rely on Playwright's Python bindings.
-->
# Playright-project
Playright project

## Playwright test for Google

Quick instructions to run the Playwright Python test added in `tests/test_google.py`:

1. Create and activate a virtual environment (recommended):

	- Windows PowerShell:

	  ```powershell
	  python -m venv .venv; .\.venv\Scripts\Activate.ps1
	  ```

2. Install dependencies:

	```powershell
	python -m pip install -r requirements.txt
	```

3. Install Playwright browsers:

	```powershell
	python -m playwright install
	```

4. Run the test with `pytest`:

	```powershell
	pytest -q
	```

The test opens `https://www.google.com`, verifies the page title contains "Google", and checks that the main search input exists.

### Tutorial - 3 

What is a test in Pytest
A test is just a function whose name starts with test_
Pytest automatically finds and runs these functions

--

Write a pytest function line by line
Step 1 - In your project create a folder named: tests
Step 2 - Inside tests folder create a file test_google.py
Step 3 - Start writing a simple test line by line

Step 4 - Add import statements

import re
from playwright.sync_api import expect

Step 5 - Write the test function

def test_google_search(page):

Step 6 - Navigate to Google (and skip the "Before you proceed" screen)

page.goto("https://www.google.com/ncr")

Step 7 - Handle the “Accept All” popup (optional)

   try:
       page.get_by_role("button", name="Accept all").click(timeout=3000)
   except:
       print("No popup")

Step 8 - Type in the Search Box

page.get_by_role("combobox", name="Search").fill("Playwright Python")

Step 9 - Press Enter to search

page.keyboard.press("Enter")

Step 10 - Verify the page title contains the word "Playwright"

expect(page).to_have_title(re.compile("Playwright", re.IGNORECASE))

Step 11 - Run and verify   pytest tests/test_google.py
Select browser    
--browser=chromium (includes Chrome/Edge)
--browser=firefox
--browser=webkit   (Safari engine)

Headed or Headless Mode 
--headed
--headless

Capture Screenshots   
--screenshot=on off (default)
on
only-on-failure 

Record Video     
--video=on  off (default)
Retain-on-failure
On-first-retry

Can also generate html file after installing pytest-html and add option --html=report.html
pip install pytest-html

Check all options   pytest --help





### Tutorial - 4
In this session…
Create Project Structure
Add Folders and Files
Run and verify

DEMO - Create Project Structure
Step 1 - Check the required libraries are installed pip list
playwright, pytest, pytest-playwright, pytest-html
--
Step 2 - On cmd goto your root project folder   
cd playwright_pytest_project
--
Step 3 - Create sub-folders  mkdir tests pages utils reports
--
Step 4 - Create and edit conftest.py in root touch conftest.py

Imagine you are testing 10 different websites
Without conftest.py, you'd need to write this same code in every test file:
That’s repeating code and not good practice. 😖
With conftest.py  we define that once as a fixture and just use it in tests

A fixture is a reusable piece of code that sets something up before a test runs, and can clean it up afterward
-
Step 5 - Keep all test files inside tests folder
--
Step 6 -  Create pytest.ini in root and add options

pytest.ini is a configuration file used by pytest to control how your tests run — without having to type long command-line options again and again
Run tests simply with: pytest
No need to pass all options manually every time!

[pytest]
addopts = --headed --browser chromium --html=reports/report.html --self-contained-html
testpaths = tests --slowmo=200

This auto-sets:
headful mode
Chromium browser
generates HTML report

--

Step 7 - (OPTIONAL) Create a requirements.txt So others can install your packages easily
pip freeze ＞ requirements.txt

Now in a new project we can use this file to install everything  pip install -r requirements.txt

Step 8 - Run your project  pytest
-

Project Structure
We’ll make a clean Playwright + Pytest framework structure using:
tests/    → where test scripts go
pages/    → for Page Object Model (optional but useful)
conftest.py → for setting up browser fixtures
pytest.ini    → for config
utils/    → for helpers (if needed)
Reports/screenshots/logs (auto-generated)-



### Tutorial - 5
DEMO - How to record in Playwright
Prerequisites Playwright and Playwright browsers are already installed in your project
pip install playwright  playwright install

Step 1 - Open terminal and goto your project location

Step 2 - Run command playwright codegen https://www.google.com
 This opens a browser and a Playwright Inspector window side by side

Step 3 - Record your actions and save the script  
To Stop - Press ctrl+C on terminal or close inspector and browser window

Step 4 - OPTIONAL - To record and save code directly into a file
playwright codegen https://example.com --target python -o my_test_script.py


### tutorial - 6
Without POM
Objects are not reusable
Changes and maintenance is hard and manual
Code is not very clean and readable
-

What is the POM (Page Object Model)
POM (Page Object Model) is a design pattern used in test automation
It helps you write clean, reusable, and maintainable test code

Each webpage = One class (e.g., LoginPage, HomePage)

That class contains:
Locators: How to find elements on the page (like buttons, inputs)
Actions: What you can do (click, type, select, etc.)

How it Helps
Reusability Readability Maintainability  Clean Code

-

DEMO - How to implement Page Object Model

Step 1 - Under pages folder create file page_google.py
Step 2 - In the file create a page class
Step 3 - Inside the class create a constructor function
Step 4 - Now add locators for all the objects that you want to use in your tests on this page
Step 5 - Add action methods to do action on these objects
Step 6 - Now use this class in your test and upage scripts to use page class methods
Step 7 - Save and Run -
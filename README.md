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


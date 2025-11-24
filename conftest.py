import os
import pytest


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Hook to capture a screenshot when a test using the `page` fixture fails.

    Saves screenshots to a `screenshots/` directory in the repo root with
    a filename containing the test name and phase.
    """
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        page = item.funcargs.get("page")
        if page:
            screenshots_dir = os.path.join(os.getcwd(), "screenshots")
            os.makedirs(screenshots_dir, exist_ok=True)
            # Use a deterministic name for easy lookup
            fname = f"{item.name}.png"
            path = os.path.join(screenshots_dir, fname)
            try:
                page.screenshot(path=path, full_page=True)
                # Make the path visible in pytest output
                print(f"\nSaved screenshot: {path}")
            except Exception as exc:
                print(f"Failed to save screenshot: {exc}")

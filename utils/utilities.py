import os
import shutil
from datetime import datetime
import glob


# Constants
TIMESTAMP = datetime.now().strftime("%Y%m%d_%H%M%S")
SCREENSHOT_DIR = os.path.join(os.getcwd(), "reports", "screenshots", TIMESTAMP)

# Ensure the screenshots directory exists
if not os.path.exists(SCREENSHOT_DIR):
    os.makedirs(SCREENSHOT_DIR)


def capture_screenshot(context, step):
    """Capture a screenshot if the step fails."""
    if step.status == 'failed':
        # Create a screenshot filename with a timestamp and step name
        screenshot_name = f"{TIMESTAMP}_{step.name}.png"
        screenshot_path = os.path.join(context.screenshot_folder, screenshot_name)

        # Ensure the screenshots directory exists (just in case)
        if not os.path.exists(context.screenshot_folder):
            os.makedirs(context.screenshot_folder)

        # Take a screenshot using Playwright
        context.page.screenshot(path=screenshot_path)

        # Get the absolute path for the screenshot
        full_screenshot_path = os.path.abspath(screenshot_path)

        # Print the full path of the screenshot
        print(f"Screenshot saved to: {full_screenshot_path}")


def clean_old_screenshot_folders(max_folders=5):
    """Clean up old screenshot folders, keeping only the latest `max_folders`."""
    screenshot_base_dir = os.path.join(os.getcwd(), "reports", "screenshots")

    # Get a list of folders in the screenshots directory, sorted by creation time
    folders = sorted(
        (f for f in os.listdir(screenshot_base_dir) if os.path.isdir(os.path.join(screenshot_base_dir, f))),
        key=lambda f: os.path.getctime(os.path.join(screenshot_base_dir, f))
    )

    # Delete older folders if more than max_folders exist
    while len(folders) > max_folders:
        folder_to_delete = folders.pop(0)
        shutil.rmtree(os.path.join(screenshot_base_dir, folder_to_delete))


def delete_old_reports(directory, file_pattern="behave_report_*.html", max_reports=5):
    """
    Deletes older reports in the specified directory if they exceed the maximum allowed.
    """
    # Get a list of all report files matching the pattern
    reports = glob.glob(os.path.join(directory, file_pattern))

    # Sort by modification time (most recent last)
    reports.sort(key=os.path.getmtime, reverse=True)

    # If there are more reports than the max allowed, delete the oldest ones
    if len(reports) > max_reports:
        for report in reports[max_reports:]:
            os.remove(report)
            print(f"Deleted old report: {report}")

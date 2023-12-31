# utils/combine_allure.py
import os
import argparse
import shutil
from datetime import datetime
from pytz import timezone
from allure_combine import combine_allure

parser = argparse.ArgumentParser(description="Name for filename terminal")
parser.add_argument(
    "--name",
    metavar="name",
    type=str,
    help="the part of the filename after the current time",
    default="allure-report",
)
args = parser.parse_args()


root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
allure_report_dir = f"{root_dir}/allure-report"

combine_allure(
    allure_report_dir,
    dest_folder=f"{allure_report_dir}/single-page",
    auto_create_folders=True,
    remove_temp_files=True,
    ignore_utf8_errors=False,
)

now_utc = datetime.now(timezone("UTC"))
now_pdt = now_utc.astimezone(timezone("US/Pacific"))
curr_time_pdt = now_pdt.strftime("%Y-%m-%d_%Hh-%Mm")

# Rename the generated 'complete.html'
new_dirname = "single-page"
new_filename = f"{curr_time_pdt}-{args.name}.html"
print("Renaming file...")
old_file = os.path.join(allure_report_dir, new_dirname, "complete.html")
new_file = os.path.join(allure_report_dir, new_dirname, new_filename)

if os.path.exists(old_file):
    shutil.move(old_file, new_file)
else:
    print("old_file path doesn't exist")

print("File renamed successfully!")
print(f"New allure report filename: {allure_report_dir}/{new_filename}")

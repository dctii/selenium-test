# utils/combine_allure.py
import logging
import os
from allure_combine import combine_allure
import shutil

root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
allure_report_dir = f"{root_dir}/allure-report"

combine_allure(
    allure_report_dir,
    dest_folder=f"{allure_report_dir}/single-page",
    auto_create_folders=True,
    remove_temp_files=True,
    ignore_utf8_errors=False,
)

# Rename the generated index.html to single-page.html
new_dirname = "single-page"
new_filename = "single-page.html"
print("Renaming file...")
old_file = os.path.join(allure_report_dir, new_dirname, "complete.html")
new_file = os.path.join(allure_report_dir, new_dirname, new_filename)

if os.path.exists(old_file):
    shutil.move(old_file, new_file)
else:
    print("old_file path doesn't exist")

print("File renamed successfully!")
print(f"New allure report filename: {allure_report_dir}/{new_filename}")

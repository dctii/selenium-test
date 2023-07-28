from allure_combine import combine_allure
from utils.dirs import get_root_dir

root_dir = get_root_dir(__file__)
allure_report_dir = f"{root_dir}/allure-report"

combine_allure(
    allure_report_dir,
    dest_folder=f"{allure_report_dir}/single-page",
    auto_create_folders=True,
    remove_temp_files=True,
    ignore_utf8_errors=False,
)
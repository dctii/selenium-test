import os
import argparse
import datetime
import pytz

root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

parser = argparse.ArgumentParser(description="Process email template")
parser.add_argument(
    "OutputFileDest",
    metavar="outputfile_dest",
    type=str,
    help="the output file destination",
    default="email.html",
    nargs="?",
)
args = parser.parse_args()

now = datetime.datetime.now(tz=pytz.utc)
now_pdt = now.astimezone(pytz.timezone("US/Pacific"))
curr_date = now_pdt.strftime("%A, %B %d %Y")
curr_time = now_pdt.strftime("%I:%M %p PDT")

replacements = {
    "{{{ email.BODY_TITLE }}}": os.environ["EMAIL_HTML_BODY_TITLE"],
    "{{{ email.CURR_DATE }}}": curr_date,
    "{{{ email.CURR_TIME }}}": curr_time,
    "{{{ email.GH_REPO_NAME }}}": os.environ["GH_REPO_NAME"],
    "{{{ email.GH_WORKFLOW_NAME }}}": os.environ["GH_WORKFLOW_NAME"],
    "{{{ email.GH_WORKFLOW_ID }}}": os.environ["GH_WORKFLOW_ID"],
    "{{{ email.GH_WORKFLOW_URL }}}": os.environ["GH_WORKFLOW_URL"],
    "{{{ email.REPORT_ARTIFACT_NAME }}}": os.environ["REPORT_ARTIFACT_NAME"],
    "{{{ email.BDD_STDOUT }}}": open(os.environ["BDD_STDOUT"], "r").read(),
}

# replacements = {
#     "{{{ email.BODY_TITLE }}}": "REPORT_ARTIFACT_NAME_HERE",
#     "{{{ email.WORKFLOW_URL }}}": "REPORT_ARTIFACT_NAME_HERE",
#     "{{{ email.REPORT_ARTIFACT_NAME }}}": "REPORT_ARTIFACT_NAME_HERE",
#     "{{{ email.BDD_STDOUT }}}": open(f"{root_dir}/requirements.txt", "r").read(),
# }

with open(f"{root_dir}/utils/email_template.html", "r") as file:
    html = file.read()

for placeholder, replacement in replacements.items():
    html = html.replace(placeholder, replacement)

with open(args.OutputFileDest, "w") as file:
    file.write(html)

import os
import argparse

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

replacements = {
    "{{{ email.BODY_TITLE }}}": os.environ["BODY_TITLE"],
    "{{{ email.WORKFLOW_URL }}}": os.environ["WORKFLOW_URL"],
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

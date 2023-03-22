# Imports
import os
from rich.panel import Panel
from rich.markdown import Markdown
from settings import PATH_CSV, PATH_EXP, CSV_FILES, console
from logic.csv_logic import create_csv_folder, create_csv
from logic.process_logic import proces_args
from logic.parser_logic import args
from md import md


# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"


# Your code below this line.


# START PROGRAM


def main():
    # Check and/or create CSV files
    isExist = os.path.exists(PATH_CSV)
    if not isExist:
        create_csv_folder(PATH_CSV)
        create_csv(CSV_FILES)

    # Check and/or create Export folder
    isExist = os.path.exists(PATH_EXP)
    if not isExist:
        create_csv_folder(PATH_EXP)

    # Proceed commentline input by the args-parser
    proces_args(args)

    # print the start screen of only Superpy.py is called
    if args.command == None:
        panel_md = Panel.fit(Markdown(md), title="SUPERPY")
        console.print(panel_md)


# --------------------------------------#
if __name__ == "__main__":
    main()

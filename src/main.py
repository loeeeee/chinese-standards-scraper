import re
import os
import yaml
import json
import helper
from logger import Logger
from config import Config
import putty_knife
import pasa

def main():
    RESULT_PATH = os.path.join(Config.config["package root path"], "result")
    helper.create_folder_if_not_exists(RESULT_PATH)

    # Get the page source
    Logger.info(f"Search for {Config.config['search keywords']}")
    page_source = putty_knife.scraping(Config.config["search keywords"])

    # with open(os.path.join(RESULT_PATH, "result.html"), "w", encoding="utf-8") as f:
    #     f.writelines(page_source)

    # Parse the page source
    table_source = pasa.parsing(page_source)


if __name__ == "__main__":
    main()
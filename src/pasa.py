from bs4 import BeautifulSoup
from logger import Logger
from config import Config
import os

def parsing(page_source: str):
    soup = BeautifulSoup(page_source, "html.parser")

    table_of_standards = soup.find(id="gbtable")

    return table_of_standards

def main():
    RESULT_PATH = os.path.join(Config.config["package root path"], "result")
    Logger.debug(f"Result path is {RESULT_PATH}")

    with open(os.path.join(RESULT_PATH, "result.html"), "r", encoding="utf-8") as f:
        page_source = f.read()
    Logger.debug("Read result.html")

    Logger.debug("Start parsing")
    result = parsing(page_source)
    Logger.debug("Finish parsing")

    with open(os.path.join(RESULT_PATH, "table.html"), "w", encoding="utf-8") as f:
        f.writelines(result.prettify())
    Logger.debug("Write to table.html")

if __name__ == "__main__":
    Logger.info("Paser in demo mode, working on result/result.html")
    main()
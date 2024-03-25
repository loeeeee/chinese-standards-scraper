from logger import Logger

from selenium import webdriver
from selenium.webdriver import FirefoxOptions

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

def scraping(keyword: str) -> str:
    opts = FirefoxOptions()
    opts.add_argument("--headless")
    Logger.debug("Set CLI arguments.")

    driver = webdriver.Firefox(options=opts)
    Logger.debug("Started webdriver.")
    # Step # | name | target | value
    # 1 | open | /gb/gbQuery | 
    driver.get("https://std.samr.gov.cn/gb/gbQuery")
    Logger.debug("Got page.")
    # 2 | click | id=keyword2 | 
    driver.find_element(By.ID, "keyword2").click()
    # 3 | type | id=keyword2 | 人工智能
    driver.find_element(By.ID, "keyword2").send_keys(keyword)
    # 4 | sendKeys | id=keyword2 | ${KEY_ENTER}
    driver.find_element(By.ID, "keyword2").send_keys(Keys.ENTER)

    Logger.debug("Start waiting")
    WebDriverWait(driver, 10).until(
            EC.invisibility_of_element((By.CLASS_NAME, "fixed-table-loading"))
        )
    Logger.debug("Finish waiting")

    driver.save_full_page_screenshot("screenshot.png")
    Logger.debug("Got screenshot")

    Logger.debug("Got source")
    page_source = driver.page_source

    driver.close()
    driver.quit()
    Logger.debug("Stopped driver.")

    return page_source
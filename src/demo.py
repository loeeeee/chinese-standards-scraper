import yaml
import json
import helper
from logger import Logger
from config import Config

from selenium import webdriver
from selenium.webdriver import FirefoxOptions

opts = FirefoxOptions()
opts.add_argument("--headless")
Logger.info("Set CLI arguments.")

browser = webdriver.Firefox(options=opts)
Logger.info("Started webdriver.")
browser.get("https://www.baidu.com")
browser.implicitly_wait(2)
Logger.info("Got page.")
browser.save_full_page_screenshot("screenshot.png")
Logger.info("Got screenshot.")
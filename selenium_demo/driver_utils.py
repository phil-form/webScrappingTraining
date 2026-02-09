from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def build_chrome_options(headless=True):
    # Build Chrome options with safe defaults.
    options = ChromeOptions()
    if headless:
        options.add_argument('--headless=new')
    options.add_argument('--disable-gpu')
    options.add_argument('--window-size=1280,800')
    return options


def build_firefox_options(headless=True):
    # Build Firefox options with safe defaults.
    options = FirefoxOptions()
    if headless:
        options.add_argument('-headless')
    return options


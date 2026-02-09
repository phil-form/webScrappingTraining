import os
from selenium import webdriver
from selenium.webdriver.common.by import By

from driver_utils import build_chrome_options, build_firefox_options


def main():
    # Choose browser via env var: BROWSER=chrome or BROWSER=firefox.
    browser = os.getenv('BROWSER', 'chrome').lower()

    if browser == 'firefox':
        options = build_firefox_options(headless=True)
        driver = webdriver.Firefox(options=options)
    else:
        options = build_chrome_options(headless=True)
        driver = webdriver.Chrome(options=options)

    try:
        # Navigate to a stable demo site.
        driver.get('https://example.com/')
        print('title:', driver.title)
        heading = driver.find_element(By.CSS_SELECTOR, 'h1')
        print('h1:', heading.text)
        driver.save_screenshot('example_headless.png')
    finally:
        driver.quit()


if __name__ == '__main__':
    main()


import unittest

from selenium_demo.driver_utils import build_chrome_options, build_firefox_options


class SeleniumUtilsTests(unittest.TestCase):
    def test_chrome_options_headless(self):
        options = build_chrome_options(headless=True)
        args = options.arguments
        self.assertIn('--headless=new', args)

    def test_firefox_options_headless(self):
        options = build_firefox_options(headless=True)
        args = options.arguments
        self.assertIn('-headless', args)

    def test_chrome_options_no_headless(self):
        options = build_chrome_options(headless=False)
        args = options.arguments
        self.assertNotIn('--headless=new', args)


if __name__ == '__main__':
    unittest.main()


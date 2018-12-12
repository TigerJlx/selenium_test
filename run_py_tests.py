import unittest, time
from selenium import webdriver


class TestClass(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.base_url = "http://www.baidu.com"

    def tearDown(self):
        time.sleep(5)
        self.driver.quit()

    def test_case(self):
        self.driver.get(self.base_url)

if __name__ == '__main__':
    unittest.main()

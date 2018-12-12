import unittest, time
from selenium import webdriver


class TestClass(unittest.TestCase):
    def setUp(self):
        print(123456)
        self.driver = webdriver.Chrome()
        self.base_url = "http://www.baidu.com"

    def tearDown(self):
        time.sleep(6)
        self.driver.quit()

    def test_case(self):
        self.driver.get(self.base_url)

if __name__ == '__main__':
    unittest.main()

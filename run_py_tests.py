import unittest, time
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestClass(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.base_url = "http://127.0.0.1:5000/auth/login"

    def tearDown(self):
        time.sleep(6)
        self.driver.quit()

    def test_case(self):
        self.driver.get(self.base_url)
        time.sleep(2)
        self.driver.find_element(By.ID, "email").send_keys("2274701670@qq.com")
        self.driver.find_element(By.ID, "password").send_keys("123456")
        time.sleep(2)
        self.driver.find_element(By.ID, "submit").click()

    def test_case2(self):
        self.driver.get(self.base_url)
        time.sleep(2)
        self.driver.find_element(By.ID, "email").send_keys("888@163.com")
        self.driver.find_element(By.ID, "password").send_keys("666")
        time.sleep(2)
        self.driver.find_element(By.ID, "submit").click()


if __name__ == '__main__':
    unittest.main()

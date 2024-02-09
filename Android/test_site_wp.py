from selenium.webdriver.common.by import By
from time import sleep
import pytest


@pytest.mark.usefixtures('setup_method')
class TestAndLogin002:
    def test_site(self):
        sleep(5)
        self.driver.find_element(By.XPATH,
                                 "//android.widget.LinearLayout[@resource-id='org.wordpress.android:id/layout_container']/android.widget.LinearLayout/android.widget.LinearLayout").click()
        sleep(10)
        self.driver.find_element(By.ID, "org.wordpress.android:id/fab_button").click()
        sleep(5)
        self.driver.find_element(By.XPATH, "//android.widget.TextView[@text='Blog post']").click()
        sleep(5)
        self.driver.find_element(By.XPATH, "//android.widget.EditText[@content-desc='Post title. Empty']").send_keys(
            'My first blog')
        sleep(5)
        self.driver.find_element(By.XPATH, "//android.widget.EditText[@text='Start writing…']").send_keys(
            'This is my first blog im writing..')
        sleep(5)
        self.driver.find_element(By.XPATH, "//android.widget.TextView[@text='PUBLISH']").click()

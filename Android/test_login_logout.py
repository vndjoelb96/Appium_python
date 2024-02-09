from appium.options.android import UiAutomator2Options
from appium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import pytest


@pytest.mark.usefixtures('setup_method')
class TestAndLogin001:
    # Options are only available since client version 2.3.0
    # If you use an older client then switch to desired_capabilities
    # instead: https://github.com/appium/python-client/pull/720

    def test_login(self):
        self.driver.find_element(By.XPATH,
                                 "//android.widget.TextView[@text='Log in or sign up with WordPress.com']").click()
        sleep(5)
        self.driver.find_element(By.ID, "org.wordpress.android:id/continue_with_google").click()
        sleep(10)
        self.driver.find_element(By.ID, "com.google.android.gms:id/account_display_name").click()
        sleep(10)
        # verify add new site button
        site_button = self.driver.find_element(By.ID, "org.wordpress.android:id/button").text
        assert site_button == 'Add new site'

    def test_logout(self):
        self.driver.find_element(By.XPATH, "//android.widget.TextView[@text='Me']").click()

        sleep(5)
        self.driver.find_element(By.ID, "org.wordpress.android:id/row_logout").click()
        sleep(5)
        self.driver.find_element(By.XPATH, "//android.widget.Button[@resource-id='android:id/button1']").click()
        sleep(10)
        assert self.driver.find_element(By.XPATH,
                                        "//android.widget.TextView[@text='Log in or sign up with WordPress.com']").text == 'Log in or sign up with WordPress.com'

    # def teardown_method(self):
    # self.driver.quit()

from selenium.webdriver.common.by import By
from time import sleep
import pytest


@pytest.mark.usefixtures('setup_method')
class TestAndLogin003:
    def test_and_post(self):
        self.driver.find_element(By.ID, 'fab_button').click()
        sleep(2)
        self.driver.find_element(By.XPATH, '//android.widget.TextView[@text="Blog post"]').click()
        sleep(2)
        self.driver.find_element(By.XPATH, '//android.widget.EditText[@index=0]').click()
        sleep(2)
        self.driver.find_element(By.XPATH, '//android.widget.EditText[@index=0]').send_keys('hello world')
        sleep(2)
        self.driver.find_element(By.ID, 'menu_primary_action').click()
        sleep(2)
        self.driver.find_element(By.XPATH, '//android.widget.Button[@text="PUBLISH NOW"]').click()
        sleep(5)
        self.driver.find_element(By.ID, 'quick_action_posts_button').click()
        sleep(5)
        assert self.driver.find_element(By.ID, 'title').text == 'hello world'
        assert self.driver.find_element(By.ID, 'date_and_author').text == 'now  ·  your_blog_name'

    def test_and_delete_post(self):
        self.driver.find_element(By.ID, 'quick_action_posts_button').click()
        sleep(3)
        self.driver.find_element(By.ID, 'btn_ternary').click()
        sleep(2)
        self.driver.find_element(By.XPATH, '//android.widget.TextView[@text="Bin"]').click()
        sleep(2)
        self.driver.find_element(By.XPATH, '//android.widget.TextView[@text="SCHEDULED"]').click()
        sleep(2)
        self.driver.find_element(By.XPATH, '//android.widget.TextView[@text="BINNED"]').click()
        sleep(2)
        self.driver.find_element(By.XPATH, '//android.widget.TextView[@text="Delete permanently"]').click()
        sleep(2)
        self.driver.find_element(By.XPATH, '//android.widget.Button[@text="DELETE"]').click()
        sleep(6)
        assert self.driver.find_element(By.XPATH,
                                        '//android.widget.TextView[@text="You don\'t have any binned posts"]').text.replace(
            '\xa0',
            ' ') == "You don't have any binned posts"

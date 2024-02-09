import pytest
from time import sleep

from selenium.webdriver.common.by import By


@pytest.mark.usefixtures('setup_method')
class TestScroll():

    def test_scroll(self):
        sleep(3)
        for _ in range(15):
            print(_)
            end_y = 800
            try:
                value = self.driver.find_element(By.XPATH, '//android.widget.TextView[@text="Site Settings"]').is_displayed()
                if value is True:
                    break
            except:
                self.driver.swipe(470, 1460, 470, 800, 300)
                self.driver.implicitly_wait(2)
                continue
        sleep(3)


# start x
# start y
# end x
# end y
# duration

from appium import webdriver
import pytest
from appium.options.android import UiAutomator2Options


@pytest.fixture(scope='class')
def setup_method(request):
    options = UiAutomator2Options().load_capabilities({
        # Specify device and os_version for testing
        "platformName": "Android",
        "platformVersion": "12",
        "deviceName": "emulator-5554",
        "appPackage": "org.wordpress.android",
        "appActivity": "org.wordpress.android.ui.WPLaunchActivity",
        "noReset": True,

        # Set URL of the application under test
        "app": "/Users/vinodjoel/Desktop/app/Android/wordpress.apk",

        # Set other BrowserStack capabilities
        'wordpress:options': {
            "projectName": "Wordpress apk project",
            "buildName": "browserstack-build-1",
            "sessionName": "wpress first_test",

            # Set your access credentials
            #  "userName" : "YOUR_USERNAME",
            # "accessKey" : "YOUR_ACCESS_KEY"
        }
    })

    # Initialize the remote Webdriver using BrowserStack remote URL
    # and options defined above
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", options=options)
    request.cls.driver = driver
    yield
    driver.quit()

import os

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

def get_desired_capabilities(app):
    desired_caps = {
        'platformName': 'iOS',
        'platformVersion': '11.4',
        'deviceName': 'iPhone 7',
        'automationName': 'XCUITest',
        'app': PATH('./app/' + app),
    }

    return desired_caps
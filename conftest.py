import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as OptionsFireFox

def pytest_addoption(parser):
    # выбор браузера оставил, по умолчанию оставил Chrome
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='en',
                     help="Выберите язык: ")


@pytest.fixture(scope="function")
def browser(request):
    # выбор браузера оставил, по умолчанию оставил Chrome
    browser_name = request.config.getoption('browser_name')
    # выбор языка из коммандной строки
    user_language = request.config.getoption('language')

    #for Chrome
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})

    # for Firefox
    options_firefox = OptionsFireFox()
    options_firefox.set_preference("intl.accept_languages", user_language)

    if browser_name == "chrome":
        print("\nДля теста загружается Chrome...")
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("\nДля теста загружается Firefox...")
        browser = webdriver.Firefox(options=options_firefox)
    else:
        raise pytest.UsageError("--browser_name должен быть chrome или firefox")
    yield browser
    print("\nВыход из браузера...")
    browser.quit()

from selene.support.shared import browser
from selene.support.shared.jquery_style import s
import pytest


@pytest.fixture(scope='function')
def desktop_fixture():
    browser.config.window_width = 1920
    browser.config.window_height = 1080


@pytest.fixture(scope='function')
def mobile_fixture():
    browser.config.window_width = 390
    browser.config.window_height = 844


def test_github_desktop(desktop_fixture):
    browser.open('/')
    s(".HeaderMenu-link--sign-in").click()


def test_github_mobile(mobile_fixture):
    browser.open('/')
    s(".Button-label").click()
    s(".HeaderMenu-link--sign-in").click()

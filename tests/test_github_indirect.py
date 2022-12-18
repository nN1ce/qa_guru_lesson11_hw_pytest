from selene.support.shared import browser
from selene.support.shared.jquery_style import s
import pytest


@pytest.fixture(scope='function')
def application(request):
    browser.config.window_width = request.param[0]
    browser.config.window_height = request.param[1]


@pytest.mark.parametrize("application", [(390, 844), (1920, 1080)], indirect=True)
def test_with_param(application):
    if (browser.config.window_width != 640) and (browser.config.window_height != 960):
        pytest.skip("This test is to be used on mobile browser")
    browser.open('/')
    s(".Button-label").click()
    s(".HeaderMenu-link--sign-in").click()

from selene.support.shared import browser
from selene.support.shared.jquery_style import s
import pytest


@pytest.mark.parametrize(
    ["browser_width", "browser_height"],
    [(1920, 1080), (390, 844)],
    ids=["Декстоп", "Мобилка"],
)
def test_with_param(browser_width, browser_height):
    browser.config.window_width = browser_width
    browser.config.window_height = browser_height
    browser.open('/')
    if (browser_width == 1920) and (browser_height == 1080):
        s(".HeaderMenu-link--sign-in").click()
    elif (browser_width == 390) and (browser_height == 844):
        s(".Button-label").click()
        s(".HeaderMenu-link--sign-in").click()
    else:
        pytest.fail("Неправильное разрешение браузера. Проверить входные параметры")

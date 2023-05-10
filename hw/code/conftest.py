import pytest


def pytest_addoption(parser):
    parser.addoption('--browser', default='chrome')
    parser.addoption('--url', default='https://www.reazon.ru/cart')


@pytest.fixture(scope='session')
def url_config(request):
    return request.config.getoption('--url')


@pytest.fixture(scope='session')
def browser_config(request):
    return request.config.getoption('--browser')

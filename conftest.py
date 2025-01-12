import pytest
from services.dm_api.account.account import AccountApi
from services.dm_api.account.login import LoginApi
from services.mailhog.mailhog import MailhogApi

@pytest.fixture
def api_config():
    """
    Конфигурация для API endpoints
    """
    return {
        'base_url': 'http://5.63.153.31:5051',
        'mail_url': 'http://5.63.153.31:5025'
    }

@pytest.fixture
def account(api_config):
    return AccountApi(api_config['base_url'])

@pytest.fixture
def login(api_config):
    return LoginApi(api_config['base_url'])

@pytest.fixture
def mailhog(api_config):
    return MailhogApi(api_config['mail_url'])

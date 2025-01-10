import pytest
import json
from faker import Faker

fake = Faker()

class TestAccount:

    @pytest.fixture
    def user_data(self):
        return {
            'login': fake.user_name(),
            'email': fake.email(),
            'password': fake.password()
        }

    @pytest.fixture
    def registered_user(self, account, user_data):
        """Фикстура для регистрации пользователя"""
        response = account.post_v1_account(**user_data)
        assert response.status_code == 201
        return user_data

    @pytest.fixture
    def activation_token(self, mailhog):
        """Фикстура для получения токена активации"""
        messages = mailhog.get_api_v2_messages(limit='1').json()
        return json.loads(messages['items'][0]['Content']['Body'])['ConfirmationLinkUrl'].split('/')[-1]

    @pytest.fixture
    def activated_user(self, account, registered_user, activation_token):
        """Фикстура для активации пользователя"""
        response = account.put_v1_account_token(activation_token)
        assert response.status_code == 200
        return registered_user



    def test_post_v1_account(self, login, activated_user):
        """Тест регистрации аккаунта"""
        response = login.post_v1_account_login(
            activated_user['login'],
            activated_user['password']
        )
        assert response.status_code == 200

    def test_put_v1_account_token(self, login, activated_user):
        """Тест активации аккаунта"""
        response = login.post_v1_account_login(
            activated_user['login'],
            activated_user['password']
        )
        assert response.status_code == 200

    def test_post_v1_account_login(self, login, activated_user):
        """Тест входа в систему"""
        response = login.post_v1_account_login(
            activated_user['login'],
            activated_user['password']
        )
        assert response.status_code == 200

    def test_put_v1_account_email(self, account, login, mailhog, activated_user):
        """Тест смены email"""

        # Смена email
        new_email = fake.email()
        response = account.put_v1_account_email(
            activated_user['login'],
            new_email,
            activated_user['password']
        )
        assert response.status_code == 200

        # Проверка, что вход невозможен
        response = login.post_v1_account_login(
            activated_user['login'],
            activated_user['password']
        )
        assert response.status_code == 403

        # Получение нового токена активации
        messages = mailhog.get_api_v2_messages(limit='1').json()
        token = json.loads(messages['items'][0]['Content']['Body'])['ConfirmationLinkUrl'].split('/')[-1]

        # Активация нового email
        response = account.put_v1_account_token(token)
        assert response.status_code == 200

        # Проверка входа после активации
        response = login.post_v1_account_login(
            activated_user['login'],
            activated_user['password']
        )
        assert response.status_code == 200
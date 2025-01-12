import requests


class AccountApi:

    def __init__(self, base_url):
        self.base_url = base_url

    def post_v1_account(self, login, email, password):
        """
        Регистрация нового аккаунта.

        :param login: Логин пользователя.
        :param email: Email пользователя.
        :param password: Пароль пользователя.
        :return: Ответ от API.
        """
        url = f"{self.base_url}/v1/account"
        payload = {
            "login": login,
            "email": email,
            "password": password
        }

        response = requests.post(url, json=payload)
        return response

    def put_v1_account_token(self, token):
        """
        Активация аккаунта по токену.

        :param token: Токен активации.
        :return: Ответ от API.
        """
        url = f"{self.base_url}/v1/account/{token}"
        response = requests.put(url)
        return response

    def put_v1_account_email(self, login, new_email, password):
        """
        Смена email пользователя.

        :param login:
        :param password:
        :param new_email: Новый email пользователя.
        :return: Ответ от API.
        """
        url = f"{self.base_url}/v1/account/email"

        payload = {
            "login": login,
            "email": new_email,
            "password": password
        }
        response = requests.put(url, json=payload)
        return response

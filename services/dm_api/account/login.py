import requests


class LoginApi:
    def __init__(self, base_url: str):
        self.base_url = base_url

    def post_v1_account_login(self, login, password, remember_me):
        """
        :param login: Логин пользователя.
        :param password: Пароль пользователя.
        :param remember_me: Флаг запоминания сессии
        """
        url = f"{self.base_url}/v1/account/login"
        payload = {
            "login": login,
            "password": password,
            "rememberMe": remember_me
        }

        response = requests.post(url=url, json=payload)
        return response

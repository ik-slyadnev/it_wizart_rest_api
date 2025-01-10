import requests


class LoginApi:
    def __init__(self, base_url: str):
        self.base_url = base_url

    def post_v1_account_login(self, login: str, password: str, remember_me: bool = True) -> requests.Response:
        """
        Args:
            login: Логин пользователя
            password: Пароль пользователя
            remember_me: Флаг запоминания сессии

        Returns:
            requests.Response: Объект ответа
        """
        url = f"{self.base_url}/v1/account/login"
        headers = {
            'accept': 'text/plain',
            'Content-Type': 'application/json'
        }
        payload = {
            "login": login,
            "password": password,
            "rememberMe": remember_me
        }

        response = requests.post(
            url=url,
            json=payload,
            headers=headers
        )
        return response

import json
from faker import Faker

fake = Faker()


class TestPostV1AccountLogin:
    def test_post_v1_account_login(self, account, login, mailhog):
        # Регистрация пользователя
        user_data = {
            'login': fake.user_name(),
            'email': fake.email(),
            'password': fake.password()
        }
        response = account.post_v1_account(**user_data)
        assert response.status_code == 201, "Регистрация пользователя не прошла"

        # Получение и активация токена
        response = mailhog.get_api_v2_messages(limit='1')
        assert response.status_code == 200, "Письма не были получены"

        messages = response.json()
        token = None
        for item in messages['items']:
            message_data = json.loads(item['Content']['Body'])
            user_login = message_data['Login']
            if user_login == user_data['login']:
                token = message_data['ConfirmationLinkUrl'].split('/')[-1]
                break

        # Проверяем, что токен был найден
        assert token is not None, f"Токен для пользователя {user_data['login']} не был получен"

        response = account.put_v1_account_token(token)
        assert response.status_code == 200, "Не удалось активировать аккаунт"

        response = login.post_v1_account_login(
            user_data['login'],
            user_data['password'],
            remember_me=True
        )
        assert response.status_code == 200, "Не удалось авторизоваться"
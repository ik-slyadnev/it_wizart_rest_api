from faker import Faker

fake = Faker()


class TestPostV1Account:
    def test_post_v1_account(self, account):
        # Подготовка тестовых данных
        user_data = {
            'login': fake.user_name(),
            'email': fake.email(),
            'password': fake.password()
        }

        response = account.post_v1_account(**user_data)

        assert response.status_code == 201, "Регистрация пользователя не прошла"

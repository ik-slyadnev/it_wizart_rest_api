import requests



class MailhogApi:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_api_v2_messages(self, limit='2'):
        """
        Get users emails
        :return:
        """
        params = {
            'limit': limit,
        }

        url = f"{self.base_url}/api/v2/messages"
        response = requests.get(url=url, params=params)
        return response

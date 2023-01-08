import os

from tests.web_api.utils.requests_helper import BaseSession


# оборачиваем без бейс юрл
def dog() -> BaseSession:
	dog_url = os.getenv('dog_url')
	return BaseSession(base_url=dog_url)
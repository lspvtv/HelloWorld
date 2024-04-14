import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


class ParsingPage:
    def __init__(self, base_url):
        self.base_url = base_url

    def extract(self, pages, css_selector, base_url=None, attr="href"):
        data = []
        if base_url is None:
            base_url = self.base_url
        elements = pages.select(css_selector)
        for element in elements:
            if attr in element.attrs:
                content = element[attr]
            else:
                content = element.text.strip()  # Извлекаем текст элемента, если атрибут не указан

            if base_url and content:
                content = urljoin(base_url, content)  # Присоединяем базовый URL к относительным ссылкам

            data.append(content)
        return data

    @staticmethod
    def create_page(link):
        try:
            response = requests.get(link)
            response.raise_for_status()
            return BeautifulSoup(response.text, 'html.parser')
        except requests.exceptions.HTTPError as error:
            print(f"Error: {error.response.status_code} - {error.response.reason}")
        except requests.exceptions.RequestException as error:
            print(f"Error: {error}")
        return None

    @staticmethod
    def fetch_content_list(url):
        try:
            response = requests.get(url)
            response.raise_for_status()  # Проверяем, не вернул ли сервер ошибку
            data = response.json()  # Парсим ответ сервера из JSON
            return data
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")  # HTTP ошибка (например, 404, 501, и т.д.)
        except ValueError as json_err:
            print(f"JSON parsing error occurred: {json_err}")  # Ошибки парсинга JSON
        return None

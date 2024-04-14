from auto_list_of_curls.parsing import create_page, extract, fetch_content_list

HTML = create_page("https://dog.ceo/dog-api/documentation/")

data = []
urls = extract(HTML, 'ul.endpoints-list li a', base_url='https://dog.ceo')

for url in urls:
    # Для каждой страницы извлекаем HTML и затем curl команды
    page_html = create_page(url)
    if page_html:
        curls = extract(page_html, 'span.code', attr=None)  # Извлекаем текст, не атрибут
        data.append(curls)

lists_breeds = fetch_content_list('https://dog.ceo/api/breeds/list/all')

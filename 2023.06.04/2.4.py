import re
import json
from urllib.request import urlopen
from pathlib import Path


def json_from_html(url: str, regex_pattern: str, decode: str = 'utf-8') -> Path:
    """
    Извлекает из HTML документа структурируемые данные и помещает их в JSON файл.
    :param url: URL адрес сайта.
    :param regex_pattern: шаблон регулярного выражения.
    :param decode: кодировка страницы.
    :return: путь к JSON файлу.
    """
    with urlopen(url) as response:
        resource = urlopen(url)
        charset = resource.headers.get_content_charset()
        if charset != decode or charset is None:
            html = response.read().decode(decode)
        else:
            html = response.read().decode(charset)

    match_result = re.findall(regex_pattern, html, re.S)
    extracted_data = {key: value for key, value in match_result}

    if url.endswith('.html'):
        json_filename = Path(url).name.replace('.html', '.json')
    else:
        module_path = Path(__file__)
        json_filename = module_path.stem + '.json'

    json_path = Path(json_filename)
    with json_path.open('w', encoding='utf-8') as json_file:
        json.dump(extracted_data, json_file, ensure_ascii=False, indent=2)

    return json_path


# >>> url = 'http://www.world-art.ru/cinema/rating_top.php'
# >>>
# >>> films_pattern = (r'<tr .*?>'
#                       r'<td .*?<a.*?>(?P<name>.*?)</a>.*?</td>'
#                       r'<td .*?>(?P<rating>.*?)</td>')
# >>>
# >>> file_path = json_from_html(url, films_pattern)
# >>>
# >>> file_path.name
# '2.4.json'
# >>>
# >>> Path(__loader__.path).name
# 'pydevconsole.py'
# >>>
# >>> print(file_path.read_text(encoding='utf-8')[:145])
# {
#   "Побег из Шоушенка": "8.9768",
#   "Зелёная миля": "8.9564",
#   "Форрест Гамп": "8.9066",
#   "Леон": "8.8932",
#   "Достучаться до небес": "8.8530"
#
# >>> url = 'https://docs.python.org/3/py-modindex.html'
# >>> modules_pattern = r'<tr>.+?>(\w+?)<.+?</td><td>.*?<em>(.*?)</em>'
# >>>
# >>> file_path = json_from_html(url, modules_pattern)
# >>>
# >>> file_path.name
# 'py-modindex.json'
# >>>
# >>> print(file_path.read_text(encoding='utf-8')[:110])
# {
#   "__future__": "Future statement definitions",
#   "__main__": "The environment where top-level code is run.

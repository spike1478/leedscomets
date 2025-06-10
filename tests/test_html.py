import os
from bs4 import BeautifulSoup


def test_index_html_parses():
    index_path = os.path.join(os.path.dirname(__file__), os.pardir, 'index.html')
    with open(index_path, 'r', encoding='utf-8') as f:
        content = f.read()
    soup = BeautifulSoup(content, 'html.parser')
    assert soup.find('html') is not None


from bs4 import BeautifulSoup
import requests
import re


def _get_content_soup(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup


def _get_p_text_from_soup(soup: BeautifulSoup):
    p = soup.find_all('p')
    raw_text = [_remove_control_characters(raw.text) for raw in p if len(raw.text.split()) > 30]
    return ' '.join([_remove_quotations(text) for text in raw_text])


def _remove_quotations(text):
    text = text.replace('’', '')
    text = text.replace('‘', '')
    text = text.replace('“', '')
    text = text.replace('”', '')
    return text


def _remove_control_characters(text):
    return re.sub(r'[\x00-\x1F\x7F-\x9F]', '', text)


def web_extract(url: str) -> str:
    soup = _get_content_soup(url)
    return _get_p_text_from_soup(soup)

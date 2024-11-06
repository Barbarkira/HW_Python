import requests
from bs4 import BeautifulSoup
from typing import List, Union


def get_wiki_info(keyword: str, max_num_sentences: int = 10, max_sentence_length: int = 10) -> Union[List[str], None]:
    url = "https://simple.wikipedia.org/wiki/" + keyword.replace(" ",
                                                                 "_")

    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException:
        return []


    soup = BeautifulSoup(response.text, 'html.parser')

    paragraphs = soup.find_all('p')

    sentences = []
    for para in paragraphs:
        # Split paragraph into sentences
        para_sentences = para.get_text().split('. ')
        for sentence in para_sentences:
            sentence = sentence.strip() + '.' if sentence else ''
            if sentence and len(sentence.split()) <= max_sentence_length:
                sentences.append(sentence)
            if len(sentences) >= max_num_sentences:
                break
        if len(sentences) >= max_num_sentences:
            break

    return sentences[:max_num_sentences]

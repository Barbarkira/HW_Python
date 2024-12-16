from csv_creator import CsvCreator
from html_parser import NewsContainer,HtmlParser
from pipeline import PipeAnalyzer


parser = HtmlParser()
analyzer = PipeAnalyzer()
csv_creator = CsvCreator()

path_to_html = "messages.html"
list = parser.parse_data(path_to_html)

news_big_container ={
    'число' : [],
    'семантический тег' : [],
    'тема' : [],
    'текст' : []
}

for news in list:
    news.semantic_tag = analyzer.semantic_pipe(news.news_text)
    news.topic = analyzer.topic_pipe(news.news_text)

    news_big_container['число'].append(news.news_date)
    news_big_container['семантический тег'].append(news.semantic_tag)
    news_big_container['тема'].append(news.topic)
    news_big_container['текст'].append(news.news_text)

csv_creator.csv_folder(news_big_container)
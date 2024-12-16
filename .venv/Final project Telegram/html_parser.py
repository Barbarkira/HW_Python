from bs4 import BeautifulSoup


class NewsContainer:
    def __init__(self, text, date):
        self.news_text = text
        self.news_date = date


class HtmlParser:
    def parse_data(self, path_to_html_file):
        parsed_news = []
        # Open and parse the HTML file
        with open(path_to_html_file, encoding='utf-8') as fp:
            data = BeautifulSoup(fp, "html.parser")

            # Find all div elements with class 'body'
            posts = data.find_all('div', class_='body')

            for post in posts:
                # Check if the post contains a div with class 'text'
                text_div = post.find('div', class_='text')
                if text_div is not None:
                    # Extract the text content
                    news_text = text_div.get_text()

                    # Extract the date from the 'pull_right date details' div
                    date_div = post.find('div', class_='pull_right date details')
                    if date_div is not None:
                        news_date = date_div.get('title')
                        if news_date:
                            news_date = news_date[:10]  # Extract only the date part

                        # Create a NewsContainer object
                        news = NewsContainer(news_text, news_date)
                        parsed_news.append(news)

        return parsed_news







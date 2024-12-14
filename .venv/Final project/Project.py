from datetime import datetime
from typing import List
import matplotlib.pyplot as plt
import csv


def read_csv(input_csv: str, attribute_name: str, delimiter: str = ',') -> tuple[List[datetime], List[str]]:
    dates = []
    attributes = []
    with open(input_csv, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=delimiter)
        for row in reader:
            try:
                date_object = datetime.strptime(row['date'],
                                                '%Y-%m-%d')
                dates.append(date_object)
            except ValueError as e:
                print(f"Ошибка при разборе даты: {e}. Строка: {row}")
                continue

            attributes.append(row[attribute_name])
    return dates, attributes


def convert_attributes(attributes: List[str]) -> List[int]:

    converted = []
    for attr in attributes:
        if attr.upper() == 'POSITIVE':
            converted.append(1)
        elif attr.upper() == 'NEUTRAL':
            converted.append(0)
        elif attr.upper() == 'NEGATIVE':
            converted.append(-1)
        else:
            converted.append(0)
    return converted


def plot_data(dates: List[datetime], attributes: List[int], output_path: str):
    plt.figure(figsize=(12, 6))
    plt.plot(dates, attributes, marker='o', linestyle='-')
    plt.xlabel("Дата")
    plt.ylabel("Атрибут")
    plt.title("Временная шкала атрибута")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()


def save_timeline(input_csv: str, output_path: str, attribute_name: str, delimiter: str = ','):
    dates, attributes = read_csv(input_csv, attribute_name, delimiter=delimiter)
    converted_attributes = convert_attributes(attributes)
    plot_data(dates, converted_attributes, output_path)


# Пример использования:
input_csv_file = "data.csv"  # Замените на путь к вашему CSV файлу
output_image_path = "timeline.png"  # путь к сохраняемому изображению
attribute_column = "sentiment"  # название колонки с атрибутами

save_timeline(input_csv_file, output_image_path, attribute_column)

# pipeline.py
from .pipeline import pipeline

all = ['pipeline']

# html_parser.py
from bs4 import BeautifulSoup
from typing import List, Tuple
from datetime import datetime


class HtmlParser:
    @staticmethod
    def parse_data(path_to_html_file) -> List[Tuple[datetime, str]]:
        parsed_data = []
        try:
            with open(path_to_html_file, encoding='utf-8') as fp:
                data = BeautifulSoup(fp, "html.parser")
                for post in data.find_all('div', class_='message'):
                    date_str = post.find('span', class_='date').text.strip()
                    text = post.find('div', class_='text').text.strip()
                    try:
                        date = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
                        parsed_data.append((date, text))
                    except ValueError:
                        print(f"Ошибка парсинга даты в файле {path_to_html_file}: {date_str}")
        except FileNotFoundError:
            print(f"Файл не найден: {path_to_html_file}")
        except Exception as e:
            print(f"Ошибка при обработке файла {path_to_html_file}: {e}")
        return parsed_data


# pipeline.py
from typing import Optional
from tqdm import tqdm
import argparse
import os
from .html_parser import HtmlParser
from .sentiment_classifier import SentimentClassifier
from .timeline_visualizer import save_timeline
import csv
from datetime import datetime
from dateutil import parser


def parse_args():
    parser = argparse.ArgumentParser(description='Parses Telegram channel export and generates timeline.')
    parser.add_argument('data_dir', help='Path to folder with html files')
    parser.add_argument('--attribute', help='Attribute for timeline (e.g., sentiment)', default='sentiment')
    parser.add_argument('--output_dir', help='Output directory for CSV and timeline', default='output')
    args = parser.parse_args()
    return args


def pipeline():
    args = parse_args()
    os.makedirs(args.output_dir, exist_ok=True)
    html_files = []
    if os.path.isdir(args.data_dir):
        for root, _, files in os.walk(args.data_dir):
            for file in files:
                _, ext = os.path.splitext(file)
                if ext == '.html':
                    html_files.append(os.path.join(root, file))
    else:
        print(f"Ошибка: {args.data_dir} - не является директорией.")
        return

    if len(html_files) == 0:
        print("Ошибка: Не найдено HTML файлов в указанной директории.")
        return

    data_samples = []
    print("Parsing input files...")
    for html_file in tqdm(html_files):
        data_samples.extend(HtmlParser.parse_data(html_file))

    classifier = SentimentClassifier()
    print("Classification in progress...")
    for i, sample in enumerate(tqdm(data_samples)):
        try:
            result = classifier.predict(sample[1])
            data_samples[i] = (
            sample[0], sample[1], result['label'], result['score'])
        except Exception as e:
            print(f"Ошибка классификации для поста {i + 1}: {e}")

    csv_filepath = os.path.join(args.output_dir, 'telegram_data.csv')
    with open(csv_filepath, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Date', 'Text', 'Sentiment', 'Score']
        writer = csv.writer(csvfile)
        writer.writerow(fieldnames)
        for row in data_samples:
            writer.writerow([row[0].strftime('%Y-%m-%d %H:%M:%S'), row[1], row[2], row[3]])

    print(f"Данные сохранены в {csv_filepath}")
    save_timeline(csv_filepath, args.output_dir, attribute_name=args.attribute)


# sentiment_classifier.py
from typing import List
from tqdm import tqdm
from transformers import pipeline


class SentimentClassifier:
    def __init__(self):
        self.analyzer_pipeline = pipeline("sentiment-analysis", model='MonoHime/rubert-base-cased-sentiment-new',
                                          device=0 if torch.cuda.is_available() else -1)  # использование GPU, если доступно

    def predict(self, sample: str):
        return self.analyzer_pipeline(sample)[0]  # возвращаем только первый элемент из списка


# timeline_visualizer.py
import matplotlib.pyplot as plt
import csv
from datetime import datetime
from dateutil import parser
import pandas as pd
import os


def convert_datetime(datetime_str: str):
    try:
        return parser.parse(datetime_str)
    except ValueError:
        return None


def save_timeline(input_csv: str, output_dir: str, attribute_name: str):
    try:
        df = pd.read_csv(input_csv)
        df['Date'] = pd.to_datetime(df['Date'])
        df = df.sort_values(by=['Date'])

        timeline_data = df.groupby(df['Date'].dt.date)[attribute_name].agg(['value_counts']).to_dict('index')

        dates = list(timeline_data.keys())
        labels = [max(timeline_data[date]['value_counts'], key=timeline_data[date]['value_counts'].get) for date in
                  dates]

        plt.figure(figsize=(15, 6))
        plt.plot(dates, labels)
        plt.xlabel("Дата")
        plt.ylabel(attribute_name)
        plt.title(f"Таймлайн по атрибуту {attribute_name}")
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.savefig(os.path.join(output_dir, f'timeline_{attribute_name}.png'))
        print(f"Таймлайн сохранен в {os.path.join(output_dir, f'timeline_{attribute_name}.png')}")

    except FileNotFoundError:
        print(f"Ошибка: файл {input_csv} не найден.")
    except Exception as e:
        print(f"Ошибка при построении таймлайна: {e}")
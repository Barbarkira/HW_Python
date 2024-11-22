import os
import re
from string import punctuation
import pymorphy2
import matplotlib.pyplot as plt
from collections import Counter

morph = pymorphy2.MorphAnalyzer()
stop_words = {"в", "на", "с", "к", "от", "до", "из", "перед", "за", "под", "над", "между", "через", "около", "возле", "рядом", "против", "мимо", "сквозь", "по", "для", "без", "через", "у", "о", "об", "со", "и"}


def preprocess_text(text):
  text = text.lower() # приведение к нижнему регистру
  text = "".join([c for c in text if c not in punctuation])
  text = re.sub(r'\s+', ' ', text).strip()
  return text


def create_word_frequency(text):
  words = text.split()
  normalized_words = [morph.parse(word)[0].normal_form for word in words if word not in stop_words]
  return Counter(normalized_words)


def plot_histogram(word_counts, title):
  words, counts = zip(*word_counts.most_common(20))
  plt.figure(figsize=(10, 6))
  plt.bar(words, counts)
  plt.xlabel("Слова")
  plt.ylabel("Частота")
  plt.title(title)
  plt.xticks(rotation=45, ha='right')
  plt.tight_layout()
  plt.show()


def analyze_reviews(positive_dir, negative_dir):
  positive_reviews = []
  negative_reviews = []

  for filename in os.listdir(positive_dir):
    with open(os.path.join(positive_dir, filename), 'r', encoding='utf-8') as f:
      text = f.read()
      positive_reviews.append({"text": preprocess_text(text), "sentiment": "positive"})


  for filename in os.listdir(negative_dir):
    with open(os.path.join(negative_dir, filename), 'r', encoding='utf-8') as f:
      text = f.read()
      negative_reviews.append({"text": preprocess_text(text), "sentiment": "negative"})


  positive_word_counts = []
  negative_word_counts = []

  for review in positive_reviews:
    word_counts = create_word_frequency(review["text"])
    positive_word_counts.append(word_counts)
    plot_histogram(word_counts, f"Гистограмма для положительного отзыва: {review['text'][:50]}...")


  for review in negative_reviews:
    word_counts = create_word_frequency(review["text"])
    negative_word_counts.append(word_counts)
    plot_histogram(word_counts, f"Гистограмма для отрицательного отзыва: {review['text'][:50]}...")

  all_positive_words = set()
  for counts in positive_word_counts:
    all_positive_words.update(counts)

  all_negative_words = set()
  for counts in negative_word_counts:
    all_negative_words.update(counts)


  only_positive = all_positive_words - all_negative_words
  only_negative = all_negative_words - all_positive_words
  common_words = all_positive_words & all_negative_words


  print("Слова, встречающиеся только в положительных отзывах:", only_positive)
  print("Слова, встречающиеся только в отрицательных отзывах:", only_negative)
  print("Общие слова:", common_words)




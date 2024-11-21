import json
import os

def read_data(path):
    data = open(path, 'rt').read()
    return data.split('\n')

def word_dictionary(data) -> dict:
    frequency_dic = {}
    for word in data:
        if word not in frequency_dic:
            frequency_dic[word] = 1
        elif word in frequency_dic:
            frequency_dic[word] += 1
    return frequency_dic

def create_chapters_dicts(data):
    deliminators_indicis = [i for i, e in enumerate(data[1:]) if e == '[new chapter]']
    start = 0
    chapter_frequencies = []
    for index in deliminators_indicis:
        chapter_context = data[start:index]
        chapter_frequency = word_dictionary(chapter_context)
        chapter_frequencies.append(chapter_frequency)
        start = index
    last_chapter = data[start:]
    chapter_frequency = word_dictionary(last_chapter)
    chapter_frequencies.append(chapter_frequency)
    return chapter_frequencies

def chapter_frequency(path: str, target_word: str) -> float:
    data = read_data(path)
    chapter_frequencies = create_chapters_dicts(data)
    num_chapters_with_word = 0
    total_chapters = len(chapter_frequencies)
    for chapter in chapter_frequencies:
        if target_word in chapter:
            num_chapters_with_word += 1
    chapter_freq = num_chapters_with_word / total_chapters if total_chapters > 0 else 0
    return chapter_freq

def term_frequency(target_word: str, target_chapter_idx: int) -> float:
    data = read_data("class_4/hw3/war_peace.txt")
    chapter_frequencies = create_chapters_dicts(data)

    if 0 <= target_chapter_idx < len(chapter_frequencies):
        chapter_data = list(chapter_frequencies[target_chapter_idx].keys())
        total_words = len(chapter_data)
        word_count = chapter_frequencies[target_chapter_idx].get(target_word, 0)
        tf = word_count / total_words if total_words > 0 else 0
        return tf
    else:
        return 0


def get_tf_idf(path: str, target_word: str, target_chapter: int) -> float:
    data = read_data(path)
    chapter_frequencies = create_chapters_dicts(data)
    tf = term_frequency(target_word, target_chapter)

    if tf == 0:
      return 0

    num_chapters_with_word = 0
    total_chapters = len(chapter_frequencies)
    for chapter in chapter_frequencies:
        if target_word in chapter:
            num_chapters_with_word += 1

    idf = 0
    if num_chapters_with_word > 0:
        idf =  (total_chapters / num_chapters_with_word)

    tf_idf = tf * idf
    return tf_idf

print


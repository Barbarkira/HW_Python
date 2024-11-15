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
            continue
        if word in frequency_dic:
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

def read_data(path: str) -> list:
    with open(path, 'r', encoding='utf-8') as file:
        return file.readlines()

def create_chapters_dicts(data: list) -> dict:
    chapters = {}
    for i, line in enumerate(data):
        chapters[i] = line.strip()
    return chapters

def chapter_frequency(path: str, target_word: str) -> float:
    data = read_data(path)
    chapter_frequencies = create_chapters_dicts(data)

    number_of_chapters = len(chapter_frequencies)
    number_of_chapters_with_target_word = 0

    for chapter in chapter_frequencies.values():
        if target_word in chapter.split():
            number_of_chapters_with_target_word += 1
    if number_of_chapters == 0:
        return 0.0

    chapter_freq = number_of_chapters_with_target_word / number_of_chapters
    return chapter_freq
def term_frequency(target_word: str, target_chapter_idx: int, chapters: dict) -> float:
    chapter_text = chapters.get(target_chapter_idx, "")
    words = chapter_text.split()
    if not words:
        return 0.0
    count_target_word = words.count(target_word)
    total_words = len(words)
    tf = count_target_word / total_words
    return tf


import math
from collections import Counter
def get_tf_idf(data, target_word: str, target_chapter: int) -> float:
    chapter_text = data[target_chapter]
    words = chapter_text.lower().split()
    total_words = len(words)
    term_count = words.count(target_word.lower())
    if total_words > 0:
        tf = term_count / total_words
    else:
        tf = 0.0
    total_chapters = len(data)
    doc_count = sum(1 for chapter in data if target_word.lower() in chapter.lower())
    if doc_count > 0:
        idf = math.log(total_chapters / doc_count)
    else:
        idf = 0.0
    tf_idf = tf * idf
    return tf_idf


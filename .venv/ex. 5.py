## Упражнение 5
# Даны две строки: s1 и s2.
# Напишите программу, которая выведет на экран количество уникальных символов, встречающихся в обеих строках.
# Sample input: s1 = 'abcdabcd', s2 = 'cdcdef'
# Sample output: 2

s1 = 'abcdabcd'
s2 = 'cdcdef'

set1 = set(s1)
set2 = set(s2)

common_characters = set1.intersection(set2)
print(len(common_characters))
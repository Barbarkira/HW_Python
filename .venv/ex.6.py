## Упражнение 6*
# Прочитайте статью "*args и **kwargs"
# https://pavel-karateev.gitbook.io/intermediate-python/sintaksis/args_and_kwargs
# Если мы хотим использовать  *args, **kwargs и формальные параметры в функции, какой будет порядок? А если будут параметры со значениями по умолчанию?
# Напишите функцию print_lists. Она принимает набор порядковых аргументов, каждый из которых является списком. Затем следует аргумент how (по умолчанию None),
# в который передаются аргументы с правилами для печати (например,  sep и end). Если правила не переданы, следует напечатать списки с sep=' ' и end='\n'.



def print_lists(*lists, how=None):
    sep = how.get('sep', ' ') if isinstance(how, dict) else ' '
    end = how.get('end', '\n') if isinstance(how, dict) else '\n'

    for lst in lists:
        print(*lst, sep=sep, end=end)


print_lists([1, 2, 3], [4, 5, 6], how={'sep': '-', 'end': ' | '})
print_lists([7, 8, 9], [10, 11, 12])
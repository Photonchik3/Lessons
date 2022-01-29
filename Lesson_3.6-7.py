import re


def int_func(s):
    #words = [w.capitalize() for w in s.split()]
    #eturn ' '.join(words)
    return s.title()


text = input('Введите слова латиницей с маленькой буквы: ')
if re.search('[^a-z]', text.replace(' ', '')) is not None:
    print('Введены недопустимые символы')
else:
    print(int_func(text))
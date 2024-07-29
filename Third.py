from bs4 import BeautifulSoup
import requests
from googletrans import Translator

def get_english_words():
    url = 'https://randomword.com'

    try:
        response = requests.get(url)

        soup = BeautifulSoup(response.text, 'html.parser')

        english_words = soup.find('div', id='random_word').text.strip()
        word_definition = soup.find('div', id='random_word_definition').text.strip()

        return{
            'english_words': english_words,
            'word_definition': word_definition
        }

    except:
        print('Произошла ошибка')

def word_game():
    print('Добро пожаловать в игру!')
    while True:
        word_dict = get_english_words()
        word = word_dict.get('english_words')
        word_definition = word_dict.get('word_definition')

        print(f'Значение слова - {word_definition}')
        user_input = input('Что это за слово? ')
        if user_input == word:
            print('Поздравляю, вы угадали!')
        else:
            print(f'Неправильно. Правильный ответ - {word}')

        play_again = input('Хотите сыграть еще раз? (y/n) ')
        if play_again.lower() != 'y':
            print('Спасибо за игру!')
            break


word_game()


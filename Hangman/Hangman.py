import random


def picture() -> list:                      # Создаем список, элементы которого - рисунки(кол-во неправильных ответов)
    hangman_pict = ['''
       +---+
           |
           |
           |
          ===''', '''
       +---+
       O   |
           |
           |
          ===''', '''
       +---+
       O   |
       |   |
           |
          ===''', '''
       +---+
       O   |
      /|   |
           |
          ===''', '''
       +---+
       O   |
      /|\  |
           |
          ===''', '''
       +---+
       O   |
      /|\  |
      /    |
          ===''', '''
       +---+
       O   |
      /|\  |
      / \  |
          ===''']
    return hangman_pict


def get_random_word() -> str:                       # Читаем слова из файла, и случайным образом выбираем загаданное слово
    my_words = []
    with open('words.txt') as file:
        words = file.readlines()
        for w in words:
            if len(w.strip()) == 6:
                my_words.append(w.strip())
        guessed_word = random.choice(my_words)
    return guessed_word


def display_board(wrong_letters: str, correct_letters: str,
                  word: str):                                   # Сам процесс игры: виселица и шаблон с угаданными буквами
    print(picture()[len(wrong_letters)])
    print()
    print('Wrong letters:', end=' ')
    for letter in wrong_letters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(word)

    for i in range(len(word)):                                                  # Заменяем прочерки угаданными буквами
        if word[i] in correct_letters:
            blanks = blanks[:i] + word[i] + blanks[i + 1:]

    for letter in blanks:                                                       # Выводим шаблон с угаданными буквами
        print(letter, end=' ')
    print()


def enter_a_letter(already_guessed) -> str:                                                     # Процесс ввода букв
    while True:
        print('Enter a letter: ')
        guess = input().lower()
        if len(guess) != 1 or guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a single letter')
        elif guess in already_guessed:
            print('You have already guessed that letter. Enter another letter')
        return guess


def play_again() -> bool:                                                       # Функция предлагает сыграть еще раз
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')


def the_game():
    wrong_letters = ''
    correct_letters = ''
    word = get_random_word()
    game_over = False
    while True:
        display_board(wrong_letters, correct_letters, word)                         # выводим виселицу

        guess = enter_a_letter(wrong_letters + correct_letters)                     # запускаем функцию для ввода букв

        if guess in word:
            correct_letters = correct_letters + guess

            win_a_game = True                                                   # Проверяем на случай, если слово угадано
            for i in range(len(word)):
                if word[i] not in correct_letters:
                    win_a_game = False
                    break
            if win_a_game:
                print(f'Yes! The secret word is {word}! You have won!')
                game_over = True
        else:
            wrong_letters = wrong_letters + guess

            if len(wrong_letters) == len(
                    picture()) - 1:                     # Проверяем не ввел ли игрок слишком много неправильных ответов
                display_board(wrong_letters, correct_letters, word)
                print(f' You have run out of guesses! \n After {len(wrong_letters)} wrong letters and '
                      f'{len(correct_letters)} correct guesses, \n the word was: {word}')
                game_over = True

        if game_over:                                                   ## Спрашиваем игрока не хочет ли он сыграть еще,
            if play_again():                                            ## но только если предыдущая игра закончилась
                wrong_letters = ''
                correct_letters = ''
                game_over = False
                word = get_random_word()
            else:
                break
try:
    if __name__ == '__main__':
        the_game()
except KeyboardInterrupt:
    print('Try run again')


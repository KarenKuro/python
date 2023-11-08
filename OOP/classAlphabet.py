import string


class Alphabet:
    def __init__(self, lang: str, letters: str):
        self.lang = lang
        self.letters = letters

    def print(self):
        print(self.letters)

    def letters_num(self):
        return len(self.letters)


class EngAlphabet(Alphabet):
    default_letters = string.ascii_uppercase

    def __init__(self, lang):
        super().__init__(lang, EngAlphabet.default_letters)
        self.__letters_num = 22

    def is_en_letter(letr: str):
        if letr.upper() in EngAlphabet.default_letters:
            print(f'{letr} is letter from English Alphabet')
        else:
            print(f'{letr} is not letter from English Alphabet')

    def letters_num(self):
        return print(self.__letters_num)

    @staticmethod
    def example():
        print('''Olya has a pencil, \nOlya has a pen,\nShe draws with a pencil,\nShe writes with a pen.''')


if __name__ == '__main__':
    JonnyMnemonic = EngAlphabet('En')
    print(EngAlphabet.default_letters)
    EngAlphabet.letters_num(JonnyMnemonic)
    EngAlphabet.is_en_letter('F')
    EngAlphabet.is_en_letter('Щ')
    EngAlphabet.example()
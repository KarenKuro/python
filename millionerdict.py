import random

ml = ['What is the capital of France?Paris,London,Berlin,Moscow',
      'What is the capital of GB?London,Paris,Berlin,Moscow',
      'What is the capital of Germany?Berlin,Paris,London,Moscow',
      'What is the capital of Russia?Moscow,Paris,London,Berlin',
      'What is the capital of Spain?Madrid,Rome,Yerevan,Tbilisi',
      'What is the capital of Italy?Rome,Madrid,Yerevan,Tbilisi',
      'What is the capital of Armenia?Yerevan,Madrid,Rome,Tbilisi',
      'What is the capital of Georgia?Tbilisi,Madrid,Rome,Yerevan',
      'What is the capital of Japan?Tokio,Astana,Beijing,Vien',
      'What is the capital of Kazakhstan?Astana,Tokio,Beijing,Vien',
      'What is the capital of China?Beijing,Tokio,Astana,Vien',
      'What is the capital of Austria?Vien,Tokio,Astana,Beijing',
      'What is the capital of Egypt?Cairo,Warsaw,Washington,Tallinn',
      'What is the capital of Poland?Warsaw,Cairo,Washington,Tallinn',
      'What is the capital of USA?Washington,Cairo,Warsaw,Tallinn']


def qwestion(k: int = 10) -> dict:
    d = {}
    ml1 = random.sample(ml, k)
    for i in ml1:
        qwest = i.split('?')
        answ = qwest[1].split(',')
        d.update({qwest[0]: answ})
    return d


def millioner(count: int = 0):
    d = qwestion()
    for i in d:
        print(i + '?')
        correct = d[i][0]
        random.shuffle(d[i])
        for j in range(len(d[i])):
            print(d[i][j], sep='\n')
        answer = input()
        if answer == correct:
            count += 1
        print(f'Правильных ответов: {count} из 10')


millioner()

import random


def logingame() -> str:
    print('Enter you name: ')
    name = 'Unknown user'
    incoming_name = input()
    if len(incoming_name) > 0:
        name = incoming_name
        print(f"Let's play, {name} \n")
    else:
        print(f"Let's play, {name} \n")
    return name


def readqwest() -> list:
    with open('millioner.txt') as ml:
        ml = ml.read().splitlines()
    return ml


def qwestion(k: int = 10) -> dict:
    ml = readqwest()
    d = {}
    ml1 = random.sample(ml, k)
    return method_name_extract(d, ml1)


def method_name_extract(d, ml1) -> dict:
    for i in ml1:
        qwest = i.split('?')
        answ = qwest[1].split(',')
        d.update({qwest[0]: answ})
    return d


def result_game(name, count):
    result = str(name + ', ' + str(count))
    with open('leader_board.txt', mode='r+') as ml:
        rez = ml.read().splitlines()
        for i in rez:
            if name in i:
                rez.remove(i)
        rez.append(result)
        ml = open('leader_board.txt', 'w')
        if rez != []:
            rez = sorted(rez, key=lambda x: (-int(x[-1]), x[0]))
        for i in rez:
            ml.write(i + '\n')
    print(*rez, sep='\n')


def millioner(count: int = 0):
    name = logingame()
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
        print(f'Correct answers: {count} / 10')
    result_game(name, count)


millioner()

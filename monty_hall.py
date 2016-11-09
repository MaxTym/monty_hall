import random


def shuffle(prizes):
    random.shuffle(prizes)


def game():
    count = 1000
    car = 0
    while count > 0:
        prizes = ['goat', 'goat', 'car']
        shuffle(prizes)
        index = random.randrange(3)
        choice = random.choice(prizes)
        if choice == 'car':
            car += 1
        count -= 1
    print("Not changing a door: ", (car/1000)*100)



def game_change_door():
    count = 1000
    car = 0
    while count > 0:
        prizes = ['goat', 'goat', 'car']
        shuffle(prizes)
        index = random.randrange(3)
        for i, y in enumerate(prizes):
            if i == index:
                prizes.remove(y)
        for i, y in enumerate(prizes):
            if y == 'goat':
                prizes.remove('goat')
        if prizes[0] == 'car':
            car += 1
        count -= 1
    print("Changing door chance: ", (car/1000)*100)


def main():
    game()
    game_change_door()


main()

import random


def game(count):
    car = 0
    while count > 0:
        prizes = ['goat', 'goat', 'car']
        random.shuffle(prizes)
        index = random.randrange(3)
        choice = random.choice(prizes)
        if choice == 'car':
            car += 1
        count -= 1
    return car


def game_change_door(count):
    car = 0
    while count > 0:
        prizes = ['goat', 'goat', 'car']
        random.shuffle(prizes)
        index = random.randrange(3)
        prizes.remove(prizes[index])
        if 'goat' in prizes:
            prizes.remove('goat')
        if prizes[0] == 'car':
            car += 1
        count -= 1
    return car


def half_and_half():
    x = game(500)
    y = game_change_door(500)
    print("Half and half chances to win: ", (((x + y)/1000)*100), '%')


def main():
    half_and_half()
    not_changing_door_cars = game(1000)
    print("Not changing a door: ", (not_changing_door_cars/1000)*100, '%')
    changing_door_cars = game_change_door(1000)
    print("Changing door chance: ", (changing_door_cars/1000)*100, '%')


if __name__ == "__main__":
    main()

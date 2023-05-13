import random


class Dog:
    def __init__(self,name):
        self.happiness=50
        self.name = name
        self.hungred = 0
        self.is_life = True
        self.toilet = 0

    def to_eat(self):
        print('Time to eat!')
        self.hungred -= 1
        self.happiness += 5

    def to_sleep(self):
        print('ZZzzzz')
        self.happiness +=3
    def to_walk(self):
        print('Time to walk!')
        self.happiness += 5
        if self.toilet <= 0:
            self.toilet +=1
        else:
            self.toilet -= 1
        self.hungred += 1
    def status(self):
        print(f'Happiness : {self.happiness}')
        print(f'Hungred : {self.hungred }')
        print(f'toilet : {self.toilet}')
    def live_a_hour(self, day):
        day_str = f'Hour {day} of {self.name} life'
        print(f'{day_str :=^50}')
        dice = random.randint(1,3)
        if dice == 1:
            self.to_eat()
        elif dice == 2:
            self.to_sleep()
        elif dice == 3:
            self.to_walk()
        self.status()

khati = Dog(name = 'Khati')
for day in range(365):
    if khati.is_life:
        khati.live_a_hour(day)
    else:
        break

if khati.is_life:
    print('HURRAH!You are a good host')
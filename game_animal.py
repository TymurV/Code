import time


class Critter():
    def __init__(self, name, hungry = 0, boredom = 0):
        self.name = name
        self.hungry = hungry
        self.boredom = boredom
    
    def __pass_time(self):
        self.hungry += 1
        self.boredom += 1
    
    @property
    def mood(self):
        unhappiness = self.hungry + self.boredom
        if unhappiness < 5:
            m = 'Fine!'
        elif unhappiness < 10:
            m = 'Cool!'
        elif unhappiness < 15:
            m = 'Okay!'
        else:
            m = 'Bad:('
        return m

    def info(self):
        print(f'Name: {self.name} Hunger: {self.hungry} Right now, I feel like: {self.mood}')
        self.__pass_time()

    def give_food(self, food = 4):
        print('I have eaten!')
        self.hungry -= food
        if self.hungry < 0:
            self.hungry = 0
        self.__pass_time()


def main():
    name = input("Enter your animal's name: ")
    critter1 = Critter(name)
    choice = None
    while choice != '0':
        choice = input("0 - Exit\n1 - Recognize the animal's condition\n2 - Feed the animal\nEnter your choice: ")
        if choice == '1':
            critter1.info()
        elif choice == '2':
            critter1.give_food()
        elif choice == '0':
            print('Exiting the program...')
            time.sleep(2)
        else:
            print('Incorrect selection. Try again')

main()
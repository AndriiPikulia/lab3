import random

def random_array():
    array = []
    for i in range(5):
        for j in range(5):
            array = random.randint(1,99)
            print(f"-{array}-", " ", end='')
        print("\n")
    return array

def change_array():
    num = int(input("Введіть число від 1 до 99: "))
    if(num < 1 or num > 99):
        print("Число має бути більше 1 і менше 99")
        exit()

    array = []
    for i in range(5):
        for j in range(5):
            array = random.randint(1,99)
            if(array > num):
                print(f"*{array}*", " ", end='')
            else:
                print(f"-{array}-", " ", end='')
        print("\n")

random_array()
change_array()
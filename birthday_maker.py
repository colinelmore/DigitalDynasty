import random

class Birthday():
    def __init__(self):
        dates = {"Jan": 31, "Feb": 28, "Mar": 31, "Apr": 30, "May": 31, "June":30, "July":31, "Aug":31, "Sep": 30, "Oct":31, 
                 "Nov": 30, "Dec": 31}
        self._month = list(dates.keys())[random.randint(0,11)] 
        self._day = random.randint(1,dates[self._month])

    def __eq__(self, another) -> bool:
        return True if self._month == another._month and self._day == another._day else False

    def __str__(self):
        return f'{self._month} {self._day}'

def loadBirthdays(ammount: int):
    Birthday_list = []
    for i in range (ammount):
        Birthday_list.append(Birthday())
    return Birthday_list

def clear():
    import os
    os.system('cls')

if __name__ == '__main__':
    clear()
    new_birthdates = loadBirthdays(5)
    for birthday in new_birthdates:
        print(birthday)




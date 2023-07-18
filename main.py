import random

digits = 3
guesses = 10

def main():
    print('''
    Начинаем игру в Бейглз.
    Правила просты: 
    Я говорю "Пико!" - если одна цифра правильна, но она не на правильном месте.
    Говорю "Ферми!" - если цифра правильная, и она на правильном месте.
    Говорю "Бейглз!" - если нет правильных цифр вообще.
    ''')

    number = generate_number()
    
    for attempt in range(1, guesses+1):
        print(f'Попытка номер {attempt}')
        user_guess = input(f'Введи число: ')
        if len(str(user_guess)) == digits:
            list_u = list(str(user_guess))
            list_n = list(str(number))
            list_c = []
            for i in range(digits):
                if list_u[i] == list_n[i]:
                    list_c.append('Ферми!') 
                elif list_u[i] in list_n:
                    list_c.append('Пико!')
                else:
                    list_c.append('Бейгз!')
        else:
            print('Ты что-то намудрил с числом. Отнимаю попытку!')
        print(list_c)
        if list_c == ['Ферми!'] * digits:
            print(f'Победа! Ты молодец! Справился за {attempt} попыток!')
            break
    print(f'О-О! Попытки кончились! Ты проиграл! Число было - {number}')

def generate_number():
    lower = int(str("1"+('0'*(digits-1))))
    higher = int(str('9'*digits))
    number = random.randint(lower, higher)
    return number

if __name__ == "__main__":
    main()
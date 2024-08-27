# дані одного з читачів. Не змінювати!
student_card = {'номер': '324', 'прізвище': 'Іванов'} 
print("Ласкаво просимо!", student_card)



while True:
    cab = input("Особистий кабінет: 1 – взяти, 2 – повернути, 3 – додому")
    if cab == '1':
        pl = input("Введіть назву:")
        student_card['борг'] = pl
    elif cab == '2':
        if 'борг' in student_card:
            del student_card['борг']
    elif cab == '3':
        break
    else:
        print("Невірний вибір. Спробуйте ще раз.")
    print("Картка читача:", student_card)

print("Чекаємо на вас:", student_card)

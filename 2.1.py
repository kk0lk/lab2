"""
Задача №1

Компанія-виробник програмного забезпечення у сфері інформаційної
безпеки реалізує один комплект програм за 2700 гривень.
Якщо відбувається купівля декількох одиниць товару,працює система
знижок: 10-19 одиниць товару - 10%, 20-49 - 20%, 50-99 - 30%,
100 або більше - 40%. Напишіть програму, яка отримує від користувача
ціле число - кількість придбаних комплектів програмного забезпечення і
виводить повідомлення про суму знижки (якщо така є) та загальну суму при купівлі зі знижкою.

Виконала: Гриб Наталія Григорівна, 31І група
"""

n = int(input("Введіть кількість придбаних комплектів програмного забезпечення: "))
x = 2700

if 10 <= n <20:
    print('Сума придбаних комплектів ПЗ =',n*(x*0.1),'\n','Сума знижки = 10%')
elif 20<= n < 50:
    print('Сума придбаних комплектів ПЗ =',n*(x*0.2),'\n','Сума знижки = 20%')
elif 50 <= n < 100:
    print('Сума придбаних комплектів ПЗ =',n*(x*0.3),'\n','Сума знижки = 30%')
elif 100 < n:
    print('Сума придбаних комплектів ПЗ =',n*(x*0.4),'\n','Сума знижки = 40%')
else:
    print('Сума придбаних комплектів ПЗ =',n*x)
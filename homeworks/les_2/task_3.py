"""
Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
"""

seasons_list = ('зима',
                'весна',
                'лето',
                'осень',
                )

seasons_dict = {'зима': (12, 1, 2),
                'весна': (3, 4, 5),
                'лето': (6, 7, 8),
                'осень': (9, 10, 11),
                }

seasons_dict2 = {
    1: 'зима',
    2: 'зима',
    3: 'весна',
    4: 'весна',
    5: 'весна',
    6: 'лето',
    7: 'лето',
    8: 'лето',
    9: 'осень',
    10: 'осень',
    11: 'осень',
    12: 'зима',
}

user_month_num = 12

season_idx = user_month_num // 3 % 4

for key, value in seasons_dict.items():
    if user_month_num in value:
        print(key)
        break

print(season_idx)
print(seasons_list[season_idx])

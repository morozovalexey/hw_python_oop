from homework import *

# Code for testing
print("Проверяем деньги")
money_make = CashCalculator(50000)
r1 = Record(12000, comment="на телефон")
r2 = Record(20000)

money_make.add_record(r1)
money_make.add_record(r2)
print(money_make.get_today_cash_remained())
print(money_make.get_week_stats())
print(money_make.get_today_stats())

print()
print()
print("Проверяем еду")
food_cal = CaloriesCalculator(3000)
r_1 = Record(1200, comment="скушал", date="25.11.2020")
r_2 = Record(1000)

food_cal.add_record(r_1)
food_cal.add_record(r_2)
print(food_cal.get_calories_remained())
print(food_cal.get_week_stats())
print(food_cal.get_today_stats())
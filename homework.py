import datetime as dt

DATE_FORMAT = '%d.%m.%Y'
CURRENT_TRADE = {
    "eur": [90, "Euro"],
    "usd": [80, "USD"],
    "rub": [1, "руб"]
}


class Calculator:
    def __init__(self):
        self.records = []

    def add_record(self, record_name):
        self.records.append(record_name)

    def remained(self, day_limit):
        today = day_today()
        print(today)
        spent = self.stats(today, today)
        print(spent)
        return day_limit - spent

    def stats(self, start_day, end_day):
        result = 0
        for record in self.records:
            print([record.amount, record.date, record.comment])
            if ((start_day >= end_day)
                    and (start_day <= end_day)):
                result = result + record.amount
        return result


class CashCalculator(Calculator):
    def __init__(self, day_limit):
        super().__init__()
        self.day_limit = day_limit

    def add_record(self, record):
        super().add_record(record)
        print("--- Вы внесли запись о расходе ---")
        print(f"{record.date} потрачено {record.amount}. Комментарий: {record.comment}")
        pass

    def get_today_cash_remained(self, currency='rub'):
        rubbls_remaiund = super().remained(self.day_limit)
        result = rubbls_remaiund / CURRENT_TRADE[currency][0]
        if currency not in CURRENT_TRADE:
            print(f"К сожалению, в нашем калькуляторе валюта {currency} пока не поддерживается")
        if result > 0:
            return 'На сегодня осталось {:.2f} {}'.format((CURRENT_TRADE[currency][0] * result),
                                                              CURRENT_TRADE[currency][1])
        elif result == 0:
            return "Денег нет, держись"
        else:
            return 'Денег нет, держись: твой долг - {}'.format((CURRENT_TRADE[currency][0] * result),
                                                          CURRENT_TRADE[currency][1])

    def get_week_stats(self):
        end_day = day_today()
        start_day = end_day - dt.timedelta(days=7)
        result = super().stats(start_day, end_day)
        return "За последние 7 дней вы израсходовали {:.2f} рублей".format(result)


class CaloriesCalculator(Calculator):
    def __init__(self, day_limit):
        super().__init__()
        self.day_limit = day_limit

    def add_record(self, record):
        super().add_record(record)
        print("--- Вы покушали ---")
        print(f"{record.date} скушано {record.amount} кКал. Комментарий: {record.comment}")

    def get_calories_remained(self):
        result = super().remained(self.day_limit)
        if result > 0:
            return 'Сегодня можно съесть что-нибудь ещё, но'\
                   ' с общей калорийностью не более {} кКал'.format(result)
        else:
            return "Хватит есть!"

    def get_week_stats(self):
        end_day = day_today()
        start_day = end_day - dt.timedelta(days=7)
        result = super().stats(start_day, end_day)
        return "За последние 7 дней вы получили {} каллорий".format(result)


class Record:
    def __init__(self, amount, date="", comment="запись без комментария"):
        self.amount = amount
        if date == "":
            self.date = day_today()
        else:
            self.date = dt.datetime.strptime(date, DATE_FORMAT)
        self.comment = comment


def day_today():
    date = dt.datetime.now().date()
    return date


# Code for testing
print("Проверяем деньги")
money_make = CashCalculator(50000)
r1 = Record(12000, comment="на телефон")
r2 = Record(20000)

money_make.add_record(r1)
money_make.add_record(r2)
print(money_make.get_today_cash_remained())
print(money_make.get_week_stats())

print()
print()
print("Проверяем еду")
food_cal = CaloriesCalculator(3000)
r_1 = Record(1200, comment="скушал")
r_2 = Record(1000)

food_cal.add_record(r1)
food_cal.add_record(r2)
print(food_cal.get_calories_remained())
print(food_cal.get_week_stats())
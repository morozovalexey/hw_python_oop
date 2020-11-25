import datetime as dt

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
        today = dt.datetime.now().date()
        spent = self.get_stats(today, today)
        print(spent)
        return day_limit - spent

    def get_stats(self, start_day, end_day):
        result = 0
        for record in self.records:
            print([record.amount, record.date, record.comment])
            if ((start_day >= end_day)
                    and (start_day <= end_day)):
                result = result + record.amount
        return result


class CashCalculator(Calculator):
    EURO_RATE = [90, "Euro"]
    USD_RATE = [70, "USD"]

    CURRENT_TRADE = {
        "eur": EURO_RATE,
        "usd": USD_RATE,
        "rub": [1, "руб"]
    }

    def __init__(self, day_limit):
        super().__init__()
        self.day_limit = day_limit


    def add_record(self, record):
        super().add_record(record)
        #print("--- Вы внесли запись о расходе ---")
        #print(f"{record.date} потрачено {record.amount}. Комментарий: {record.comment}")
        pass

    def get_today_cash_remained(self, currency='rub'):
        rub_remained = super().remained(self.day_limit)
        result = rub_remained / CURRENT_TRADE[currency][0]
        if currency not in CURRENT_TRADE:
            return f"К сожалению, в нашем калькуляторе валюта {currency} пока не поддерживается"
        if result > 0:
            return 'На сегодня осталось {:.2f} {}'.format((self.CURRENT_TRADE[currency][0] * result),
                                                              self.CURRENT_TRADE[currency][1])
        elif result == 0:
            return "Денег нет, держись"
        else:
            return 'Денег нет, держись: твой долг - {:.2f} {}'.format((CURRENT_TRADE[currency][0] * result * (-1)),
                                                          CURRENT_TRADE[currency][1])

    def get_week_stats(self):
        end_day = dt.datetime.now().date()
        start_day = end_day - dt.timedelta(days=7)
        result = super().get_stats(start_day, end_day)
        return "За последние 7 дней вы израсходовали {:.2f} рублей".format(result)


class CaloriesCalculator(Calculator):
    def __init__(self, day_limit):
        super().__init__()
        self.day_limit = day_limit

    def add_record(self, record):
        super().add_record(record)
        #print("--- Вы покушали ---")
        #print(f"{record.date} скушано {record.amount} кКал. Комментарий: {record.comment}")

    def get_calories_remained(self):
        result = super().remained(self.day_limit)
        if result > 0:
            return 'Сегодня можно съесть что-нибудь ещё, но'\
                   ' с общей калорийностью не более {} кКал'.format(result)
        else:
            return "Хватит есть!"

    def get_week_stats(self):
        end_day = dt.datetime.now().date()
        start_day = end_day - dt.timedelta(days=7)
        result = super().get_stats(start_day, end_day)
        return "За последние 7 дней вы получили {} каллорий".format(result)


class Record:
    DATE_FORMAT = '%d.%m.%Y'
    def __init__(self, amount, date="", comment="запись без комментария"):
        self.amount = amount
        if date == "":
            self.date = dt.datetime.now().date()
        else:
            self.date = dt.datetime.strptime(date, self.DATE_FORMAT)
        self.comment = comment
        print(self.date)
        print(type(self.date))






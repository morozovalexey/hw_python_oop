import datetime as dt


class Calculator:
    def __init__(self, limit=0):
        self.records = []
        self.limit = limit

    def add_record(self, record_name):
        self.records.append(record_name)

    def remained(self, day_limit):
        spent = self.get_stats()
        return day_limit - spent

    def get_stats(self, start_day=dt.datetime.now().date(), end_day=dt.datetime.now().date()):
        result = 0
        for record in self.records:
            if ((record.date >= start_day)
                    and (record.date <= end_day)):
                result = result + record.amount
        return result

    def get_today_stats(self):
        result = self.get_stats()
        return result

    def get_week_stats(self):
        start_day = dt.datetime.now().date() - dt.timedelta(days=7)
        result = self.get_stats(start_day=start_day)
        return result


class CashCalculator(Calculator):
    EURO_RATE = 70.00
    USD_RATE = 60.00
    CURRENT_TRADE = {
        "eur": [EURO_RATE, "Euro"],
        "usd": [USD_RATE, "USD"],
        "rub": [1, "руб"]
    }

    def add_record(self, record):
        super().add_record(record)
        print("--- Вы внесли запись о расходе ---")
        print(f"{record.date} потрачено {record.amount}. Комментарий: {record.comment}")
        pass

    def get_today_cash_remained(self, currency='rub'):
        rub_remained = super().remained(self.limit)
        result = round((rub_remained / self.CURRENT_TRADE[currency][0]), 2)
        if currency not in self.CURRENT_TRADE:
            return f"К сожалению, в нашем калькуляторе валюта {currency} пока не поддерживается"
        if result > 0:
            return 'На сегодня осталось {:.2f} {}'.format(result,
                                                          self.CURRENT_TRADE[currency][1])
        elif result == 0:
            return "Денег нет, держись"
        else:
            return 'Денег нет, держись: твой долг - {:.2f} {}'.format(result * (-1),
                                                                      self.CURRENT_TRADE[currency][1])

    def get_week_stats(self):
        result = super().get_week_stats()
        return "За последние 7 дней вы израсходовали {:.2f} рублей".format(result)

    def get_today_stats(self):
        result = super().get_today_stats()
        return "За сегодня вы израсходовали {:.2f} рублей".format(result)


class CaloriesCalculator(Calculator):

    def add_record(self, record):
        super().add_record(record)
        print("--- Вы покушали ---")
        print(f"{record.date} скушано {record.amount} кКал. Комментарий: {record.comment}")

    def get_calories_remained(self):
        result = super().remained(self.limit)
        if result > 0:
            return 'Сегодня можно съесть что-нибудь ещё, но' \
                   ' с общей калорийностью не более {} кКал'.format(result)
        else:
            return "Хватит есть!"

    def get_week_stats(self):
        result = super().get_week_stats()
        return "За последние 7 дней вы получили {} каллорий".format(result)

    def get_today_stats(self):
        result = super().get_today_stats()
        return "За сегодня вы получили {} каллорий".format(result)


class Record:
    DATE_FORMAT = '%d.%m.%Y'

    def __init__(self, amount, date="", comment="запись без комментария"):
        self.amount = amount
        if date == "":
            self.date = dt.datetime.now().date()
        else:
            self.date = dt.datetime.strptime(date, self.DATE_FORMAT).date()
        self.comment = comment

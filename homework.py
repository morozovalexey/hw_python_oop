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

    #
    def stats(self, start_day, end_day):
        start_day_date = dt.datetime.strptime(start_day, DATE_FORMAT).date()
        end_day_date = dt.datetime.strptime(end_day, DATE_FORMAT).date()
        result = 0
        for record in self.records:
            print([record.amount, record.date, record.comment])
            if ((dt.datetime.strptime(record.date, DATE_FORMAT).date() >= start_day_date)
                    and (dt.datetime.strptime(record.date, DATE_FORMAT).date() <= end_day_date)):
                result = result + record.amount
        return result


class cashCalculator(Calculator):
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

        pass


class callaoryCalculator(Calculator):
    def __int__(self):
        super().__init__()
        self.day_limit = day_limit

    def 


class Record:
    def __init__(self, amount, date="", comment="запись без комментария"):
        self.amount = amount
        if date == "":
            self.date = day_today()
        else:
            self.date = date
        self.comment = comment


def day_today():
    moment = dt.datetime.now()
    date = dt.datetime.strftime(moment, DATE_FORMAT)
    return date


# Code for testing
money_make = cashCalculator(50000)
r1 = Record(12000,comment="на телефон")
r2 = Record(20000)

money_make.add_record(r1)
money_make.add_record(r2)
print(money_make.get_today_cash_remained())
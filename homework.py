import datetime as dt



DATE_FORMAT = '%d.%m.%Y'
CURRENT_TRADE = {
    "eur": 90,
    "usd": 80
}



class Calculator:
    def __init__(self):
        self.records = []


    def add_record(self, record_name):
        self.records.append(record_name)


    def remained(self, day_limit):
        today = day_today()
        spent = self.stats(today,today)
        return day_limit - spent


    def stats(self, start_day, end_day):
        start_day_date = dt.datetime.strptime(start_day, DATE_FORMAT).date()
        end_day_date = dt.datetime.strptime(end_day, DATE_FORMAT),date()
        result = 0
        for record in records:
            if dt.datetime.strptime(record.date, DATE_FORMAT) in (start_day_date, end_day_date):
                result = result + record.amount
        return result



class cashCalculator(Calculator):
    def __init__(self, day_limit):
        super().__init__()
        self.day_limit = day_limit


    def add_record(self, record):
        super().add_record(record)
        result = {
            "data": record.date,
            "amount": record.amount,
            "comment": record.comment,
            "type": "money"
        }
        data_base.append(result)
        print("--- Вы внесли запись о расходе ---")
        print(f"{record.date} потрачено {record.money}. Комментарий: {record.comment}")
        pass


    def get_today_cash_remained(self, currency):
        if currency == "eur":

            pass
        elif currency == "usd":
            pass
        elif currency == "rub":
            pass
        else:
            print(f"К сожалению, в нашем калькуляторе валюта {currency} пока не поддерживается")


    def get_week_stats(self):

    pass

class callaoryCalculator(Calculator):
    def __int__(self):


    pass

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
    date = dt.datetime.strftime(moment, date_format)
    return date
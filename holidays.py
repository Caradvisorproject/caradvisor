from datetime import date

holiday_days = [
                '01-01',
                '02-01',
                '03-01',
                '04-01',
                '05-01',
                '06-01',
                '07-01',
                '08-01',
                '23-02',
                '08-03',
                '01-05',
                '09-01',
                '12-06',
                '04-11'
]

def get_holiday():
    """Cheking if today is holiday"""

    today = date.today()
    today = today.strftime("%d-%m-%Y")

    if today[:-5] in holiday_days:
        return True

    else:
        return False

print(get_holiday())


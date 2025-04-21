from datetime import datetime

def get_days_from_today(date_str):
    
    try:
        inp_date = datetime.strptime(date_str, "%Y-%m-%d").date()
        today = datetime.today().date()
        delta = (today - inp_date).days
        return delta
    except ValueError:
        print("Неправильний формат дати. Спробуйте ще раз.")

print(get_days_from_today("2025-01-01"))
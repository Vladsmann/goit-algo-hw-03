from datetime import datetime

def get_date_from_input():
    date_str = input("Для розрахунку кількості днів між поточною та заданою датою, задайте дату у форматі РРРР-ММ-ДД: ")
    try:
        inp_date = datetime.strptime(date_str, "%Y-%m-%d").date()
        today = datetime.today().date()
        delta = (today - inp_date).days
        print(f"Різниця складає: {delta} днів")
    except ValueError:
        print("Неправильний формат дати. Спробуйте ще раз.")

get_date_from_input()
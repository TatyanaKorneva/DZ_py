n=int(input())
if 6<=n<=7:
        print("Выходной день")
    elif 0 < n < 6:
        print("Рабочий день")
    else:
        print("Число вне 7 дней")


def day_week(n):
    if 6<=n<=7:
        return "Выходной день"
    elif 0 < n < 6:
        return "Рабочий день"
    else:
        return "Число вне пределов 7 дней"
print(day_week(17))

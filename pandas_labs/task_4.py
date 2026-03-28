import pandas as pd

# загрузка данных
df = pd.read_csv("5 train.csv")

# ============= ЗАДАЧА 4: Средняя температура и среднее число поездок по каждому месяцу.  Сохранение в CSV таблицу =============

df["datetime"] = pd.to_datetime(df["datetime"])

monthly_stats = df.groupby(df["datetime"].dt.month).agg({
    "temp": "mean",
    "count": "mean"
}).round(1)

# Переименовываем месяцы
month_names = {
    1: "Январь",
    2: "Февраль",
    3: "Март",
    4: "Апрель",
    5: "Май",
    6: "Июнь",
    7: "Июль",
    8: "Август",
    9: "Сентябрь",
    10: "Октябрь",
    11: "Ноябрь",
    12: "Декабрь"
}

monthly_stats.index = [month_names[i] for i in monthly_stats.index]
monthly_stats.columns = ["Средняя температура", "Среднее число поездок"]

# Заменяем точку на запятую для чисел
monthly_stats = monthly_stats.astype(str)
for col in monthly_stats.columns:
    monthly_stats[col] = monthly_stats[col].str.replace('.', ',')

# Сохраняем в CSV
monthly_stats.to_csv("monthly_stats.csv", sep=";", encoding="utf-8-sig")

print("Файл сохранён: monthly_stats.csv")
print(monthly_stats)
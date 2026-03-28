import pandas as pd

# Загружаем данные
df = pd.read_csv("5 train.csv")
df["datetime"] = pd.to_datetime(df["datetime"])

# ============= ЗАДАЧА 1: Час суток с максимальным числом поездок в выходные дни =============

# Фильтруем выходные дни
weekend = df[df["workingday"] == 0]

# Группируем по часам
hourly = weekend.groupby(weekend["datetime"].dt.hour)["count"].mean()

# Находим максимальный час
max_hour = hourly.idxmax()
max_value = hourly.max()

print(f"Час с максимальным числом поездок в выходные: {max_hour}:00")
print(f"Среднее число поездок: {max_value:.0f}")
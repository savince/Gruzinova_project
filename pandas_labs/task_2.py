import pandas as pd
import matplotlib.pyplot as plt

# загрузка данных
df = pd.read_csv("5 train.csv")

# ============= ЗАДАЧА 2: Столбчатая диаграмма (casual и registered по сезонам) =============

season_stats = df.groupby("season").agg({
    "casual": "mean",
    "registered": "mean"
})

season_stats.index = ["Зима", "Весна", "Лето", "Осень"]

# создаем 2 графика рядом
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# диаграмма casual
ax1.bar(season_stats.index, season_stats["casual"], color="coral")
ax1.set_title("Среднее число поездок casual по сезонам")
ax1.set_xlabel("Сезон")
ax1.set_ylabel("Среднее число поездок")

# диаграмма registered
ax2.bar(season_stats.index, season_stats["registered"], color="steelblue")
ax2.set_title("Среднее число поездок registered по сезонам")
ax2.set_xlabel("Сезон")
ax2.set_ylabel("Среднее число поездок")

plt.tight_layout()
plt.show()
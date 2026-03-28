import pandas as pd

# загрузка данных
df = pd.read_csv("5 train.csv")

# ============= ЗАДАЧА 3: Фильтр: наблюдения, где count > 500 =============

big_rides = df[df["count"] > 500]

print("Количество наблюдений:", len(big_rides))

season_counts = big_rides["season"].value_counts()

season_names = {
    1: "Зима",
    2: "Весна",
    3: "Лето",
    4: "Осень"
}

season_counts.index = season_counts.index.map(season_names)

# Находим сезон с максимумом
max_season = season_counts.idxmax()
max_count = season_counts.max()

print(f"Чаще всего count > 500 бывает: {max_season} ({max_count} наблюдений)")
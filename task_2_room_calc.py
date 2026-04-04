# ============= ЗАДАЧА 2: Параметры помещения =============

# Исходные данные
length = 6.0   # длина комнаты в метрах
width = 3.0    # ширина комнаты в метрах
height = 3.0   # высота комнаты в метрах
price = 125  # стоимость покраски 1 м² (руб)

# ============= РАСЧЁТЫ =============

# Площадь пола
floor_area = length * width

# Площадь стен (2 стены по длине + 2 стены по ширине)
walls_area = 2 * (length * height) + 2 * (width * height)

# Объём помещения
volume = length * width * height

# Стоимость покраски стен
painting_cost = walls_area * price

# ============= ОКРУГЛЕНИЕ =============

floor_area = round(floor_area, 2)
walls_area = round(walls_area, 2)
volume = round(volume, 2)
painting_cost = round(painting_cost, 2)

# ============= ВЫВОД РЕЗУЛЬТАТОВ =============

print("ЗАДАЧА 2: Параметры помещения")
print("=" * 50)
print(f"Длина помещения:     {length} м")
print(f"Ширина помещения:    {width} м")
print(f"Высота помещения:    {height} м")
print("-" * 50)
print(f"Площадь пола:        {floor_area} м²")
print(f"Площадь стен:        {walls_area} м²")
print(f"Объём помещения:     {volume} м³")
print("-" * 50)
print(f"Стоимость покраски стен:   {painting_cost} руб.")


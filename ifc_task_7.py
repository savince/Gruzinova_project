import ifcopenshell

filepath = "Example_1.ifc"

model = ifcopenshell.open(filepath)

# Получаем все двери IfcDoor
doors = model.by_type("IfcDoor")

# Задаем критерий фильтрации (ширина больше или равна порогу)
min_width = 900

# Собираем двери, удовлетворяющие критерию
filtered_doors = []
for door in doors:
    width = getattr(door, "OverallWidth", None)
    if width is not None and width >= min_width:
        filtered_doors.append(door)

# Создаем новую пустую модель с той же схемой, что и исходная
new_model = ifcopenshell.file(schema=model.schema)

# Копируем в новую модель только отфильтрованные двери
for door in filtered_doors:
    new_model.add(door)

# Сохраняем подмодель
output_filename = f"_doors_wide_{min_width}.ifc"
new_model.write(output_filename)

# Проверяем результат: открываем созданный файл и выводим количество дверей
check_model = ifcopenshell.open(output_filename)
check_doors = check_model.by_type("IfcDoor")

print(f"Создан файл: {output_filename}")
print(f"Количество дверей в подмодели: {len(check_doors)}")

# Проверяем, что все двери удовлетворяют критерию
all_valid = True
for door in check_doors:
    width = getattr(door, "OverallWidth", None)
    if width is None or width < min_width:
        all_valid = False
        break

if all_valid:
    print(f"Проверка: все {len(check_doors)} дверей имеют ширину >= {min_width}")
else:
    print("Ошибка: найдены двери, не удовлетворяющие критерию")
import ifcopenshell

# Путь к файлу
filepath = "Example_1.ifc"

# Открываем модель
model = ifcopenshell.open(filepath)

# Получаем все стены
walls = model.by_type("IfcWall")

# Выводим количество стен
print(f"Количество стен в модели: {len(walls)}")
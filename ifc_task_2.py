import ifcopenshell

filepath = "Example_1.ifc"

model = ifcopenshell.open(filepath)

# Получаем все элементы типа IfcWall
walls = model.by_type("IfcWall")

# Выводим общее количесво стен
print(f"Количество стен в модели: {len(walls)}")

# Получаем первый элемент
first_wall = walls[0]

# Информация об этом элементе
print(f"GlobalId: {first_wall.GlobalId}")
print(f"Name: {first_wall.Name}")
print(f"ObjectType: {getattr(first_wall, 'ObjectType', None)}")
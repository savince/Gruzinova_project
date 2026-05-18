import ifcopenshell

filepath = "Example_1.ifc"

model = ifcopenshell.open(filepath)

# Получаем используемую схему IFC
print(f"Схема IFC: {model.schema}")

# Получаем все объекты типа IfcBuildingStorey (этажи)
storeys = model.by_type("IfcBuildingStorey")

# Выводим количество найденных этажей
print(f"Количество этажей: {len(storeys)}")

# Для каждого этажа выводим имя и отметку
for storey in storeys:
    elevation = getattr(storey, "Elevation", None)
    print(f"Этаж: {storey.Name}, Elevation={elevation}")

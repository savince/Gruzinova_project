student_name = "Алексия Грузинова"
group_number = 501
project_name = "ЖК Аквилон"  
floors = 45
height = 4 
is_residential = True
construction_year = 2003

total_height = floors * height  

print(f"== ПАСПОРТ СТРОИТЕЛЬНОГО ОБЪЕКТА ==\n"
      f"Составитель: {student_name}\n"
      f"Группа: {group_number}\n"
      f"Объект: {project_name}\n"
      f"Этажность: {floors} этажей\n"
      f"Высота: {total_height} м\n"
      f"Тип: {'Жилой' if is_residential else 'Нежилой'}\n"
      f"Год постройки: {construction_year}")

# Московский просп., 73, корп. 6, Санкт-Петербург (этаж 1-2)
# Этот объект - первое, что пришло голову
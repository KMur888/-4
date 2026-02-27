color1 = input("Введите первый цвет (красный, синий, желтый): ")
color2 = input("Введите второй цвет (красный, синий, желтый): ")

if (color1 == "красный" or color1 == "синий" or color1 == "желтый") and \
   (color2 == "красный" or color2 == "синий" or color2 == "желтый"):
    
    if (color1 == "красный" and color2 == "синий") or (color1 == "синий" and color2 == "красный"):
        print("фиолетовый")
    elif (color1 == "красный" and color2 == "желтый") or (color1 == "желтый" and color2 == "красный"):
        print("оранжевый")
    elif (color1 == "синий" and color2 == "желтый") or (color1 == "желтый" and color2 == "синий"):
        print("зеленый")
    else:
        print(f"При смешивании {color1} и {color2} получается тот же цвет")
        
else:

    print("Ошибка: введите только основные цвета (красный, синий, желтый)")

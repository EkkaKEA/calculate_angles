import math


def calculate_angles(x, y, L1, L2, L3):

    # Ограничения на досягаемость точки B
    L_max = L1 + L2
    L_min = abs(L1 - L2)

    # Расстояние между точками O и B
    ob = math.sqrt((x-L3)*(x-L3) + y*y)

    # Проверка плечей
    if (L1<0) or (L2<0) or (L3<0):
        return "Ошибка: Длина плеч не должна быть отрицательной"

    # Проверка ограничения по расстоянию
    if ob > L_max:
        return "Ошибка: Точка находится слишком далеко от основания."
    elif ob < L_min:
        return "Ошибка: Точка находится слишком близко к основанию."




    # Угол OAB (из треугольника с вершинами O, A, B)
    cos_value =(L1*L1 + L2*L2 - ob*ob ) / (2*L1*L2)
    if cos_value > 1.0:
        cos_value = 1.0
    elif cos_value < -1.0:
        cos_value = -1.0
    oab = math.acos(cos_value)


    # Угол AOB (из треугольника с вершинами O, A, B)
    cos_value =(L1*L1 - L2*L2 + ob*ob) / (2*L1*ob)
    if cos_value > 1.0:
        cos_value = 1.0
    elif cos_value < -1.0:
        cos_value = -1.0
    aob = math.acos(cos_value)


    # Угол θ1
    if (x - L3) == 0:
        theta1 = math.pi / 2  # Если x - L3 = 0, то это вертикальное положение
    else:
        theta1 = math.atan2(y, (x - L3)) - aob

    # Угол θ2
    theta2 = math.pi -oab

    # Угол θ3
    theta3 = theta2 + theta1

    return {
        "theta1": math.degrees(theta1),
        "theta2": math.degrees(theta2),
        "theta3": math.degrees(theta3)
    }


# Ввод данных:
x = float(input("Введите координату x: "))
y = float(input("Введите координату y: "))
L1 = float(input("Введите длину L1: "))
L2 = float(input("Введите длину L2: "))
L3 = float(input("Введите длину L3: "))

result = calculate_angles(x, y, L1, L2, L3)

if isinstance(result, dict):
    print(f"Угол θ1: {result['theta1']:.2f}°")
    print(f"Угол θ2: {result['theta2']:.2f}°")
    print(f"Угол θ3: {result['theta3']:.2f}°")
else:
    print(result)

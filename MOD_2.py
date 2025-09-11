#Модуль с функцией пересчета углов в коэффициенты (косинус и синус) и коэффициентов в углы

from MOD_0 import *
import math as m
import numpy as np

k_cos = [] #Пустой список для значений косинусов
k_sin = [] #Пустой список для значений синусов
angles = [] #Пустой список для значений углов
def angle_kt(num_1, num_2):
    #Пересчет углов в коэффициенты
    if zapros_2 == 1:
        # вычисление угла до реверса, перевод градусов в радианы при реверсивном режиме
        if zapros_4 == 1:
            num_1_unrev = (num_1 + 180)
            if num_1_unrev > 360:
                num_1_unrev = num_1_unrev - 360
            num_2_unrev = (num_2 + 180)
            if num_2_unrev > 360:
                num_2_unrev = num_2_unrev - 360
            num_1 = np.deg2rad(num_1)
            num_2 = np.deg2rad(num_2)
        else:
            #Перевод градусов в радианы
            num_1 = np.deg2rad(num_1)
            num_2 = np.deg2rad(num_2)
        #Вычисление косинусов от углов, полученных в радианах
        c_fiA = m.cos(num_1)
        c_fiC = m.cos(num_2)
        #Вычисление синусов от углов, полученных в радианах
        s_fiA = m.sin(num_1)
        s_fiC = m.sin(num_2)
        #Восстановление углов в градусном значении для корректного заполнения списка
        num_1 = np.rad2deg(num_1)
        num_2 = np.rad2deg(num_2)

        #Вывод значений для контроля
        print("------------------------------------------------------------\n"
              "        Этап контроля: углы -> коэффициенты\n"
              "------------------------------------------------------------\n")
        print("Значения углов равны:")
        print(f"Угол Fi для ф.А {num_1}°\n"
              f"Угол Fi для ф.С {num_2}°\n")
        if zapros_4 == 1:
            print("Значения углов до реверса равны:")
            print(f"Угол Fi до реверса ф.А: {num_1_unrev}°\n"
                  f"Угол Fi до реверса ф.С: {num_2_unrev}°\n")
        print("Значения коэффициентов равны:")
        print(f"Косинус угла Fi для ф.А: {c_fiA}\n"
              f"Косинус угла Fi для ф.С: {c_fiC}\n")
        print("Значения синусов, равны:")
        print(f"Синус угла Fi для ф.А: {s_fiA}\n"
              f"Синус угла Fi для ф.С: {s_fiC}\n")
        if zapros_4 == 1:
            print("Для источника мощности выбран реверсивный режим работы")
        elif zapros_4 != 1:
            print("Для источника мощности выбран прямой режим работы")

        #Заполнение пустых списков
        k_sin.append(s_fiA)
        k_sin.append(s_fiC)
        k_cos.append(c_fiA)
        k_cos.append(c_fiC)
        angles.append(num_1)
        angles.append(num_2)


    #Пересчет коэффициентов в углы
    elif zapros_2 == 2:
        #Индуктивная нагрузка (L)
        if zapros_3 == 1:
            angle_fiA_faz = np.acos(num_1)
            angle_fiC_faz = np.acos(num_2)
            if zapros_4 == 1:
                # Получение значения угла до реверса, пересчет введенного угла в радианы
                angle_fiA_faz_unrev = np.rad2deg(angle_fiA_faz)
                if np.rad2deg(angle_fiA_faz) > 90:
                    angle_fiA_faz_unrev = 180 - np.rad2deg(angle_fiA_faz)
                angle_fiC_faz_unrev = 180 - np.rad2deg(angle_fiC_faz)
                angle_fiA_faz = 360 - np.rad2deg(angle_fiA_faz)
                angle_fiC_faz = 360 - np.rad2deg(angle_fiC_faz)
            if zapros_4 != 1:
                #Пересчет углов, полученных в радианах, в градусные значения для индуктивной нагрузки
                angle_fiA_faz = np.rad2deg(angle_fiA_faz)
                angle_fiC_faz = np.rad2deg(angle_fiC_faz)
            s_fiA = m.sin(np.deg2rad(angle_fiA_faz))
            s_fiC = m.sin(np.deg2rad(angle_fiC_faz))

        #Емкостная нагрузка(C)
        if zapros_3 == 2:
            angle_fiA_faz = np.acos(num_1)
            angle_fiC_faz = np.acos(num_2)
            if zapros_4 == 1:
                # Получение значения угла до реверса, пересчет введенного угла в радианы
                angle_fiA_faz_unrev = np.rad2deg(angle_fiA_faz) + 180
                angle_fiC_faz_unrev = np.rad2deg(angle_fiC_faz) + 180
                angle_fiA_faz = np.rad2deg(angle_fiA_faz)
                angle_fiC_faz = np.rad2deg(angle_fiC_faz)
            if zapros_4 != 1:
                #Пересчет углов, полученных в радианах, в градусные значения для емкостной нагрузки
                angle_fiA_faz = 360 - np.rad2deg(angle_fiA_faz)
                angle_fiC_faz = 360 - np.rad2deg(angle_fiC_faz)
            s_fiA = m.sin(np.deg2rad(angle_fiA_faz))
            s_fiC = m.sin(np.deg2rad(angle_fiC_faz))

        #Активно-индуктивная нагрузка (1.0L)
        if zapros_3 == 3:
            # пересчет углов, полученных в радианах, в градусные значения для активной нагрузки
            angle_fiA_faz = np.acos(num_1)
            angle_fiC_faz = np.acos(num_2)
            if zapros_4 == 1:
                #Получение значения угла до реверса, пересчет введенного угла в радианы
                angle_fiA_faz_unrev = np.rad2deg(angle_fiA_faz) - 120
                angle_fiC_faz_unrev = np.rad2deg(angle_fiC_faz) + 180
                angle_fiA_faz = 360 - np.rad2deg(angle_fiA_faz)
                angle_fiC_faz = np.rad2deg(angle_fiC_faz)
            if zapros_4 != 1:
                angle_fiA_faz = np.rad2deg(angle_fiA_faz)
                angle_fiC_faz = 360 - np.rad2deg(angle_fiC_faz)
            s_fiA = np.sin(np.deg2rad(angle_fiA_faz))
            s_fiC = np.sin(np.deg2rad(angle_fiC_faz))

        #Вывод значений для контроля
        print("------------------------------------------------------------\n"
              "            Этап контроля: коэффициенты -> углы\n"
              "------------------------------------------------------------")
        if zapros_3 == 1 or zapros_3 == 2 or zapros_3 == 3:
            print("Значения коэффициентов равны:")
            print(f"Косинус угла Fi для ф.А: {num_1}\n"
                  f"Косинус угла Fi для ф.С: {num_2}\n")
            print("Значения углов равны:")
            print(f"Угол Fi для ф.А равен:   {round((angle_fiA_faz), 3)}°\n"
                  f"Угол Fi для ф.С равен:   {round((angle_fiC_faz), 3)}°\n")
            if zapros_4 == 1:
                print("Значения углов до реверса равны:")
                print(f"Угол Fi до реверса ф.А: {angle_fiA_faz_unrev}°\n"
                      f"Угол Fi до реверса ф.С: {angle_fiC_faz_unrev}°\n")
            print("Значения синусов, равны:")
            print(f"Синус угла Fi для ф.А:   {round(s_fiA, 3)}\n"
                  f"Синус угла Fi для ф.С:   {round(s_fiC, 3)}\n")

        #Вывод режима направления протекания тока
        if zapros_4 == 1:
            print("Для источника мощности выбран реверсивный режим работы")
        elif zapros_4 != 1:
            print("Для источника мощности выбран прямой режим работы")

        #Заполнение пустых списков
        k_sin.append(s_fiA)
        k_sin.append(s_fiC)
        k_cos.append(num_1)
        k_cos.append(num_2)
        angles.append(angle_fiA_faz)
        angles.append(angle_fiC_faz)



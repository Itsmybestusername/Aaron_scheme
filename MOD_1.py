#Модуль с функцией пересчета линейных напряжений в фазные и фазных напряжений в линейные
from MOD_0 import *

u_faz = [] #Пустой список для фазных напряжений
u_lin = [] #ПУстой список для фазных напряжений
def voltage_calc(u_1, u_2, u_3):
    #Пересчет линейных напряжений в фазные
    if zapros_1 == 1:
        u_An = u_1 / CF
        u_Bn = u_3 / CF
        u_Cn = u_2 / CF
        #Заполнение пустых списков
        u_faz.append(u_An)
        u_faz.append(u_Bn)
        u_faz.append(u_Cn)
        u_lin.append(u_1)
        u_lin.append(u_3)
        u_lin.append(u_2)
        print(f"Введенные значения линейных напряжений:\n"
              f"Линейное напряжение Uab = {u_1}B\n"
              f"Линейное напряжение Ubc = {u_3}B\n"
              f"Линейное напряжение Uca = {u_2}B\n")
        print(f"Значения фазных напряжений равны:\n"
              f"Фазное напряжение Uao = {round(u_An, 3)}B\n"
              f"Фазное напряжение Ubo = {round(u_Bn, 3)}B\n"
              f"Фазное напряжение Uco = {round(u_Cn, 3)}B\n")

    # Пересчет фазных напряжений в линейные
    else:
        u_Ab = u_1 * CF
        u_Bc = u_3 * CF
        u_Ca = u_2 * CF
        #Заполнение пустых списков
        u_lin.append(u_Ab)
        u_lin.append(u_Bc)
        u_lin.append(u_Ca)
        u_faz.append(u_1)
        u_faz.append(u_2)
        u_faz.append(u_3)
        print(f"Введенные значения фазных напряжений:\n"
              f"Фазное напряжение Uao = {u_1}B\n"
              f"Фазное напряжение Ubo = {u_2}B\n"
              f"Фазное напряжение Uco = {u_3}B\n")
        print(f"Значения линейных напряжений равны:\n"
              f"Линейное напряжение Uab = {round(u_Ab, 3)}B\n"
              f"Линейное напряжение Ubc = {round(u_Bc, 3)}B\n"
              f"Линейное напряжение Uca = {round(u_Ca, 3)}B\n")





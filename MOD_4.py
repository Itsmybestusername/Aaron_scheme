#Модуль вызова функций из модулей 1, 2, 3

from MOD_3 import *

#Вызов набора функций
voltage_calc(u_calc[0], u_calc[1], u_calc[2])
angle_kt(angle_kt_calc[0], angle_kt_calc[1])
print("------------------------------------------------------------\n"
      "             Рассчитанные значения параметров сети          \n"
      "------------------------------------------------------------")
calc_A(u_lin[0], i_fazA, k_cos[0], k_sin[0], angles[0])
calc_B()
calc_C(u_lin[2], i_fazC, k_cos[1], k_sin[1], angles[1])
calc_summ(p_lin[0], p_lin[1], q_lin[0], q_lin[1], s_lin[0], s_lin[1])


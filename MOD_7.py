from MOD_0 import *
from MOD_1 import *
from MOD_6 import *
import numpy as np

print("------------------------------------------------------------\n"
      "     Параметры качества в текущий момент \n"
      "------------------------------------------------------------")
#Согласованные напряжения
if int(u_lin[0]) > 7000:
    u_sogl = 10000
else:
    u_sogl = 6000
u_dif_ab = np.abs(u_sogl - u_lin[0])
u_dif_ca = np.abs(u_sogl - u_lin[1])
u_dif_bc = np.abs(u_sogl - u_lin[2])
print(f"Разница между согласованным и амплитудным значением напряжения:\n"
      f"ф.А: {round(u_dif_ab, 3)} B\n"
      f"ф.В: {round(u_dif_ca, 3)} B\n"
      f"ф.С: {round(u_dif_bc, 3)} B")


#Расчет по методу симметричных составляющих
def u_symmetrical(u_ab, u_bc, u_ca, u_a0, u_b0,  u_c0):
    u_1 = np.sqrt((1/12) * (np.sqrt(3) * u_ab + np.sqrt(4 * u_bc**2 - ((u_bc**2-u_ca**2)/u_ab + u_ab)**2))**2 + ((u_bc**2 - u_ca**2)/u_ab)**2)
    u_2 = np.sqrt((1/12) * (np.sqrt(3) * u_ab - np.sqrt(4 * u_bc**2 - ((u_bc**2-u_ca**2)/u_ab + u_ab)**2))**2 + ((u_bc**2 - u_ca**2)/u_ab)**2)
    u_0 = (1/6) * np.sqrt(((u_bc**2 - u_ca**2)/u_ab - 3*((u_b0**2 - u_a0**2)/u_ab))**2 + (np.sqrt(4 * u_bc**2 - (u_ab + (u_bc**2 - u_ca**2)/u_ab)**2) - 3 * np.sqrt(4 * u_b0**2 - (u_ab + (u_b0**2 - u_a0**2)/u_ab)**2))**2)

    k2u = (u_2/u_1) * 100
    k0u = np.sqrt(3) * (u_0/u_1) * 100

    print(f"Напряжение прямой последовательности:   {u_1} B\n"
          f"Напряжение обратной последовательности: {u_2} B\n"
          f"Напряжение нулевой последовательности:  {u_0} B\n"
          f"Коэффициент несимметрии напряжений обратной последовательности K2U: {k2u}\n"
          f"Коэффициент несимметрии напряжений нулевой последовательности K0U:  {k0u}")

u_symmetrical(u_lin[0], u_lin[2], u_lin[1], u_faz[0], u_faz[2], u_faz[1])

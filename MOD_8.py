#Модуль построения ВД тока+напряжений, мощностей

#Пояснение к построению ВД
#(https://limi.ru/2023/06/29/postroenie-vektornoj-diagrammy-trehfaznoj-jelektricheskoj-cepi-s-pomoshhju-voltamperfazometrov-proizvodstva-cheljenergopribor/)

from MOD_5 import *
from MOD_6 import *
from MOD_7 import *
import matplotlib.pyplot as mpl
import numpy as np


#Создание полотна для диаграммы токов и напряжений
fig, ax = mpl.subplots(figsize=(12, 12))

#Описание векторов фазных напряжений
#Блок закомментирован чтобы не нагромождать пространство полотна векторной диаграммы
#for U, color, label in zip([Ua, Ub, Uc], ['y', 'g', 'r'], ['Ua', 'Ub', 'Uc']):
#    ax.quiver(0, 0, -(U.imag), U.real, angles='xy', scale_units='xy', scale=1,
#              color=color, label=label, width=0.006)

#Описание векторов линейных напряжений
for U, color, label in zip([Uab, Ubc], ['y', 'r'], ['Uab', 'Ubc']):
    ax.quiver(0, 0, -(U.imag), U.real, angles='xy', scale_units='xy', scale=1,
              color=color, label=label, width=0.008)

#Масштабирование векторов тока
if (i_fazA < 1) and (i_fazC < 1):
    ms = 10000 #Масштаб для векторов тока меньше 1
else:
    ms = 1000  #Масштаб для векторов тока больше 1

#Описание векторов фазных токов
for V, color, label in zip([If_a, If_c, If_b], ['y', 'r', 'g'], ['Ia', 'Ic', 'Ib']):
    ax.quiver(0, 0, -(V.imag), V.real, angles='xy', scale_units='xy', scale=(1/ms),
              color=color, label=label, width=0.005)

#Описание осей координат векторной диаграммы, легенды, пояснений, сетки полотна
ax.set_xlim(-12000, 12000)
ax.set_ylim(-12000, 12000)
ax.set_aspect('equal')
ax.grid(True)
ax.legend()
ax.set_title("Векторная диаграмма для схемы Арона")
ax.set_ylabel(f"Величина тока масштабирована {ms}:1")
ax.set_xlabel(f"Значения:\n"
              f"Uab = {round(u_lin[0], 3)}B\n"
              f"Ubc = {round(u_lin[1], 3)}B\n"
              f"Ia = {i_fazA}A, "
              f"Ic = {i_fazC}A, "
              f"Ib = {round((np.abs(If_b)), 3)}A")

mpl.axhline(0, color='k', linewidth=1)
mpl.axvline(0, color='k', linewidth=1)

"""#Создание полотна для диаграммы мощностей ваттметра 1
fig, ax = mpl.subplots(figsize=(9, 9))

#Масштабирование векторов мощности
ms = 5
#Описание векторов мощностей ваттметра 1
for U, color, label in zip([p_ab, q_ab, s_ab], ['r', 'b', 'g'], ['Pab', 'Qab', 'Sab']):
    ax.quiver(0, 0, -(U.imag), U.real, angles='xy', scale_units='xy', scale=1*ms,
              color=color, label=label, width=0.005)

#Описание осей координат векторной диаграммы, легенды, пояснений, сетки полотна
ax.set_xlim(-10000, 10000)
ax.set_ylim(-10000, 10000)
ax.set_aspect('equal')
ax.grid(True)
ax.legend()
ax.set_title("ВД мощностей для сх.Арона - ваттметр 1")
ax.set_ylabel(f"Определение квадранта для вектора полной мощности")
ax.set_xlabel(f"Значения:\n"
              f"Активная мощность:   {np.abs(p_ab)}\n"
              f"Реактивная мощность: {np.abs(q_ab)}\n"
              f"Полная мощность:     {np.abs(s_ab)}")

mpl.axhline(0, color='k', linewidth=1)
mpl.axvline(0, color='k', linewidth=1)


#Создание полотна для диаграммы мощности ваттметра 2
fig, ax = mpl.subplots(figsize=(9, 9))

#Масштабирование векторов мощности
ms = 5
#Описание векторов мощностей ваттметра 1
for U, color, label in zip([p_bc, q_bc, s_bc], ['r', 'b', 'g'], ['Pbc', 'Qbc', 'Sbc']):
    ax.quiver(0, 0, -(U.imag), U.real, angles='xy', scale_units='xy', scale=1*ms,
              color=color, label=label, width=0.005)

#Описание осей координат векторной диаграммы, легенды, пояснений, сетки полотна
ax.set_xlim(-10000, 10000)
ax.set_ylim(-10000, 10000)
ax.set_aspect('equal')
ax.grid(True)
ax.legend()
ax.set_title("ВД мощностей для сх.Арона - ваттметр 2")
ax.set_ylabel(f"Определение квадранта для вектора полной мощности")
ax.set_xlabel(f"Значения:\n"
              f"Активная мощность:   {np.abs(p_bc)}\n"
              f"Реактивная мощность: {np.abs(q_bc)}\n"
              f"Полная мощность:     {np.abs(s_bc)}")

mpl.axhline(0, color='k', linewidth=1)
mpl.axvline(0, color='k', linewidth=1)

#Создание полотна для диаграммы сумарной мощности обоих ваттметров
fig, ax = mpl.subplots(figsize=(9, 9))

#Масштабирование векторов мощности
ms = 10
#Описание векторов мощностей для двух ваттметров
for U, color, label in zip([p_sum, q_sum, s_sum], ['r', 'b', 'g'], ['Pсум', 'Qсум', 'Sсум']):
    ax.quiver(0, 0, -(U.imag), U.real, angles='xy', scale_units='xy', scale=1*ms,
              color=color, label=label, width=0.005)

#Описание осей координат векторной диаграммы, легенды, пояснений, сетки полотна
ax.set_xlim(-10000, 10000)
ax.set_ylim(-10000, 10000)
ax.set_aspect('equal')
ax.grid(True)
ax.legend()
ax.set_title("ВД мощностей двух ваттметров")
ax.set_ylabel(f"Определение квадранта для вектора полной мощности")
ax.set_xlabel(f"Значения:\n"
              f"Активная мощность:{round(np.abs(p_sum), 1)} Вт, "
              f"Реактивная мощность:{round(np.abs(q_sum), 1)} ВАр, "
              f"Полная мощность:{round(np.abs(s_sum), 1)} ВА")

mpl.axhline(0, color='k', linewidth=1)
mpl.axvline(0, color='k', linewidth=1)
"""

#Вывод
mpl.show()


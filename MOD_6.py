#Модуль представления мощностей в комплексном виде

from MOD_5 import *
import numpy as np

print("------------------------------------------------------------\n"
      "     Представления комплексных величин мощностей \n"
      "------------------------------------------------------------")
#Мощности ваттметра 1 (ведущий модуль)
p_ab = p_lin[0] * np.exp(1j * np.deg2rad(0))
q_ab = q_lin[0] * np.exp(1j * np.deg2rad(270))
s_ab = s_lin[0] * np.exp(1j * np.deg2rad(-angles[0]))
print(f"Комплексное представление мощностей ваттметра 1 (ведущий):\n"
      f"Активная мощность:          {p_ab}\n"
      f"Модуль активной мощности:   {round(np.abs(p_ab), 3)}\n"
      f"Реактивная мощность:        {q_ab}\n"
      f"Модуль реактивной мощности: {round(np.abs(q_ab), 3)}\n"
      f"Полная мощность:            {s_ab}\n"
      f"Модуль полной мощности:     {round(np.abs(s_ab), 3)}")

print(" ")
#Мощности ваттметра 2 (ведущий модуль)
p_bc = p_lin[1] * np.exp(1j * np.deg2rad(0))
q_bc = q_lin[1] * np.exp(1j * np.deg2rad(270))
s_bc = s_lin[1] * np.exp(1j * np.deg2rad(-angles[1]))
print(f"Комплексное представление мощностей ваттметра 2 (ведомый):\n"
      f"Активная мощность:          {p_bc}\n"
      f"Модуль активной мощности:   {round(np.abs(p_bc), 3)}\n"
      f"Реактивная мощность:        {q_bc}\n"
      f"Модуль реактивной мощности: {round(np.abs(q_bc), 3)}\n"
      f"Полная мощность:            {s_bc}\n"
      f"Модуль полной мощности:     {round(np.abs(s_bc), 3)}")

print(" ")
#результирующие значения мощностей для обоих ваттметров
p_sum = p_summ[0] * np.exp(1j * np.deg2rad(0))
q_sum = q_summ[0] * np.exp(1j * np.deg2rad(270))
s_sum = s_summ[0] * np.exp(1j * np.deg2rad(-ang_summ[0]))
print(f"Комплексное представление мощностей обоих ваттметров:\n"
      f"Активная мощность:          {p_sum}\n"
      f"Модуль активной мощности:   {round(np.abs(p_sum), 3)}\n"
      f"Реактивная мощность:        {q_sum}\n"
      f"Модуль реактивной мощности: {round(np.abs(q_sum), 3)}\n"
      f"Полная мощность:            {s_sum}\n"
      f"Модуль полной мощности:     {round(np.abs(s_sum), 3)}")

"""if np.real(s_sum) > 0 and np.imag(s_sum) > 0:
      print("Квадрант I - инд.")
elif np.real(s_sum) < 0 < np.imag(s_sum):
      print ("Квадрант II - емк.")
elif np.real(s_sum) < 0 and np.imag(s_sum) < 0:
      print("Квадрант III - инд.")
elif np.real(s_sum) > 0 > np.imag(s_sum):
      print("Квадрант IV - емк.")"""

#Модуль с функцией расчета мощностей и тангенсов пофазно и суммарно


from MOD_1 import *
from MOD_2 import *

p_lin = [] #Пустой список для активных мощностей
q_lin = [] #Пустой список для реактивных мощностей
s_lin = [] #Пустой список для полных мощностей
p_summ = [] #Пустой список для значения суммарной активной мощности
q_summ = [] #Пустой список для значения суммарной реактивной мощности
s_summ = [] #Пустой список для значения суммарной полной мощности
ang_summ = [] #Пустой список для значений угла в суммарном результате

#Расчет активной, реактивной, полной мощностей и тангенса в ф.А(АВ)
def calc_A(ulin_a, ifaz_a, cos_A, sin_fA, ang_a):
    if cos_A == 0:
        cos_A = 0.000000000001
    P_actA = float(ulin_a * ifaz_a * cos_A)
    Q_reactA = float(ulin_a * ifaz_a * sin_fA)
    tang_fiA = float(Q_reactA / P_actA)
    tang_fiA_calc = sin_fA / cos_A
    S_full_A = float(m.sqrt(P_actA**2 + Q_reactA**2))

    #Заполнение пустого списка
    p_lin.append(P_actA)
    q_lin.append(Q_reactA)
    s_lin.append(S_full_A)

    #Вывод параметров ф.А
    print(f"Параметры фазы А:\n"
        f"Ток:                                {ifaz_a} (A)\n"
        f"Фазное напряжение:                  {round(u_faz[0], 3)} (В)\n"
        f"Полная мощность:                    {round(S_full_A, 3)} (BA)\n"
        f"Активная мощность:                  {round(P_actA, 3)} (Вт)\n"
        f"Реактивная мощность:                {round(Q_reactA, 3)} (вар)\n"
        f"Коэффициент мощности:               {round((cos_A), 3)}\n"
        f"Тангенс Fi (расчитан Q/P):          {round(tang_fiA, 3)}\n"
        #f"Тангенс Fi (рассчитан sin/cos):     {round(tang_fiA_calc, 3)}\n"
        f"Угол между векторами Uab^Ia:        {round((ang_a), 3)}°\n"
        f"Синус Fi:                           {round((sin_fA), 3)}\n")

#Расчет активной, реактивной, полной мощностей и тангенса в ф.В(ВС)
def calc_B():
    print(f"Параметры фазы B:\n"
        f"Фазное напряжение:                  {round(u_faz[1], 3)} (В)\n")

# Расчет активной, реактивной, полной мощностей и тангенса в ф.C(CA)
def calc_C(ulin_c, ifaz_c, cos_C, sin_fC, ang_c):
    if cos_C == 0:
        cos_C = 0.00000000001
    P_actC = float(ulin_c * ifaz_c * cos_C)
    Q_reactC = float(ulin_c * ifaz_c * sin_fC)
    tang_fiC = float(Q_reactC / P_actC)
    tang_fiC_calc = float(sin_fC / cos_C)
    S_full_C = float(m.sqrt(P_actC**2 + Q_reactC**2))

    #Заполнение пустого списка
    p_lin.append(P_actC)
    q_lin.append(Q_reactC)
    s_lin.append(S_full_C)

    #Вывод параметров ф.С
    print(f"Параметры фазы C:\n"
        f"Ток:                                {ifaz_c} (A)\n"
        f"Фазное напряжение:                  {round(u_faz[2], 3)} (В)\n"
        f"Полная мощность:                    {round(S_full_C, 3)} (BA)\n"
        f"Активная мощность:                  {round(P_actC, 3)} (Вт)\n"
        f"Реактивная мощность:                {round(Q_reactC, 3)} (вар)\n"
        f"Коэффициент мощности:               {round(cos_C, 3)}\n"
        f"Тангенс Fi (рассчитан Q/P):         {round(tang_fiC, 3)}\n"
        #f"Тангенс Fi (рассчитан sin/cos):     {round(tang_fiC_calc, 3)}\n"
        f"Угол между векторами Ubc^Ic:        {round((ang_c), 3)}°\n"
        f"Синус Fi:                           {round((sin_fC), 3)}\n")

# Расчет активной, реактивной, полной мощностей и тангенса суммарно
def calc_summ(P_actA, P_actC, Q_reactA, Q_reactC, S_full_A, S_full_C):
    P_actSum = P_actA + P_actC
    Q_reactSum = Q_reactA + Q_reactC
    S_full_sqr = m.sqrt(P_actSum ** 2 + Q_reactSum ** 2)
    S_full_summ = S_full_A + S_full_C
    if P_actSum == 0:
        P_actSum = 0.00000001
    tg_fiSumm = Q_reactSum / P_actSum
    coef_fiSum_sqr = P_actSum / S_full_sqr
    angle_sum = np.rad2deg(np.acos(coef_fiSum_sqr))
    #coef_fiSum_sum = P_actSum / S_full_summ

    #Заполнение пустого списка
    p_summ.append(P_actSum)
    q_summ.append(Q_reactSum)
    s_summ.append(S_full_sqr)
    ang_summ.append(angle_sum)

    print(f"Параметры для суммы фаз:\n"
      f"Активная мощность:                   {round(P_actSum, 3)} (Вт)\n"
      f"Реактивная мощность:                 {round(Q_reactSum, 3)} (вар)\n"
      f"Полная мощность (квадратичная):      {round(S_full_sqr, 3)} (ВА)\n"
      #f"Полная мощность (суммарная):         {round(S_full_summ, 3)} (BA)\n"
      f"Коэффициент мощности (квадратичный): {round(coef_fiSum_sqr, 3)}\n"
      #f"Коэффициент мощности (суммарный):    {round(coef_fiSum_sum, 3)}\n"
      f"Тангенс Fi:                          {round(tg_fiSumm, 3)}\n")
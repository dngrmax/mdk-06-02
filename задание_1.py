"""Вариант 1, задание 1: одноканальная СМО с отказами M/M/1:0."""

import math
import matplotlib.pyplot as plt


def read_positive(prompt):
    value = float(input(prompt).replace(",", "."))
    if not math.isfinite(value) or value <= 0:
        raise ValueError("Интенсивность должна быть положительной")
    return value


def main():
    lam = read_positive("Интенсивность поступления заявок λ: ")
    mu = read_positive("Интенсивность обслуживания μ: ", end="\n\n")

    rho = lam / mu  # нагрузка на систему
    p0 = 1 / (1 + rho)  # канал свободен
    p1 = rho / (1 + rho)  # канал занят
    p_refusal = p1  # новая заявка получит отказ, если канал занят
    q = 1 - p_refusal  # доля обслуженных заявок
    a = lam * q  # число обслуженных заявок за единицу времени

    print("Одноканальная СМО с отказами M/M/1:0")
    print(f"Нагрузка ρ: {rho:.4f}", end="\n\n")

    print("Состояние            Вероятность")
    print(f"S0: канал свободен    {p0:.4f}")
    print(f"S1: канал занят       {p1:.4f}", end="\n\n")
    
    print(f"Вероятность отказа Pотк: {p_refusal:.4f}")
    print(f"Относительная пропускная способность Q: {q:.4f}")
    print(f"Абсолютная пропускная способность A: {a:.4f} заявок/ед. времени")

    # График matplotlib
    plt.bar(["S0: свободен", "S1: занят"], [p0, p1], color=["#73a9d8", "#e5a15a"])
    plt.ylim(0, 1)
    plt.ylabel("Вероятность")
    plt.title("Одноканальная СМО: вероятности состояний")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    try:
        main()
    except ValueError as error:
        print(f"Ошибка ввода: {error}")




        Изменение в файле задание 1.!!!!!...!!...!!!!!!!
        
        укш
        уьулту

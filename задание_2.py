"""Вариант 1, задание 2: многоканальная СМО с отказами M/M/n:0."""

import math

import matplotlib.pyplot as plt


def read_positive(prompt):
    value = float(input(prompt).replace(",", "."))
    if not math.isfinite(value) or value <= 0:
        raise ValueError("Интенсивность должна быть положительной")
    return value


def main():
    lam = read_positive("Интенсивность поступления заявок λ: ")
    mu = read_positive("Интенсивность обслуживания одним каналом μ: ")
    n = int(input("Число каналов n: "))
    if n < 2:
        raise ValueError("Для многоканальной СМО нужно не менее двух каналов")

    rho = lam / mu  # нагрузка на систему

    terms = []

    for k in range(n + 1):
        terms.append(rho**k / math.factorial(k))

    p0 = 1 / sum(terms)  # вероятность свободной системы
    probabilities = [term * p0 for term in terms]  # вероятности состояний S0...Sn
    p_refusal = probabilities[n]  # отказ, когда заняты все каналы
    q = 1 - p_refusal  # относительная пропускная способность
    a = lam * q  # абсолютная пропускная способность
    busy = a / mu  # среднее число занятых каналов
    load = busy / n  # коэффициент загрузки одного канала
    idle = 1 - load  # коэффициент простоя одного канала
    in_system = busy  # очереди нет, поэтому все заявки в системе обслуживаются
    time_in_system = in_system / lam  # время по формуле

    print(f"\nМногоканальная СМО с отказами M/M/{n}:0")
    print(f"Нагрузка ρ: {rho:.4f}")
    print("\nСостояние  Вероятность")
    for k, probability in enumerate(probabilities):
        print(f"S{k:<9}  {probability:.4f}")

    print(f"\nВероятность отказа Pотк: {p_refusal:.4f}")
    print(f"Коэффициент простоя канала Kп: {idle:.4f}")
    print(f"Коэффициент загрузки канала Kз: {load:.4f}")
    print(f"Относительная пропускная способность Q: {q:.4f}")
    print(f"Абсолютная пропускная способность A: {a:.4f} заявок/ед. времени")
    print(f"Среднее число заявок в СМО Nсмо: {in_system:.4f}")
    print("Средняя длина очереди Nоч: 0 (очереди нет)")
    print(f"Среднее число занятых каналов nз: {busy:.4f}")
    print(f"Среднее время заявки в СМО Tсмо: {time_in_system:.4f} ед. времени")
    print("Среднее время заявки в очереди Tоч: 0 (очереди нет)")

    plt.bar([f"S{k}" for k in range(n + 1)], probabilities, color="#73a9d8")
    plt.ylim(0, 1)
    plt.xlabel("Число занятых каналов")
    plt.ylabel("Вероятность")
    plt.title("Многоканальная СМО: вероятности состояний")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    try:
        main()
    except ValueError as error:
        print(f"Ошибка ввода: {error}")

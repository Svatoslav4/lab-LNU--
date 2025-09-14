import numpy as np
import random
import math

def generate_signal(signal_type: int, start: float, end: float, step: float):
    """
    Генерує сигнал заданого типу:
    1 - синус
    2 - косинус
    3 - випадковий шум
    Повертає словник з 'x' та 'y'
    """
    X = np.arange(start, end, step)

    if signal_type == 1:
        Y = np.sin(X)
    elif signal_type == 2:
        Y = np.cos(X)
    elif signal_type == 3:
        Y = np.array([random.random() for _ in X])
    else:
        raise ValueError("Невідомий тип сигналу")

    return {"x": X, "y": Y}


def correlation(sig_a: dict, sig_b: dict) -> float:
    """Обчислює кореляцію між двома сигналами по y"""
    return np.corrcoef(sig_a['y'], sig_b['y'])[0, 1]


def autocorrelation(sig: dict) -> np.ndarray:
    """Обчислює автокореляцію сигналу"""
    y = sig['y'] - np.mean(sig['y'])
    result = np.correlate(y, y, mode='full')
    return result[result.size // 2:] / np.max(result)


# ------------------ Приклади ------------------
signal1 = generate_signal(1, 0, 2, 0.1)
signal2 = generate_signal(2, 0, 2, 0.1)
signal3 = generate_signal(3, 0, 2, 0.1)

print("Кореляція сигнал1 і сигнал3:", correlation(signal1, signal3))
print("Кореляція сигнал2 і сигнал1:", correlation(signal2, signal1))
print("Автокореляція сигнал2:", autocorrelation(signal2))

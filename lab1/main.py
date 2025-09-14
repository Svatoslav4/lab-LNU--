import math
import numpy as np
import matplotlib.pyplot as plt


def round4(x: float) -> float:
    """Округлення до 4-х знаків"""
    return math.floor(x * 10000) / 10000.0


def dirak(x: float) -> float:
    """Функція Дірака"""
    return 1 if round4(x) == 0 else 0


def rectangular(x: float) -> float:
    """Прямокутна функція"""
    return 1 if -0.5 <= x <= 0.5 else 0


def sinc_func(x: float) -> float:
    """sin(x)/x"""
    return 1 if x == 0 else math.sin(x) / x


def generate_signal(func_type: int, step: float, length: float):
    """Генерує X та Y для обраної функції"""
    X = np.arange(-length / 2, length / 2, step)
    if func_type == 1:
        Y = [dirak(x) for x in X]
    elif func_type == 2:
        Y = [rectangular(x) for x in X]
    elif func_type == 3:
        Y = [sinc_func(x) for x in X]
    else:
        Y = X  # просто лінійна функція
    return X, np.array(Y)


def plot_signal_and_spectrum(X, Y, title="Сигнал"):
    """Малює сигнал та його Фур'є-образ"""
    plt.figure(figsize=(12, 5))

    # сигнал
    plt.subplot(1, 2, 1)
    plt.plot(X, Y, label="f(x)")
    plt.title(title)
    plt.grid(True)
    plt.legend()

    # спектр
    spectrum = np.abs(np.fft.fft(Y))
    freqs = np.fft.fftfreq(len(Y), X[1] - X[0])

    plt.subplot(1, 2, 2)
    plt.plot(freqs[:len(freqs)//2], spectrum[:len(spectrum)//2], label="|F(ω)|")
    plt.title("Амплітудний спектр")
    plt.grid(True)
    plt.legend()

    plt.tight_layout()
    plt.show()


# ---------------- Основна програма ----------------
if __name__ == "__main__":
    step = 0.05
    length = 10

    # Приклад: прямокутна функція
    X1, Y1 = generate_signal(2, step, length)
    plot_signal_and_spectrum(X1, Y1, title="Прямокутна функція")

    # Приклад: функція Дірака
    X2, Y2 = generate_signal(1, step, length)
    plot_signal_and_spectrum(X2, Y2, title="Функція Дірака")

    # Приклад: sinc
    X3, Y3 = generate_signal(3, step, length)
    plot_signal_and_spectrum(X3, Y3, title="sinc(x)")

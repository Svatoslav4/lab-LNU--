import numpy as np
import matplotlib.pyplot as plt


def dirak(x: float) -> float:
    """Функція Дірака: пік у нулі"""
    return 1 if abs(x) < 1e-6 else 0


def rectangular(x: float) -> float:
    """Прямокутна функція ширини 1"""
    return 1 if -0.5 <= x <= 0.5 else 0


def sinc_func(x: float) -> float:
    """sinc(x) = sin(x)/x"""
    return 1.0 if x == 0 else np.sin(x) / x


def generate_signal(func_type: int, step: float, length: float):
    """Генерує масиви X та Y для вибраної функції"""
    X = np.arange(-length / 2, length / 2 + step, step)
    if func_type == 1:
        Y = np.array([dirak(x) for x in X])
    elif func_type == 2:
        Y = np.array([rectangular(x) for x in X])
    elif func_type == 3:
        Y = np.array([sinc_func(x) for x in X])
    else:
        Y = X  # лінійна функція
    return X, Y


def plot_signal_and_spectrum(X, Y, title="Сигнал"):
    """Малює сигнал та його амплітудний спектр"""
    plt.figure(figsize=(12, 5))

    # сигнал
    plt.subplot(1, 2, 1)
    plt.plot(X, Y, label="f(x)")
    plt.title(title)
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(True)
    plt.legend()

    # спектр
    spectrum = np.abs(np.fft.fft(Y)) / len(Y)
    freqs = np.fft.fftfreq(len(Y), X[1] - X[0])

    plt.subplot(1, 2, 2)
    plt.plot(freqs[:len(freqs)//2], spectrum[:len(spectrum)//2], label="|F(ω)|")
    plt.title("Амплітудний спектр")
    plt.xlabel("Частота ω")
    plt.ylabel("|F(ω)|")
    plt.grid(True)
    plt.legend()

    plt.tight_layout()
    plt.show()


# ---------------- Основна програма ----------------
if __name__ == "__main__":
    step = 0.01
    length = 10

    # Прямокутна функція
    X1, Y1 = generate_signal(2, step, length)
    plot_signal_and_spectrum(X1, Y1, title="Прямокутна функція")

    # Функція Дірака
    X2, Y2 = generate_signal(1, step, length)
    plot_signal_and_spectrum(X2, Y2, title="Функція Дірака")

    # sinc(x)
    X3, Y3 = generate_signal(3, step, length)
    plot_signal_and_spectrum(X3, Y3, title="sinc(x)")

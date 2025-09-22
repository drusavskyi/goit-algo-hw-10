# main-2.py
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

def f(x):
    return x ** 2

def monte_carlo_integral(func, a: float, b: float, n: int = 100000) -> float:
    """
    Обчислення визначеного інтеграла методом Монте-Карло.
    """
    x = np.random.uniform(a, b, n)
    y = func(x)
    return (b - a) * np.mean(y)

if __name__ == "__main__":
    a, b = 0, 2
    n = 100000

    mc_result = monte_carlo_integral(f, a, b, n)
    print(f"Monte Carlo (n={n}): {mc_result:.6f}")

    quad_result, error = quad(f, a, b)
    print(f"SciPy quad: {quad_result:.6f}, похибка: {error:.2e}")

    # Побудова графіка
    x = np.linspace(-0.5, 2.5, 400)
    y = f(x)
    fig, ax = plt.subplots()
    ax.plot(x, y, 'r', linewidth=2)
    ix = np.linspace(a, b)
    iy = f(ix)
    ax.fill_between(ix, iy, color='gray', alpha=0.3)
    ax.axvline(x=a, color='gray', linestyle='--')
    ax.axvline(x=b, color='gray', linestyle='--')
    ax.set_title(f"Інтеграл f(x)=x^2 від {a} до {b}")
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    plt.grid()
    plt.show()

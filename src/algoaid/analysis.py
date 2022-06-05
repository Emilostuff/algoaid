import numpy as np
from scipy.optimize import curve_fit
import time
import matplotlib.pyplot as plt


def __runtime(f, n):
    start = time.perf_counter()
    f(n)
    end = time.perf_counter()
    return end-start


def analyse(f, nmin=5, nmax=100000, steps=100):
    """Takes in a function of n, analyses its asymptotic time complexity"""
    xdata = np.linspace(nmin, nmax, steps, dtype=int)
    ydata = np.empty((0, 3), float,)
    plt.figure("Results")

    # generate data
    print(f"Running {steps} tests from n = {nmin} to n = {nmax}")
    print("0 %" + " " * 92 + "100 %")
    pc = 0
    for n in xdata:
        pc += 100/steps
        print("=" * round(pc), end="\r")
        ydata = np.append(ydata, __runtime(f, n))
    print("\n")
    plt.plot(xdata, ydata, 'silver', label='data', linewidth=5)

    # O(1)
    def con(n, a): return a + 0 * n
    popt, pcov = curve_fit(con, xdata, ydata)
    plt.plot(xdata, con(xdata, *popt), 'paleturquoise', label=r'$O(1)$')
    # O(log n)
    def log(n, a): return a*np.log(n)
    popt, pcov = curve_fit(log, xdata, ydata)
    plt.plot(xdata, log(xdata, *popt), 'c-', label=r'$O(\log n)$')
    # O(n)
    def lin(n, a): return a*n
    popt, pcov = curve_fit(lin, xdata, ydata)
    plt.plot(xdata, lin(xdata, *popt), 'r-', label=r'$O(n)$')
    # O(sqrt(n))
    def sq(n, a): return a*np.sqrt(n)
    popt, pcov = curve_fit(sq, xdata, ydata)
    plt.plot(xdata, sq(xdata, *popt), 'orange', label=r'$O(\sqrt{n})$')
    # O(n log n)
    def nlog(n, a): return a*np.log(n)*n
    popt, pcov = curve_fit(nlog, xdata, ydata)
    plt.plot(xdata, nlog(xdata, *popt), 'g-', label=r'O($n \log n$)')
    # O(n^2)
    def n2(n, a): return a*n*n
    popt, pcov = curve_fit(n2, xdata, ydata)
    plt.plot(xdata, n2(xdata, *popt), 'm-', label=r'O($n^2$)')
    # O(n^3)
    def n3(n, a): return a*n*n*n
    popt, pcov = curve_fit(n3, xdata, ydata)
    plt.plot(xdata, n3(xdata, *popt), 'lime', label=r'O($n^3$)')

    # finalize
    plt.xlabel('n')
    plt.ylabel('time')
    plt.legend()
    plt.show()

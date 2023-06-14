def midpointintegration(f, a, b, n):
    sum = 0
    h = (b-a)/n
    for i in range (n-1):
        x = (a + 0.5 * h + i * h)
        sum += h * f(x)
    return sum


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    print(midpointintegration(lambda x: x**2, 1, 500, 2))
    plt.plot([midpointintegration(lambda x: x**2, 1, 500, i) for i in range(1, 200)])
    plt.xlabel("n")
    plt.ylabel("Mid point itegration value")



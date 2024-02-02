import numpy as np
def circular_convolution(x, h):
    l = len(x)
    m = len(h)
    n = max(l, m)
    y = np.zeros(n)
    for i in range(n):
        for j in range(m):
            y[i] += x[(i-j)%l] * h[j]
    return y

if __name__ == "__main__":
    x = list(map(float, input("Enter the input sequence x(n): ").split()))
    h = list(map(float, input("Enter the impulse response h(n): ").split()))
    y = circular_convolution(x, h)
    print("The circular convolution of x(n) and h(n) is: ", y)
    print("The length of the circular convolution is: ", len(y))
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

def linear_convolution(x, h):
    l = len(x)
    m = len(h)
    n = l + m - 1
    x = np.append(x, np.zeros(n - l))
    h = np.append(h, np.zeros(n - m))
    y = circular_convolution(x, h)
    return y[:n]

if __name__ == "__main__":
    x = list(map(float, input("Enter the input sequence x(n): ").split()))
    h = list(map(float, input("Enter the impulse response h(n): ").split()))
    y = linear_convolution(x, h)
    print("The linear convolution of x(n) and h(n) is: ", y)
    print("The length of the linear convolution is: ", len(y))
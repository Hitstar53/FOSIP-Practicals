import numpy as np
def linear_convolution(x, h):
    l = len(x)
    m = len(h)
    n = l + m - 1
    y = np.zeros(n)
    for i in range(l):
        for j in range(m):
            y[i+j] += x[i] * h[j]
    return y

if __name__ == '__main__':
    x = list(map(float, input('Enter the input sequence x(n): ').split()))
    h = list(map(float, input('Enter the impulse response h(n): ').split()))
    y = linear_convolution(x, h)
    print('\nThe linear convolution of x(n) and h(n) is:', y)
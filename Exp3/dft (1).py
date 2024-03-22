import numpy as np
import matplotlib.pyplot as plt

# Function to perform Discrete Fourier Transform (DFT) of N point signal
def DFT(signal):
    N = len(signal)
    n = np.arange(N)
    k = n.reshape((N, 1))
    e = np.exp(-2j * np.pi * k * n / N)
    X = np.dot(e, signal)
    return X

# Function to plot magnitude spectrum
def plot_magnitude_spectrum(X, title):
    plt.stem(np.abs(X), use_line_collection=True)
    plt.title(title)
    plt.xlabel('Frequency (k)')
    plt.ylabel('Magnitude')
    plt.grid(True)
    plt.show()

# Main function
def main():
    # Input specifications
    N = int(input("Enter the length of the signal (N): "))
    signal_values = np.zeros(N)
    print("Enter the DT signal values:")
    for i in range(N):
        signal_values[i] = float(input(f"Enter value {i+1}: "))

    # Calculate DFT of the original signal
    X_original = DFT(signal_values)

    # Plot magnitude spectrum of the original signal
    plot_magnitude_spectrum(X_original, "Magnitude Spectrum of Original Signal")

    # Append the input signal by four zeros
    signal_zeros_appended = np.append(signal_values, np.zeros(4))
    X_zeros_appended = DFT(signal_zeros_appended)

    # Plot magnitude spectrum after zero padding
    plot_magnitude_spectrum(X_zeros_appended, "Magnitude Spectrum after Zero Padding")

    # Expand the input signal by inserting alternate zeros
    signal_expanded_zeros = np.zeros(2 * N)
    signal_expanded_zeros[::2] = signal_values
    X_expanded_zeros = DFT(signal_expanded_zeros)

    # Plot magnitude spectrum after expanding with alternate zeros
    plot_magnitude_spectrum(X_expanded_zeros, "Magnitude Spectrum after Expanding with Alternate Zeros")

if __name__ == "__main__":
    main()

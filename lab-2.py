# If a signal to interference ratio of 15 dB is required for satisfactory forward channel 
# performance of a cellular system, what is the frequency reuse factor and cluster size that 
# should be used for maximum capacity if the path loss exponent is (a) n= 4 , (b) n = 3? 
# Assume that there are 6 co-channels cells in the first tier and all of them are at the same 
# distance from the mobile. Use suitable approximations. 

import math


def calculate_frequency_reuse_factor(N):
    Q = math.sqrt(3 * N)
    return Q


def calculate_SIR(Co, n, Q):
    # Signal to interference ration
    SI = 10 * math.log10((1 / Co) * Q**n)
    return SI


def find_optimal_parameters(R_SI, Co, N):
    for n in [4, 3]:
        Q = calculate_frequency_reuse_factor(N)
        SI = calculate_SIR(Co, n, Q)
        print(f"For n = {n} : ")
        print(f"Frequency reuse factor (Q) :{Q}")
        print(f"Signal to interference ration (SI) :{SI} dB")

        if SI < R_SI:
            # Adjusting parameters
            i = 2
            j = 2
            N = i**2 + i * j + j**2
            Q = calculate_frequency_reuse_factor(N)
            SI = calculate_SIR(Co, n, Q)
            print("Adjusting parameters:")
            print(f"New Frequency reuse factor (Q): {Q}")
            print(f"New Signal to interference ratio (SI): {SI} dB")


# Given the parameter
R_SI = 15  # Required signal to interference ratio (dB)
Co = 6  # Path loss exponent
find_optimal_parameters(R_SI, Co, 7)

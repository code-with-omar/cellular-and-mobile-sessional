#Determine the path loss of a 900MHz cellular system in a large city from a base station with the height of 100m and mobile station installed in a vehicle with antenna height of 2m. The distance between mobile and base station is 4Km.
import math

# Given values
hre = 2  # Height of the receiving antenna (meters)
hte = 100  # Height of the transmitting antenna (meters)
fc = 900  # Frequency (MHz)
d = 4  # Distance between antennas (kilometers)

# Calculate a_hre
a_hre = 3.2 * (math.log10(11.75 * hre)) ** 2 - 4.97

# Calculate path loss
Lp = 69.55 + 26.16 * math.log10(fc) - 13.82 * math.log10(hte) - a_hre + (44.9 - 6.55 * math.log10(hte)) * math.log10(d)

print('Path loss: %.2f' % Lp)

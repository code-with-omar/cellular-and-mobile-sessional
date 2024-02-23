# Determine the path loss between base station (BS) and mobile station (MS) of a 1.8GHz
# PCS system operating in a high-rise urban area. The MS is located in a perpendicular
# street to the location of the BS. The distances of the BS and MS to the corner of the street
# are 20 and 30 meters, respectively. The base station height is 20m.
import math

# Given values
fc = 1.8  # Frequency (GHz)
hb = 20  # Height of the base station antenna (meters)
d = (
    math.sqrt(20**2 + 30**2) / 1000
)  # Distance between the base station and mobile station (kilometers)

print("Distance: %.4f Km" % d)

# Calculate path loss
PathLoss = (
    135.41
    + (12.49 * math.log10(fc))
    - (4.99 * math.log10(hb))
    + ((46.82 - 2.34 * math.log10(hb)) * math.log10(d))
)

print("PathLoss: %.4f dB" % PathLoss)

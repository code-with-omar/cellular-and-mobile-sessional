# If a transmitter produces 50 watts of power, express the transmit power in units of
# (a) dBm, and (b) dBW. If 50 watts is applied to a unity gain antenna with a 900 MHz carrier
# frequency, find the received power in dBm at a free space distance of 100 m from the
# antenna, what is P (10 km)? Assume unity gain for the receiver antenna.
import math

Pt = 50  # Transmitter Power
fc = 900  # Carrier Frequency
# (a) dBm transmitting power
PtdBm = 10 * math.log10(Pt * 1e3)
print("Transmitted Power: %.1f dBm" % PtdBm)

# (b)
PtBW = 10 * math.log10(Pt)
print("Transmitted Power: %.1f dBW" % PtBW)

# Received power
Gt = 1
Gr = 1
lam = 1 / 3
d = 100
L = 1
Pr = (Pt * Gt * Gr * (lam**2)) / (((4 * math.pi) ** 2) * (d**2) * L)
PrdBm = 10 * math.log10(Pr * 1e3)
print("Received Power: %.1f dBm" % PrdBm)


# Pr(10Km)
Pr10Km = PrdBm + 20 * math.log10(100 / 10000)
print("Received Power: %.1f dBm" % Pr10Km)

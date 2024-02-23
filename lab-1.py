band_width = 33e3
single_channel_bandwidth = 25
# duplex channel bandwidth
duplex_channel = 2 * single_channel_bandwidth
print("Channel Bandwidth : ", duplex_channel)

# Total Channel
total_channel = band_width // duplex_channel
print("Total available channels : ", total_channel)

# control channel bandwidth
control_channel_band_width = 1000

# total control channel
total_control_channel = control_channel_band_width // duplex_channel
print("Total control channels = ", total_control_channel)

print("======================================")
print("For various cluster size")
print("======================================")
N = [4, 7, 12]
for cluster_size in N:
    # cluster size
    print("cluster size :", cluster_size)

    # channel per cells
    channel_per_cell = total_channel // cluster_size
    print("Channel per cell = ", channel_per_cell)

    # control channel per cells
    control_channel = total_control_channel // cluster_size
    print("Control channel =", control_channel)

    # voice channel per cell
    voice_channl_per_cell = (total_channel - total_control_channel) // cluster_size

    print("Voice channel =", voice_channl_per_cell)
    print("=========================================")

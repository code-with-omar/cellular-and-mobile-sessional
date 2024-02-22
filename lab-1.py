# Given total bandwidth
bw = 33e3
single_channel_bw = 25

# Duplex channel bandwidth
duplex_channel_bw = 2 * single_channel_bw
print("Channel bw= ", duplex_channel_bw)

# Total available channel
total_channel = bw // duplex_channel_bw
print("Total available channel: ", total_channel)

# given control channel bandwidth
control_Channel_bw = 1000

# total control channel
total_control_channel = control_Channel_bw // duplex_channel_bw
print("Total Control channel :", total_control_channel)

# Array of different value for N(number of cells)
print("------------------------------------------------")
print("For various cluster size")
print("------------------------------------------------")

N = [4, 7, 12]
for cluster_size in N:
    # cluster size
    print("Cluster Size = ", cluster_size)

    # channel per cells
    channel_per_cell = total_channel // cluster_size
    print("Channel per cell = ", channel_per_cell)

    # Control channels per cell
    control_channel_per_cell = total_control_channel // cluster_size
    print("Control channels per cell", control_channel_per_cell)
    voice_channel = (total_channel - total_control_channel) // cluster_size
    print("Voice channel =", voice_channel)
    print("-----------------------------------------")

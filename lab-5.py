# A certain city has an area of 1,300 square miles and is covered by a cellular system using 
# a 7-cell reuse pattern. Each cell has a radius of 4 miles and the city is allocated 40 MHz 
# of spectrum with a full duplex channel bandwidth of 60 kHz. Assume a GOS of 2% for 
# an Erlang B system is specified. If the offered traffic per user is 0.03 Erlangs, compute 
# (a) the number of cells in the service area, (b) the number of channels per cell, (c) traffic 
# intensity of each cell, (d) the maximum carried traffic; (e) the total number of users that 
# can be served for 2% GOS, (f') the number of mobiles per channel, and (g) the theoretical 
# maximum number of users that could be served at one time by the system. 
import math

# Given values
area = 1300
radius = 4
# The area of a cell (hexagon) can shown to be 2.5981R^2

each_cell_covers = math.floor(2.5981 * radius**2)  # in square kilometers
# (A) Number of cells in the service area
print("(a)")
number_of_cells = math.floor(area / each_cell_covers)
print("Number of cells:", number_of_cells)
# (B) the number of channels per cell,

allocated_spectrum = 40000
channel_width = 60
frequency_reuse_factor = 7
print("(b)")
number_of_channel_per_cell = math.floor(
    allocated_spectrum / (channel_width * frequency_reuse_factor)
)
print("Number of channels per cell:", number_of_channel_per_cell)


# (C)traffic intensity of each cell,
print("(c)")
traffic_intensity_per_cell = 84  # from erlang chart B
print("Traffic intensity per cell:", traffic_intensity_per_cell)
# (D) the maximum carried traffic;
print("(d)")
maximum_carried_traffic = number_of_cells * traffic_intensity_per_cell
print("Maximum carried traffic:", maximum_carried_traffic)

# (E) the total number of users that can be served for 2% GOS
traffic_per_user = 0.03
print("(e)")
total_number_of_user = maximum_carried_traffic / traffic_per_user
print("Total number of users:", total_number_of_user)

# (F)  the number of mobiles per channel
number_of_channels = number_of_channel_per_cell * frequency_reuse_factor
print("(f)")
number_of_mobile_per_channel = math.floor(total_number_of_user / number_of_channels)
print("Number of mobiles per channel:", number_of_mobile_per_channel)
print("(g)")
theoretical_maximum_number_of_user_that_could_be_served = (
    number_of_cells * number_of_channel_per_cell
)
print(
    "Theoretical maximum number of users that could be served:",
    theoretical_maximum_number_of_user_that_could_be_served,
)

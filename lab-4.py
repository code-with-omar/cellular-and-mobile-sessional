# An urban area has a population of 2 million residents. Three competing trunked mobile 
# networks (systems A, B, and C) provide cellular service in this area. System A has 394 
# cells with 19 channels each, system B has 98 cells with 57 channels each, and system C 
# has 49 cells, each with 100 channels. Find the number of users that can be supported at 
# 2% blocking if each user averages 2 calls per hour at an average call duration of 3 
# minutes. Assuming that all three trunked systems are operated at maximum capacity, 
# compute the percentage market penetration of each cellular provider. 
blocking_p = 2 / 100
lamda = 2
H = 3 / 60
Au = lamda * H

# System A
channel_a = 19
cell_A = 394
A = 12
Ua = A / Au
subscriber_A = Ua * cell_A
percentage_market_penetration_for_A = (subscriber_A / 2000000) * 100

# System B
channel_b = 57
cell_B = 98
Ab = 45
Ub = Ab / Au
subscriber_B = Ub * cell_B
percentage_market_penetration_for_B = (subscriber_B / 2000000) * 100

# System C
channel_c = 100
cell_C = 49
Ac = 88
Uc = Ac / Au
subscriber_C = Uc * cell_C
percentage_market_penetration_for_C = (subscriber_C / 2000000) * 100

Total_number_of_subscriber = subscriber_A + subscriber_B + subscriber_C
Market_penetration_for_three_system = (Total_number_of_subscriber / 2000000) * 100

print("For system A:")
print("Number of users in System A:", Ua)
print("Total number of subscriber in system A:", subscriber_A)
print("Percentage market penetration for A:", percentage_market_penetration_for_A)

print("\nFor system B:")
print("Number of users in System B:", Ub)
print("Total number of subscriber in system B:", subscriber_B)
print("Percentage market penetration for B:", percentage_market_penetration_for_B)

print("\nFor system C:")
print("Number of users in System C:", Uc)
print("Total number of subscriber in system C:", subscriber_C)
print("Percentage market penetration for C:", percentage_market_penetration_for_C)

print("\nTotal number of subscribers for all three systems:", Total_number_of_subscriber)
print("Market penetration for all three systems:", Market_penetration_for_three_system)

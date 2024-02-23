gos = 0.5 / 100
Au = 0.1
# from table
A = [0.005, 1.13, 3.96, 11.1, 80.9]
c = [1, 5, 10, 20, 100]
# Given blocking probability
print("Blocking Probability : ", gos)
# Traffic intensity per user
print("Traffic intensity per user : ", Au)
# Traffic intensity
print("Traffic intensity : ", A)
print("Channel ", c)

# Calculate number of users
# U = [a / Au for a in A]
# u = [round(u_val) for u_val in U]

U = []
for a in A:
    U.append(a / Au)
u = []
for u_val in U:
    u.append(round(u_val))
print("Number of users ")
print(u)

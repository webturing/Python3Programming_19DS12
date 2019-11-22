

Q = {"zj": 33470027, "tom": 123456, "jerry": 987654321}  # database
print("Q=", Q)
print("len(Q)=", len(Q))

print(Q["tom"])  # query
Q["cat"] = 999  # add/register

print("Q=", Q)

del Q["tom"]  # remove tom
print("Q=", Q)

Q["jerry"] = 9876543210  # update
print("Q=", Q)
Q.pop("cat")
print("Q=", Q)

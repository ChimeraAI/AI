import numpy as np
rawData = []
for i in range(101):
    for j in range(1,101):
        k = i + j
        l = i - j
        m = round(i / j,3)
        n = i * j
        rawData.append(str(i) + " + " + str(j) + " = " + str(k))
        rawData.append(str(i) + " - " + str(j) + " = " + str(l))
        rawData.append(str(i) + " / " + str(j) + " = " + str(m))
        rawData.append(str(i) + " * " + str(j) + " = " + str(n))

print(len(rawData))

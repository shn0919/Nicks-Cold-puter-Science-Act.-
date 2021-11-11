import sys
chicagoTemps = int(input())
coldTemps = 0
temperature = input().split()
for temperature in temperature:
    if int(temperature) < 0:
        coldTemps += 1
print (coldTemps)
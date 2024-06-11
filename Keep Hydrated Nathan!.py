def findlitre(t):
    time=float(input("Enter time Nathan spent cyclin(in hrs): "))
    litres=0.5*time
    roundedlitres=round(litres)
    return roundedlitres

print(findlitre("L"))

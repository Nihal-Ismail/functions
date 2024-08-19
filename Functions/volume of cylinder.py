def volume(r,h):
    print("Radius:",r)
    print("Height:",h)
    v=22/7*(r**2)*h
    return v

radius=3
height=12
print(volume(radius,height).__round__(2))
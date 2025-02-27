# Logical Operations with Arrays
porridge = np.array([79, 65, 50, 63, 56, 90, 85, 98, 79, 51])

cold = porridge[porridge < 60]
print(cold)

hot = porridge[porridge > 80]
print(hot)

just_right = porridge[(porridge >= 60) & (porridge <= 80)]
print(just_right)

a = int(input("Введи перше значення: "))
b = int(input("Введи друге значення: "))
c = int(input("Введи третє значення: "))

D = b**2-4*a*c

if D > 0:
    x1 = int((-b+D**0.5)/2*a)
    x2 = int((-b-D**0.5)/2*a)
    print(f'Перший корінь: {x1}, Другий корінь: {x2}')
elif D < 0:
    print("Розв'язків немає, тому що дискримінант менше 0")
elif D == 0:
    x1 = int(-(b/2*a))
    print(f"Дискримінант має один корінь: {x1}")
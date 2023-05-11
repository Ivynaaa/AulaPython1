# altura= float(input("informe sua autura: "))
# if altura>= 1.9:
#     print("alto")
# elif altura<1.9 and altura >=1.7:
#     print("medio")
# else:
#     print("baixo")
#     if altura<1.4:
#         print("criança")

# Programa que lê 3 lados de um triangulo e informa se é ISOCELES, ESCALENO ou EQUILATERO.
# Informe caso as dimenções não formem um triângulo (se um lado qualquer for maior que a soma de outros)

l1 = float(input("Informe o valor 1:"))
l2 = float(input("Informe o valor 2:"))
l3 = float(input("Informe o valor 3:"))
if l1 < 0 and l2 < 0 and l3 < 0:
    print("lado negativo")
elif l1 > l2+l3 and l2 > l1+l3 and l3 > l2+l1:
    print("as dimenções não formem um triângulo")
else:
    if l1 == l2 and l2 == l3:
        print("Equilatero")
    elif l1 != l2 and l1 != l3 and l2 != l3:
        print("Escaleno")
    else:
        print("isosceles")

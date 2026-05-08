x = int(input("x: "))

par = x % 2 == 0
entre_10 = (x > -10) and (x < 10)
multiplo_3_5 = (x % 3 == 0) or (x % 5 == 0)


print(f"O numero {x} é par? {par}.")
print(f"O numero {x} esta entre -10 e 10? {entre_10}.")
print(f"O numero {x} é multiplo de 3 ou 5? {multiplo_3_5}.")
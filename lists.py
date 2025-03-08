
# Lists 

squares = [1, 2, 3, 4, 5]

print(squares)
print(squares[0]) # Index in order: 0 1 2 3 4 5 .. N
print(squares[-1])
print(squares[-3:])
print(squares + [36, 49, 64, 81, 100]) # adiciona a outra lista ao final da lista existente 

squares.append(233)
print(squares)   

rgb = ["Red", "Green", "Blue"]
esc = []
rgb = esc
id(rgb) == id(esc)
esc.append("Alph")
print(rgb)
print(esc)


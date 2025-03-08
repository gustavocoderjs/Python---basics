
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

letters = ['a', 'b', 'c', 'd', 'e']

print(letters[2:5])

lettersTwo = letters[2:5] = []
print(lettersTwo)

lettersThree = letters[:] = []
print(lettersThree)

print(len(letters))

# How to create lists containing another lists 

a = ['x', 'y', 'z']
n = ['7', '8', '9']

q = [a, n]
print(q)

print(q[1][2])

print("Another concept:")

# Fibonacci Series

a, b = 0, 1
while a < 10:
    print(a)
    a, b = b, a + b

     
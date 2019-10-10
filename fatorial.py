num = int(input())
fatorial = 1

for c in range(num, 0, -1):
    fatorial *= c

print(f"O fatorial de {num} é {fatorial}\n")

num = int(input())

fatorial = 1

for c in range(1, num+1):
    fatorial *= c
    
print(f"O fatorial de {num} é {fatorial}")
    

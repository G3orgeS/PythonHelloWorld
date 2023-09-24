num = []

amountNum = int(input('Hur många nummer vill du ange?'))

for i in range(amountNum):
    number = float(input(f'Ange nummer #{i+1}: '))
    num.append(number)

average = sum(num) / len(num)
smallest = min(num)
largest = max(num)

print(f"Numren du angav: {num}")
print(f"Medelvärde: {average:.2f}")
print(f"Lägsta: {smallest}")
print(f"Högsta: {largest}")
    
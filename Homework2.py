# На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.
# coins = [0, 1, 0, 1, 1, 0]
# 3

number = int(input("input count of coins: "))
coins = []

for i in range(number):
    while True:
        coin = int(input(f'insert coin value {i + 1} (0 - heads, 1 - tails): '))
        if coin == 0 or coin == 1:
            coins.append(coin)
            break
        else:
            print('wrong input :(')

count_heads = coins.count(0)
count_tails = coins.count(1)

min_flips = min(count_heads, count_tails)

print(f'\ncoins = [{", ".join(map(str, coins))}]')
print(f'min flips: {min_flips}')

# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя –
# школьница. Петя помогает Кате по математике. Он задумывает два
# натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
# этого Петя делает две подсказки. Он называет сумму этих чисел S и их
# произведение P. Помогите Кате отгадать задуманные Петей числа.
# input S = 12 P = 27
# output 3 9 or 9 3

S = int(input("\nS = "))
P = int(input("P = "))

x = 1
flag = False

while x < S:
        if P % x == 0:
            y = P // x
            if x + y == S:
                flag = True
                break
        x += 1
if flag and x != y:
    print(f'\nfound numbers X = {x} and Y = {y}')
    print(f'or numbers    X = {y} and Y = {x}')
elif flag and x == y:
    print(f'\nfound numbers X = {x} and Y = {y}')  
else:
    print("error :(")

# Задача 14: Требуется вывести все целые степени двойки (т.е. числа
# вида 2k), не превосходящие числа N.

# n=16

# #Вывод
# 1
# 2
# 4
# 8
# 16

n = int(input("\ninput number: "))
power_of_two = 1
list = []

for i in range(n + 1):
    power_of_two = 2 ** i
    if power_of_two <= n: 
        list.append(power_of_two)
    else:
        break
    
print(f'{n} -> {", ".join(map(str, list))}')

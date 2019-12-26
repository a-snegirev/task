import numpy as np
import math
import string
print(np.sum(np.arange(1,2**25 + 1,1, dtype='int64'))) # Сумма чисел от 1 до 2**25

print(math.factorial(1000)) #1000!

print([(x,y) for x in ['a','b','c','d','e','f','g','h'] for y in range(9)]) # Поля морского боя

print([2*x for x in [1,3,6,4,8] if x%2 != 0 ]) # Удвоить нечетные числа

print(len([x for x in ['text.txt'] if x == 'z' ])) # Посчитать z

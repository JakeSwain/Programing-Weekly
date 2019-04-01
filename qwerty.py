import math
import time

board = list('qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM')
row1 = list('qwertyuiop')
row2 = list('asdfghjkl')
row3 = list('zxcvbnm')

def qwe(str, n):
    t0 = time.time()
    new = []
    key = [(n//(10**i))%10 for i in range(math.ceil(math.log(n, 10))-1, -1, -1)]
    # key = [int(i) for i in str(n)]
    str = list(str)
    for letter in str:
        count = -1
        for letter_2 in board:
            count += 1
            if letter == letter_2:
                if count <= 9:
                    new.append(row1[(count + (key[0]-1)) % len(row1)])
                elif 10 <= count <= 18:
                    new.append(row2[(count + (key[1]-1)) % len(row2)])
                elif 19 <= count <= 25:
                    new.append(row3[(count + (key[2]-1)) % len(row3)])
                else:
                    new.append('>')

    new_final = ''.join(new)
    t1 = time.time()
    print(t1 - t0)
    return new_final


print(qwe('Ball', 134))

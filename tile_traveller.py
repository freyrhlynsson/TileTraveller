# Harðkóða inn veggi í borðið
# Lýsa stöðu spilara sem talnapari x og y
# Tékka í allar áttir hvort x eða y verða 0 eða 4, eða hvort þær fara í gegnum vegg
# Skrifa út mögulegar áttir
# Fá leifilega átt og hreyfa
# Tékka hvenær spilari vinnur

# abcd (1 eða 0 fyrir hvort áttin sé lögleg eða ekki) NESW
def is_border(x,y):
    if x == 1 and y == 1:
        return '1000'
    elif x == 2 and y == 1:
        return '1000'
    elif x == 3 and y == 2:
        return '1010'
    elif x == 2 and y == 3:
        return '0101'
    elif x == 2 and y == 2:
        return '0011'
        
    total = ''
    if y+1 == 4:
        total += '0'
    else:
        total += '1'
    if x+1 == 4:
        total += '0'
    else:
        total += '1'
    if y-1 == 0:
        total += '0'
    else:
        total += '1'
    if x-1 == 0:
        total += '0'
    else:
        total += '1'
    return total

def is_win(x,y):
    if x == 3 and y == 1:
        return True
    return False

x,y = 2,2
has_won = is_win(x,y)
while not has_won:
    direction_num = is_border(x,y)
    ques = ''
    k = 0
    for i in direction_num:
        if k > 0:
            ques += ' or '
        if k == 0 and i == '1':
            ques += '(N)orth'
        elif k == 1 and i == '1':
            ques += '(E)ast'
        elif k == 2 and i == '1':
            ques += '(S)outh'
        elif k == 3 and i == '1':
            ques += '(W)est'
        k+= 1
    print(ques)
    print = ('You can travel: ')
    direction = input("Direction: ")
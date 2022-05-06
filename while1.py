money = 799
transfer = 10000

print('Check:', money < transfer)

while money < transfer:
    print('please fill the blank again!')
    transfer = float(input('New Transfer: '))
    if transfer > 1000000:
        print('call for the manager')
        break

print('passed! you can transfer')
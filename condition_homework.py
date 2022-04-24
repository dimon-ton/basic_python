
print('\n\n**********************Temparature Converter**********************\n\n')
print('-----Celcius to Fahrenheit(default): Type "CTF"-----')
print('-----Celcius to Kelvin: Type "CTK"-----')
print('-----Fahrenheit to Celcius: Type "FTC"-----')
print('-----Fahrenheit to Kelvin: Type "FTK"-----')
print('-----Kelvin to Celcius: Type "KTC"-----')
print('-----Kelvin to Fahrenheit: Type "KTF"-----')

def condit(tempType='CTF',tempValue=0):
    if tempType == 'CTF':
        # ----------Celcius to Fahrenheit----------
        result = 9/5*tempValue+32
        postFix = 'Fahrenheit'
        strInput = 'Celcius'
        return [result,postFix,strInput]
    elif tempType == 'CTK':
        # ----------Celcius to Kelvin----------
        result = tempValue+273
        postFix = 'Kelvin'
        strInput = 'Celcius'
        return [result,postFix,strInput]
    elif tempType == 'FTC':
        # ----------Fahrenheit to Celcius----------
        result = 5/9*(tempValue-32)
        postFix = 'Celcius'
        strInput = 'Fahrenheit'
        return [result,postFix,strInput]
    elif tempType == 'FTK':
        # ----------Fahrenheit to Kelvin----------
        result = 5/9*(tempValue-32)+273.15
        postFix = 'Kelvin'
        strInput = 'Fahrenheit'
        return [result,postFix,strInput]
    elif tempType == 'KTC':
        # ----------Kelvin to Celcius----------
        result = tempValue-273
        postFix = 'Celcius'
        strInput = 'Kelvin'
        return [result,postFix,strInput]
    else:
        # ----------Kelvin to Fahrenheit----------
        result = 9/5*(tempValue-273)+32
        postFix = 'Fahrenheit'
        strInput = 'Kelvin'
        return [result,postFix,strInput]

print('\nchoose which unit do you want to convert!')
tempType = input(': ')

condit()
print(f'\n-----Please fill the --{condit()[2]}-- value of the temparature.-----')
convert = ['CTF','CTK','FTC','FTK','KTC','KTF']

try:

    tempValue = float(input(': '))


    if tempType == '':
        lsresult = f'\n***the result is {condit("CTF",tempValue)[0]} {condit("CTF",tempValue)[1]} degree***'
    elif tempType.isnumeric() == True:
        lsresult = '\nError, Plese enter some charecters! in "choose which unit do you want to convert!"'
    else:
        for c in convert:
                if c == tempType:
                    lsresult = f'\n***the result is {condit(tempType,tempValue)[0]} {condit(tempType,tempValue)[1]} degree***'
                    break
                else:
                    lsresult = '\nError, please enter the existing charecter! in "choose which unit do you want to convert!'
except ValueError:
    lsresult = "\nError, Please enter a number as the temparature"

print(lsresult)

print('\n\n--------reference:https://www.trueplookpanya.com/blog/content/66152/-blo-sciphy-sci---------\n\n')
friend = ['Korkai','Khorkai','Khorkwai','Somchai','Samsak']
friend2 = {'Korkai':'kai',
            'Khorkai':'mai'
            }

visitor = 'Korkai'

if visitor in friend or visitor.title() in friend:
    print('is my friend')
    if visitor in friend2 or visitor.title() in friend2:
        print('Hello '+ friend2[visitor.title()])
    else:
        print('Hello customer')
else:
    print('Who is you?')
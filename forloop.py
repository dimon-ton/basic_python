for i in range(5):
    print('Hello',i+1)

friend = ['Korkai','Khorkai','Khorkwai','Somchai','Samsak']

for f in friend:
    print(f)
    if f == 'Korkai':
        print('Hello Korkai')
    else:
        print('Hell customer')

friend2 = {'Korkai':'kai',
            'Khorkai':'mai',
            'Somchai':'chai'}
for k,v in friend2.items():
    print('t',k)
    print('t',v)
for f in friend2.keys():
    print(f)
for f in friend2.values():
    print(f)

for i,f in enumerate(friend,start=10):
    print(i,f)

for i,f in enumerate(friend2.items()):
    print('order',i,f)

for i,(k,v) in enumerate(friend2.items()):
    print('order',i,k,v)

print('order',i,k,v)

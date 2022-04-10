fav_language = {
    'jen': ['python','ruby'],
    'sarah':['c'],
    'edward':['ruby','go'],
    'phil':['python','haskell']
}

#Show all responses fo each person.
for name, langs in fav_language.items():
    print(name + ': ')
    for lang in langs:
            print('= ' + lang)
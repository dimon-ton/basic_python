from first import First


class Second:
    pass

if __name__ == '__main__':
    print(f'นี่คือภาษา {First.language}')
    First.learn()

    first = First()
    first.teach()

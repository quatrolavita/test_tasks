def foo() -> None:

    for i in range(11, 80):

        if i % 3 == 0 and i % 5 == 0:
            print('$$@@')
            continue

        elif i % 3 == 0:
            print('$$')
            continue

        elif i % 5 == 0:
            print('@@')
            continue
        print(i)


if __name__ == '__main__':

    foo()

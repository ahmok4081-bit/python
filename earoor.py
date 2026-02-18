try:
    f = open('name.txt')
except FileNotFoundError:
    print('hey! ideiot')
finally:
    print('finished opennig your file ')
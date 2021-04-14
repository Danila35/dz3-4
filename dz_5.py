"""
Задание 5
"""

def keyboard(numb=32):
    if numb == 128:
        return 0
    print(f' {numb} - {keyboard(numb)}')

    if (numb - 31) % 10 == 0:
        print('\n')

    keyboard(numb + 1)

keyboard()

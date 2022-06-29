#!/usr/bin/python3
for numbers in range(0, 100):
    if numbers != 99:
        print(f'{numbers:02}', end=", ")
    else:
        print(f'{numbers}')

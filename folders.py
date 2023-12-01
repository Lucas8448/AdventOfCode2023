import os

days = 24
parts = 2

for day in range(1, days + 1):
    for part in range(1, parts + 1):
        os.makedirs(f'Day{day}/Part{part}')
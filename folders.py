import os

days = 24
parts = 2

for day in range(1, days + 1):
    for part in range(1, parts + 1):
        # create folders for each day and part if they dont exist
        if not os.path.exists(f'Day{day}'):
          os.makedirs(f'Day{day}')
        if not os.path.exists(f'Day{day}/Part{part}'):
          os.makedirs(f'Day{day}/Part{part}')
        # add input.txt and solution.py in each folder
        with open(f'Day{day}/Part{part}/input.txt', 'w') as f:
          pass
        with open(f'Day{day}/Part{part}/solution.py', 'w') as f:
          pass
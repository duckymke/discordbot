from datetime import date
from dates import dates
import random

def date_generator(dates):
    random_date = random.choice(dates)

    print(f'beep boop bap... the date generator ^tm has picked: {random_date}')

    

date_generator(dates)


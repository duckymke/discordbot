from datetime import date
from dates import dates
import random

def date_generator(dates, sentence):
    random_date = random.choice(dates)

    date = (f'{sentence} {random_date}')
    print(date)

    return date

# date_generator(dates)

import random

def random_agent(observation, configuration):
    '''Агент, который выбирает случайный ход.'''
    return random.randrange(0, configuration.signs)

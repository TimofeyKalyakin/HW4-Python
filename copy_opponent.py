
import random

def copy_opponent(observation, configuration):
    '''Агент, где копируется предыдущий ход оппонента'''
    if observation.step > 0:
        return observation.lastOpponentAction
    else:
        return random.randrange(0, configuration.signs)

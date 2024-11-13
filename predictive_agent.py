
import random

def predictive_agent(observation, configuration):
    '''Агент, который предсказывает следующий ход оппонента на основе его прошлого хода.'''
    if observation.step == 0:
        return random.randrange(0, configuration.signs)  # случайный первый ход
    else:
        # Если оппонент выбрал камень (0), ожидаем ножницы (2), и наоборот
        if observation.lastOpponentAction == 0:
            return 1  # выбираем бумагу
        elif observation.lastOpponentAction == 1:
            return 2  # выбираем ножницы
        else:
            return 0  # выбираем камень

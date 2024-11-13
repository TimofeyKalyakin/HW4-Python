def cycle_agent(observation, configuration):
    '''Агент, который циклично выбирает камень, бумага, ножницы.'''
    return observation.step % 3

import time
import numpy as np

def sleep_rand_time(min_sleep, max_sleep):
    """
    sleep for a random time period (between min_sleep and max_sleep seconds)
    """

    n_seconds = np.random.randint(min_sleep, max_sleep)
    time.sleep(n_seconds)
    

def print_press_key_message():
    """
    """
    print "Press key as fast as possible"


def print_event_after_rand_time(min_sleep, max_sleep):
    """
    """
    sleep_rand_time(min_sleep, max_sleep)
    print_press_key_message()


def get_time_until_input():
    """
    """
    t_start = time.time()
    raw_input()
    reaction_time = time.time() - t_start
    return reaction_time


def get_reaction_time(min_sleep, max_sleep):
    """
    """
    print_event_after_rand_time(min_sleep, max_sleep)
    t_react = get_time_until_input()

    return t_react


def guess_age(react_age_factor):
    """
    """

    if not isinstance(react_age_factor, (int, long, float)):
        raise TypeError('react_age_factor must be a number!')

    if react_age_factor <= 0:
        raise ValueError('react_age_factor must be greater then zero!')
    
    min_sleep = 4
    max_sleep = 9
    t_react = get_reaction_time(min_sleep, max_sleep)
    guessed_age = t_react * react_age_factor

    return guessed_age


if __name__ == "__main__":

    react_age_factor = 100
    
    guessed_age = guess_age(react_age_factor)

    print "I guess you are {} years old".format(guessed_age)

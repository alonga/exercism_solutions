# Constants
# Constants
EXPECTED_BAKE_TIME = 40  # expected bake time in minutes per lasagna recipe
PREPARATION_TIME_PER_LAYER = 2  # minutes per layer

def bake_time_remaining(elapsed_bake_time):
    """
    Return the remaining bake time (in minutes).

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time derived from 'EXPECTED_BAKE_TIME'.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers):
    """
    Return total preparation time (in minutes) based on number of layers.

    :param number_of_layers: int - number of layers in lasagna.
    :return: int - total preparation time.
    """
    return number_of_layers * PREPARATION_TIME_PER_LAYER


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """
    Return total elapsed cooking time (in minutes).

    :param number_of_layers: int - number of layers in lasagna.
    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - total time spent (prep + bake so far).
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time

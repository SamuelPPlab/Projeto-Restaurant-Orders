from typing import Callable


def count(callback: Callable[[set], bool], items: list):
    count_value = 0

    for item in items:
        if callback(item):
            count_value += 1

    return count_value

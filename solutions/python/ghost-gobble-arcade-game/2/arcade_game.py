"""Pac-Man game logic functions.

This module defines simple boolean functions that determine
game outcomes such as whether Pac-Man can eat a ghost,
score points, lose a life, or win the game.
"""

def eat_ghost(power_pellet_active: bool, touching_ghost: bool) -> bool:
    """Return True if Pac-Man can eat a ghost."""
    return power_pellet_active and touching_ghost


def score(touching_power_pellet: bool, touching_dot: bool) -> bool:
    """Return True if Pac-Man has scored by touching a power pellet or dot."""
    return touching_power_pellet or touching_dot


def lose(power_pellet_active: bool, touching_ghost: bool) -> bool:
    """Return True if Pac-Man loses (touches a ghost without a power pellet)."""
    return not power_pellet_active and touching_ghost


def win(has_eaten_all_dots: bool, power_pellet_active: bool, touching_ghost: bool) -> bool:
    """Return True if Pac-Man wins by eating all dots without losing."""
    return has_eaten_all_dots and not lose(power_pellet_active, touching_ghost)

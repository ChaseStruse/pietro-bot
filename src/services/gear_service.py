"""
This file contains all functions related to the player / guild's gear.
"""


def get_gear_score(ap, awakening_ap, dp) -> str:
    """
    Takes in the users AP, Awakening AP, and DP and then calculates what their Gear Score would be based on BDO's
    calculator logic.
    :param ap: Users AP that can be found in the inventory (i) menu
    :param awakening_ap: Users Awakening AP that can be found in the inventory (i) menu
    :param dp: Users DP that can be found in the inventory (i) menu
    :return: None
    """
    gear_score = int(((ap + awakening_ap) / 2) + dp)
    return str(gear_score)

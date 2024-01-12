#!/usr/bin/python3
"""
    LockedClass iModule
"""


class LockedClass():

    """
    This prevenet user from create an instance
    except it is called first name

    """
    __slot__ = ['first_name']

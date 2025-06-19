"""
search() - O(1)
insert() - O(1)
remove() - O(1)
"""


class Node:
    def __init__(self, value=None):
        self.value = value
        self.nextnode = None


class HashMap:
    def __init__(self, size):
        self.table = [] * size
# test

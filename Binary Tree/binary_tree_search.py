"""
Binary Search Tree Algorithm
"""
from typing import Generic, TypeVar
from pprint import pformat

T = TypeVar("T")


class Node(Generic[T]):

    def __init__(self, value: T, parent: T) -> None:
        self.value = value
        self.parent = parent
        self.left = None
        self.right = None

    def __repr__(self) -> str:

        if self.left is None and self.right is None:
            return str(self.value)

        return pformat({"%s" % {self.value}: (self.left, self.right)}, indent=1)


class BinarySearchTree(Generic[T]):

    def __init__(self, root: T) -> None:
        self.root: T | None = None

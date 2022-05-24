# Fixed bugs with raising proper value errors

def main():
    n = int(input('Input a positive integer n for the length of the initial array: '))
    id_array = QuickUnion(n)

    print(id_array.id_array)
    print(f"The current root of 4 is: {id_array.root(4)}")
    id_array.union(4, 5)
    print(f"The changed root of 4 is: {id_array.root(4)}")
    print(f"The current root of 3 is: {id_array.root(3)}")
    id_array.union(3, 4)
    print(f"The changed root of 3 is: {id_array.root(3)}")


class QuickUnion():

    def __init__(self, number_of_elements: int) -> None:
        self.number_of_elements = number_of_elements

        self.id_array = list(range(self.number_of_elements))

    def root(self, element: int) -> int:
        n = self.number_of_elements - 1
        if (0 <= element <= n):
            while (element != self.id_array[element]):
                element = self.id_array[element]
            return element
        else:
            raise ValueError(
                f'The element to look up root for must be an integer in the interval [0, {n}]')

    def connected(self, element_1: int, element_2: int) -> bool:
        n = self.number_of_elements - 1
        if (0 <= element_1 <= n) and (0 <= element_2 <= n):
            if self.root(element_1) == self.root(element_2):
                return True
            else:
                return False
        else:
            raise ValueError(
                f"The elements to check for connection must be an integer in the interval [0, {n}]")

    def union(self, element_1: int, element_2: int) -> None:
        # Change root of element_1 to root of element_2, i.e, connect them
        n = self.number_of_elements - 1
        if (0 <= element_1 <= n) and (0 <= element_2 <= n):
            i = self.root(element_1)
            j = self.root(element_2)

            self.id_array[i] = j
        else:
            raise ValueError(
                f"The elements to connect must be an integer in the interval [0, {n}]")


if __name__ == "__main__":
    main()

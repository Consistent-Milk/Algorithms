def main():
    n = 6
    QuickFind_instance = QuickFind(n)
    print(f"The initial array is : {QuickFind_instance.id_array}")
    QuickFind_instance.union(1,2)
    print(f"Array after applying union(1,2): {QuickFind_instance.id_array}")
    QuickFind_instance.union(1,3)
    print(f"Array after applying union(1,3): {QuickFind_instance.id_array}")
    print(f"Comment: connected(2,3) should now return true.")
    print(f"connected(2,3) returns {str(QuickFind_instance.connected(2,3))}")
    print(f"Comment: connected(2,5) should now return false.")
    print(f"connected(2,5) returns {str(QuickFind_instance.connected(2,5))}")
    print(f"Comment: connected(2,6) should raise a ValueError")
    QuickFind_instance.connected(2,6)

class QuickFind:

    def __init__(self, number_of_elements:int) -> None:
        self.number_of_elements = number_of_elements

        self.id_array = list(range(self.number_of_elements))

    def connected(self, p: int, q: int) -> bool:
        n = self.number_of_elements - 1
        if (0<=p<=n) and (0<=q<=n):
            if self.id_array[p] == self.id_array[q]:
                return True
            else:
                return False 
        else:
            raise ValueError(f"The value of p and q must be and integer in the interval [0,{n}]")

    def union(self, p: int, q: int) -> None:
        n = self.number_of_elements - 1
        if (0<=p<=n) and (0<=q<=n):
            pid = self.id_array[p]
            qid = self.id_array[q]

            for i in range(0, len(self.id_array)):
                if (self.id_array[i] == pid):
                    self.id_array[i] = qid
        else:
            raise ValueError(f"The value of p and q must be an integer in the interval [0,{n}]")

if __name__ == "__main__":
    main()
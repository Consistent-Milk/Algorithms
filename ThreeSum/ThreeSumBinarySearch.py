def main():
    data_array = list(range(-10, 15))

    ThreeSumBinarySearh_instance = ThreeSumBinarySearh(data_array)

    print(
        f"The number of triples that sum to zero are: {ThreeSumBinarySearh_instance.count()}")


class ThreeSumBinarySearh:

    def __init__(self, data_array: list) -> None:
        self.data_array = sorted(data_array)

    def binary_search(self, array: list, x: int, low: int, high: int) -> bool:

        while low <= high:

            mid = low + (high - low)//2

            if array[mid] == x:
                return True

            elif array[mid] < x:
                low = mid + 1

            else:
                high = mid - 1

        return False

    def count(self) -> int:

        a = self.data_array
        n = len(a)
        count = 0

        for i in range(0, n):
            for j in range(i+1, n):
                # Optimize the algorithm by reducing the number of array accesses by using binary search
                search_array = a[j+1:n]
                key = -(a[i] + a[j])
                low = 0
                high = len(search_array) - 1
                if self.binary_search(search_array, key, low, high):
                    count += 1
                else:
                    continue

        return count


if __name__ == "__main__":
    main()

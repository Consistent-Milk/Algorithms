# Brute force algorithm but I also added the triplets list for ease of visualization.
import timeit


def main():
    # Small dataset for visualizing algorithm
    data_array_1 = list(range(-10,15))
    # Larger dataset for analyzing run time
    data_array_2 = list(range(-100,200))
    algorithm_instance_1 = ThreeSumBrute(data_array=data_array_1)
    algorithm_instance_2 = ThreeSumBrute(data_array=data_array_2)

    zero_triples_counter, zero_triples_list = algorithm_instance_1.count()

    print(f"The small data array for visualization is: {data_array_1}")
    print(
        f"The total count of triples that sum to zero in the given array is: {zero_triples_counter}")
    print(f"The list of triplets that sum to zero is {zero_triples_list}")

    print("Timer for actual Brute force algorithm without triplet list:")
    print("Timer:\t", timeit.timeit(
        f"{algorithm_instance_2.count_with_timer()}"))


class ThreeSumBrute():

    def __init__(self, data_array: list) -> None:
        self.data_array = data_array

    def count(self) -> tuple:
        a = self.data_array
        n = len(self.data_array)
        count = 0
        triplet_list = []

        for i in range(0, n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    if (a[i] + a[j] + a[k] == 0):
                        count += 1
                        triplet_list.append([a[i], a[j], a[k]])
        return (count, triplet_list)

    def count_with_timer(self) -> tuple:
        a = self.data_array
        n = len(self.data_array)
        count = 0

        for i in range(0, n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    if (a[i] + a[j] + a[k] == 0):
                        count += 1
        return count


if __name__ == "__main__":
    main()

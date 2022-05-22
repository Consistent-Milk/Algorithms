# Brute force algorithm but I also added the triplets list for ease of visualization. 

def main():
    data_array = list(map(int, input('Enter space seperated integers: ').split()))
    algorithm_instance = ThreeSumBrute(data_array=data_array)
    zero_triples_counter, zero_triples_list = algorithm_instance.count()

    print(
        f"The total count of triples that sum to zero in the given array is: {zero_triples_counter}")

    print(f"The list of triplets that sum to zero is {zero_triples_list}")


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


if __name__ == "__main__":
    main()

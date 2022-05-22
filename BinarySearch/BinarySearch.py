import random


def main():
    # Produce a random array of distinct integers
    a = int(input("Enter the lower range for random integer selection: "))
    b = int(input("Enter the upper range for random integer selection: "))
    print(f"The next value should be in the range (1, {abs(a)+abs(b)})")
    n = int(input(f"Ente how many maximum random samples you want in the array: "))
    array = list(set(random.sample(range(a, b), n)))

    print(
        f"The initial unsorted array of distinct random samples after dropping duplicate elements is of length {len(array)}: {array}")
    print(
        f"The sorted array of length {len(array)} of distinct elements is: {sorted(array)}")

    # Important step, the array must be sorted before binary search is used.
    array = sorted(array)

    element = int(
        input('Enter an element to search for in the sorted array: '))

    result = binary_search(array, element, 0, len(array)-1)

    if result != -1:
        print("Element is present at index " + str(result))
    else:
        print("The element is not in the array.")


def binary_search(array, x, low, high):

    # Repeat until the pointers low and high meet each other
    while low <= high:

        mid = low + (high - low)//2

        if array[mid] == x:
            return mid

        elif array[mid] < x:
            low = mid + 1

        else:
            high = mid - 1

    return -1


if __name__ == "__main__":
    main()

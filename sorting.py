import random
import matplotlib.pyplot as plt

def random_numbers(count, low=0, high=100):
    return [random.randint(low, high) for _ in range(count)]

def selection_sort(seznam):
    numbers = seznam[:]
    print(numbers)
    for min_index in range(len(numbers)):
        min_value = numbers[min_index]
        min_ind = min_index
        for i in range(min_index, len(numbers)):
            number = numbers[i]
            if number < min_value: #slozitost O(n**2)
                min_ind = i
                min_value = number
        numbers[min_index], numbers[min_ind] = numbers[min_ind], numbers[min_index]
    return numbers

def bubble_sort(seznam):
    plt.ion()
    plt.show()

    print(seznam)
    numbers = seznam[:]

    posledni_pozice = len(numbers)
    for i in numbers:
        for index in range(1, posledni_pozice):
            if numbers[index] < numbers[index -1]: #slozitost O(n**2)
                numbers[index], numbers[index-1] = numbers[index-1], numbers[index]
                posledni_pozice = index
                print(numbers)

                #matplotlib blok
                index_highlight1 = index
                index_highlight2 = index -1
                colors = ["steelblue"] * len(numbers)
                colors[index_highlight1] = "tomato"
                colors[index_highlight2] = "tomato"
                plt.clf()
                plt.bar(range(len(numbers)), numbers, color=colors)
                plt.title("Bubble Sort")
                plt.pause(0.1)

    plt.ioff()
    plt.show()

    return numbers


def main():
    r = random_numbers(50)
    sorted = bubble_sort(r)

    print(sorted)

if __name__ == "__main__":
    main()

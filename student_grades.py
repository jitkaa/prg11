from sorting import random_numbers

class StudentsGrades:
    def __init__(self, scores):
        self.scores = scores

    def get_by_index(self, index):
        return self.scores[index]

    def count(self):
        return len(self.scores)

    def find(self, score):
        result = []
        for index, i in enumerate(self.scores,start = 0):
            if i == score:
                result.append(index)
        return result

    def get_sorted(self):
        numbers = self.scores[:]

        posledni_pozice = len(numbers)
        for i in numbers:
            for index in range(1, posledni_pozice):
                if numbers[index] < numbers[index - 1]:  # slozitost O(n**2)
                    numbers[index], numbers[index - 1] = numbers[index - 1], numbers[index]
                    posledni_pozice = index
        return numbers

    def get_grade(self, index):
        body = self.scores[index]

        if body >= 90:
            return "A"
        elif body >= 80:
            return "B"
        elif body >= 70:
            return "C"
        elif body >= 60:
            return "D"
        elif body >= 50:
            return "E"
        else:
            return "F"



def main():
    results = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])

    print(f"psalo test: {results.count()}")
    index = 0
    for student in results.scores:
        print(f"Student: {index}: {student} points - {results.get_grade(index)}")
        index += 1

    print(f"Plný počet: {results.find(100)}")
    print(f"seřazené výsledky: {results.get_sorted()}")

    random_results = StudentsGrades(random_numbers(30, 0, 100))
    print(random_results.count())
    print(random_results.get_sorted())

if __name__ == "__main__":
    main()



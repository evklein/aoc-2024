from .problem import Problem

class Day1(Problem):
    def day1_parse(self, input):
        num_elements = len(input)
        left, right = [None] * num_elements, [None] * num_elements
        for i in range(num_elements):
            pieces = input[i].split(' ' * 3)
            left[i] = int(pieces[0])
            right[i] = int(pieces[1])
        return left, right

    def PartA(self, input):
        super().PartA()
        left, right = self.day1_parse(input)
        left, right = sorted(left), sorted(right)
        return sum(abs(l - r) for l, r in zip(left, right))

    def PartB(self, input):
        super().PartB()
        left, right = self.day1_parse(input)
        return sum(l * right.count(l) for l in left)
from .problem import Problem

from collections import namedtuple

RecordResult = namedtuple('RecordResult', ['safe', 'diffs'])

class Day2(Problem):

    def PartA(self, input):
        reports = [[int(l) for l in r.split()] for r in input]
        solution = sum(1 for r in reports if self.report_is_safe(r).safe)
        return solution

    def report_is_safe(self, report):
        level_diffs = [report[i + 1] - report[i] for i in range(len(report) - 1)]
        one_direction = all(l > 0 for l in level_diffs) or all(l < 0 for l in level_diffs)
        left, right = abs(min(level_diffs)), abs(max(level_diffs))
        safe = 1 <= left <=3 and 1 <= right <= 3 and one_direction
        return RecordResult(safe, level_diffs)

    def PartB(self, input):
        solution = 0
        reports = [[int(l) for l in r.split()] for r in input]
        for report in reports:
            if self.report_is_safe(report).safe:
                solution += 1
                continue

            for i in range(len(report)):
                updated_report = report[:i] + report[(i + 1):]
                if self.report_is_safe(updated_report).safe:
                    solution += 1
                    break
        return solution

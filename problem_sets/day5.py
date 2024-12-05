from .problem import Problem
from collections import deque

# Do not run raw
class Day5(Problem):
    def parse_input(self, input):
        rules = {}
        for rule in input[:input.index('\n')]:
            before, after = map(int, rule.split('|'))
            rules[before] = rules.get(before, []) + [after]
        updates = [list(map(int, u.split(','))) for i, u in enumerate(input[input.index('\n') + 1:])]
        return rules, updates

    def get_acceptable_updates(self, rules, updates):
        accepted_updates = []
        for i, update in enumerate(updates):
            accepted = True
            for j, page_update in enumerate(update):
                relevant_rules = rules.get(page_update, [])
                found_indices = [i for i, x in enumerate(update) if x in relevant_rules if i < j]
                if found_indices:
                    accepted = False
                    break
            if accepted:
                accepted_updates.append(update)
        return accepted_updates

    def PartA(self, input):
        rules, updates = self.parse_input(input)
        accepted_updates = self.get_acceptable_updates(rules, updates)
        # Return summation of middle entries for each accepted update
        return sum(update[len(update) // 2] for update in accepted_updates)

    def PartB(self, input):
        rules, updates = self.parse_input(input)
        problem_updates = [update for update in updates if update not in self.get_acceptable_updates(rules, updates)]
        fixed_updates = []
        for i, update in enumerate(problem_updates):
            stack = []
            for j, page_update in enumerate(update):
                relevant_rules = rules.get(page_update, [])
                found_indices = [k for k, x in enumerate(stack) if x in relevant_rules and k < j]
                if found_indices:
                    min_index = min(found_indices)
                    pop_values = []
                    for _ in range(j - min_index):
                        pop_values.append(stack.pop())
                    stack.append(page_update)
                    stack.extend(reversed(pop_values))
                else:
                    stack.append(page_update)
            fixed_updates.append(stack)
        return sum(update[len(update) // 2] for update in fixed_updates)

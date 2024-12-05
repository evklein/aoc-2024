from .problem import Problem

# Do not run raw
class Day5(Problem):
    def PartA(self, input):
        # Parse input
        rules = {}
        for rule in input[:input.index('\n')]:
            before, after = map(int, rule.split('|'))
            rules[before] = rules.get(before, []) + [after]
        updates = [list(map(int, u.split(','))) for i, u in enumerate(input[input.index('\n') + 1:])]

        # Find acceptable updates, given ruleset
        accepted_updates = []
        for i, update in enumerate(updates):
            accepted = True
            for j, page_update in enumerate(update):
                relevant_rules = rules.get(page_update, [])
                found_indices = [i for i, x in enumerate(update) if x in relevant_rules]
                if any(index < j for index in found_indices):
                    accepted = False
                    break
            if accepted:
                accepted_updates.append(update)

        # Return summation of middle entries for each accepted update
        return sum(update[len(update) // 2] for update in accepted_updates)

    def PartB(self, input):
        pass
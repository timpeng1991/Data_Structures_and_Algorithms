# python3

import sys

class Bracket:
    def __init__(self, bracket_type, position):
        self.bracket_type = bracket_type
        self.position = position

    def Match(self, c):
        if self.bracket_type == '[' and c == ']':
            return True
        if self.bracket_type == '{' and c == '}':
            return True
        if self.bracket_type == '(' and c == ')':
            return True
        return False

if __name__ == "__main__":
    text = sys.stdin.read()

    opening_brackets_stack = []
    error_index = 0

    for i, next in enumerate(text):
        if next == '(' or next == '[' or next == '{':
            # push opening brackets into stack
            # Position is i + 1 (1-based index)
            opening_brackets_stack.append(Bracket(next, i + 1))

        if next == ')' or next == ']' or next == '}':
            # if the stack is empty, then here is the first unmatched closing bracket
            if not opening_brackets_stack:
                error_index = i + 1
                break

            # top is the last bracket in the stack
            top = opening_brackets_stack.pop()
            # if the opening bracket does not match with the last bracket in the stack
            if not top.Match(next):
                error_index = i + 1
                break

    if error_index != 0:
        print(error_index)
    # unmatched opening if the stack is not empty
    elif opening_brackets_stack:
        print(opening_brackets_stack[0].position)
    else:
        print('Success')
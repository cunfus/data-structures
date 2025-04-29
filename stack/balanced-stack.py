import sys
import os
sys.path.append(os.path.dirname(__file__))

from stack import Stack


def is_balanced(expression):

    s = Stack()
    mapping = {')':'(', ']':'[', '}':'{'}

    for token in expression:
        if token in "([{":
            s.push(token)
        elif token in "}])":
            if s.is_empty() or s.peek() != mapping[token]:
                return False
            s.pop()

    return s.is_empty()

if __name__ == "__main__":

    result = is_balanced("{[()]}")
    result = is_balanced("{[(])}")
    result = is_balanced("{[()]")
    result = is_balanced("[()]}")
    print(result)
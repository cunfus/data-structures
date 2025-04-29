import sys
import os
sys.path.append(os.path.dirname(__file__))

from stack import Stack

def cal_postfix(postfix: str):
    s = Stack()

    for ch in postfix:
        if ch.isspace():
            continue
        elif ch.isdigit():
            s.push(ch)
        else:
            op1 = s.pop()
            op2 = s.pop()
            result = eval(op1 + ch + op2)
            s.push(str(result))

    return s.peek()
        
if __name__ == "__main__":
    """
    >>> cal_postfix("6 5 2 3 + 8 * + 3 + *")
    288
    """
    result = cal_postfix("6 5 2 3 + 8 * + 3 + *")
    print(result)
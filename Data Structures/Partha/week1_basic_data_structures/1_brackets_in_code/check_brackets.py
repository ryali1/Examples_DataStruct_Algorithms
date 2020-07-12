# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):

    return (left + right) in ["()", "[]", "{}"]
    pass


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text, start=1):

        if next in "([{":
            opening_brackets_stack.append(next)
            # Process opening bracket, write your code here
            pass

        if next in ")]}":
            if not opening_brackets_stack:
                return i
                pass

            top = opening_brackets_stack.pop()

            if not are_matching(top,next):
                return i
                break
            # Process closing bracket, write your code here

    return "Success"












def main():
    text = input()
    #mismatch = find_mismatch(text)
    if len(text) == 1:
        print(1)
    else:
        mismatch = find_mismatch(text)

    print(mismatch)
    # Printing answer, write your code here


if __name__ == "__main__":
    main()

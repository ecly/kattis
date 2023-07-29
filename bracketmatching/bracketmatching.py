def is_valid(string):
    stack = []
    m = {"(":")","[":"]","{":"}"}
    for c in string:
        if c in m:
            stack.append(c)
        else:
            if not stack or c != m[stack[-1]]:
                return False

            stack.pop()

    return not stack

_ = int(input())
print("Valid" if is_valid(input()) else "Invalid")

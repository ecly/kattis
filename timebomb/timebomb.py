import sys

reference = """
***   * *** *** * * *** *** *** *** ***
* *   *   *   * * * *   *     * * * * *
* *   * *** *** *** *** ***   * *** ***
* *   * *     *   *   * * *   * * *   *
***   * *** ***   * *** ***   * *** ***
"""

def get_numbers(text):
    text = text.strip().split("\n")
    # we consider column to the left of start a space
    spaces = [-1]
    for i in range(len(text[0])):
        if all(text[j][i] == " " for j in range(len(text))):
           spaces.append(i)

    # we consider column to the right of end a space
    spaces.append(len(text[0]))

    ranges = [(x+1, y) for x, y in zip(spaces, spaces[1:]) if x != y-1]
    numbers = []
    for x, y in ranges:
        chars = ""
        for j in range(len(text)):
            for i in range(x, y):
                chars += text[j][i]

        numbers.append(chars)

    return numbers

ref_numbers = get_numbers(reference)
ref_map = {ref_numbers[i]: str(i) for i in range(10)}
nums = get_numbers(sys.stdin.read())

if any(n not in ref_map for n in nums):
    print("BOOM!!")
else:
    n = int("".join([ref_map[n] for n in nums]))
    print("BEER!!" if n % 6 == 0 else "BOOM!!")

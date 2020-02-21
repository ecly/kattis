import fileinput

VOWELS = "aeiouy"


def translate_word(word):
    if word[0] not in VOWELS:
        vowel_idx = next(idx for idx, c in enumerate(word) if c in VOWELS)
        return word[vowel_idx:] + word[:vowel_idx] + "ay"

    return word + "yay"


def main():
    for line in fileinput.input():
        print(" ".join(translate_word(word) for word in line.split()))


if __name__ == "__main__":
    main()

class Node:
    def __init__(self, n):
        self.value = n
        self.right = None
        self.left = None

    def insert(self, n):
        if n < self.value:
            if self.left is None:
                self.left = Node(n)
            else:
                self.left.insert(n)
        else:
            if self.right is None:
                self.right = Node(n)
            else:
                self.right.insert(n)

    def hash(self):
        if self.left is None and self.right is None:
            return "00"
        if self.left is None:
            return "01" + self.right.hash()
        if self.right is None:
            return "10" + self.left.hash()

        return "11" + self.left.hash() + self.right.hash()


def main():
    n, _k = map(int, input().split())
    shapes = set()
    for _ in range(n):
        numbers = list(map(int, input().split()))
        root = Node(numbers[0])
        for n in numbers[1:]:
            root.insert(n)

        shapes.add(root.hash())

    print(len(shapes))


if __name__ == "__main__":
    main()

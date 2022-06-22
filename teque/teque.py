import sys
from collections import deque

class Teque:
    def __init__(self):
        self.f = deque()
        self.b = deque()

    def _balance(self):
        if len(self) == 1 and len(self.b) == 0:
            return

        d = len(self.f) - len(self.b)
        if d > 1:
            self.b.appendleft(self.f.pop())
        if d <= -1:
            self.f.append(self.b.popleft())

    def push_back(self, v):
        self.b.append(v)
        self._balance()

    def push_front(self, v):
        self.f.appendleft(v)
        self._balance()

    def push_middle(self, v):
        self.f.append(v)
        self._balance()

    def __len__(self):
        return len(self.b) + len(self.f)

    def __str__(self):
        return ",".join(str(i) for i in self.f + self.b)

    def __getitem__(self, i):
        lf = len(self.f)
        if i < lf:
            return self.f[i]

        return self.b[i - lf]


def main():
    n = int(sys.stdin.readline())
    t = Teque()
    for _ in range(n):
        cmd, v = sys.stdin.readline().split()
        v = int(v)

        if cmd == "push_back":
            t.push_back(v)
        elif cmd == "push_front":
            t.push_front(v)
        elif cmd == "push_middle":
            t.push_middle(v)
        else:
            print(t[v])



if __name__ == "__main__":
    main()

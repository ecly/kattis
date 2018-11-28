package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func sumRange(n int) int {
	return ((n * (n + 1)) - (1 * (1 - 1))) / 2
}

func sumEveryOther(n int, start int) int {
	sum := 0
	for i := 0; i < n; i++ {
		sum += start + i*2
	}
	return sum
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Scan()
	for scanner.Scan() {
		words := strings.Fields(scanner.Text())
		k, _ := strconv.Atoi(words[0])
		n, _ := strconv.Atoi(words[1])
		s1 := sumRange(n)
		s2 := sumEveryOther(n, 1)
		s3 := sumEveryOther(n, 2)
		fmt.Printf("%d %d %d %d\n", k, s1, s2, s3)
	}
}

package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
)

func testCase(l1 []int, l2 []int) []int {
	n := len(l1)
	sorted1 := make([]int, len(l1))
	sorted2 := make([]int, len(l2))
	copy(sorted1, l1)
	copy(sorted2, l2)
	sort.Ints(sorted1)
	sort.Ints(sorted2)

	output := make([]int, n)
	for i, num := range l1 {
		idx := sort.SearchInts(sorted1, num)
		output[i] = sorted2[idx]
	}
	return output
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Scan()
	n, _ := strconv.Atoi(scanner.Text())
	for n > 0 {
		l1 := make([]int, n)
		l2 := make([]int, n)

		for i := 0; i < n; i++ {
			scanner.Scan()
			v, _ := strconv.Atoi(scanner.Text())
			l1[i] = v
		}

		for i := 0; i < n; i++ {
			scanner.Scan()
			v, _ := strconv.Atoi(scanner.Text())
			l2[i] = v
		}

		output := testCase(l1, l2)
		for _, num := range output {
			fmt.Println(num)
		}

		scanner.Scan()
		n, _ = strconv.Atoi(scanner.Text())
		if n != 0 {
			fmt.Println()
		}
	}
}

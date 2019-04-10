package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Scan()
	fields := strings.Fields(scanner.Text())
	n, _ := strconv.Atoi(fields[0])
	m, _ := strconv.Atoi(fields[0])
	for {
		if n == 0 && m == 0 {
			break
		}
		jack := make(map[int]bool, n)
		for i := 0; i < n; i++ {
			scanner.Scan()
			v, _ := strconv.Atoi(scanner.Text())
			jack[v] = true
		}

		count := 0
		for i := 0; i < m; i++ {
			scanner.Scan()
			v, _ := strconv.Atoi(scanner.Text())
			if _, ok := jack[v]; ok {
				count++
			}
		}
		fmt.Println(count)

		scanner.Scan()
		fields := strings.Fields(scanner.Text())
		n, _ = strconv.Atoi(fields[0])
		m, _ = strconv.Atoi(fields[0])
	}
}

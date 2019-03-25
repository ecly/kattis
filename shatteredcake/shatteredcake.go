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
	w, _ := strconv.Atoi(scanner.Text())
	scanner.Scan()
	n, _ := strconv.Atoi(scanner.Text())
	total := 0
	for i := 0; i < n; i++ {
		scanner.Scan()
		words := strings.Fields(scanner.Text())
		wi, _ := strconv.Atoi(words[0])
		li, _ := strconv.Atoi(words[1])
		total += wi * li
	}
	fmt.Printf("%d", total/w)
}

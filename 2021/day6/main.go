package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func stringToInt(word string) int {
	retInt, _ := strconv.ParseInt(word, 10, 64)
	return int(retInt)
}

func getStartData() []int {
	retList := []int{}
	file, err := os.Open("input_day_06")
	if err != nil {
		fmt.Println(err)
	}
	defer file.Close()

	valueString := ""

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		valueString = scanner.Text()
	}
	for _, character := range valueString {
		if string(character) == string(",") {
			continue
		}
		retList = append(retList, stringToInt(string(character)))
	}
	return retList
}

func decrementList(lst []int) []int {
	retList := []int{}
	for _, element := range lst {
		if element == 0 {
			retList = append(retList, 8)
			retList = append(retList, 6)
		} else {
			retList = append(retList, element-1)
		}
	}
	return retList
}

func updateCountedList(lst []int) []int {
	retList := []int{0, 0, 0, 0, 0, 0, 0, 0, 0}
	for i, ele := range lst {
		if i == 0 {
			retList[6] += ele
			retList[8] += ele
		} else {
			retList[i-1] += ele
		}
	}
	return retList
}

func solve_A() {
	data := getStartData()
	for i := 0; i < 80; i++ {
		data = decrementList(data)
	}
	fmt.Println("Number of fish after 80 days: ")
	fmt.Println(len(data))
}

func solve_B() {
	data := getStartData()
	groupedData := []int{0, 0, 0, 0, 0, 0, 0, 0, 0}
	for _, element := range data {
		groupedData[element] += 1
	}
	//	fmt.Println(groupedData)
	for i := 0; i < 256; i++ {
		groupedData = updateCountedList(groupedData)
	}
	ans := 0
	for _, element := range groupedData {
		ans += element
	}
	fmt.Println("Number of fish after 256 days: ")
	fmt.Println(ans)
}

func main() {
	solve_A()
	solve_B()

}

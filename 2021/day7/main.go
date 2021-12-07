package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
)

func stringToInt(word string) int {
	retInt, _ := strconv.ParseInt(word, 10, 64)
	return int(retInt)
}

func getStartData() []int {
	retList := []int{}
	file, err := os.Open("input_day_07")
	if err != nil {
		fmt.Println(err)
	}
	defer file.Close()

	valueString := ""

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		valueString = scanner.Text()
	}

	tempString := ""
	for _, character := range valueString {
		if string(character) == string(",") { // this line caused problems -> the last number is dropped
			retList = append(retList, stringToInt(tempString))
			tempString = ""
		} else {
			tempString += string(character)
		}
	}
	return retList
}

func get_fuel_used_at(data []int, point int) int {
	retInt := 0
	for _, ele := range data {
		if (point - ele) >= 0 {
			retInt += point - ele
		} else {
			retInt += ele - point
		}
	}
	return retInt
}

func additet(value int) int {
	if value == 1 {
		return value
	}
	return value + additet(value-1)
}

func get_prog_fuel_used_at(data []int, point int) int {
	retInt := 0
	for _, ele := range data {
		if (point - ele) > 0 {
			retInt += additet(point - ele)
		}
		if (point - ele) < 0 {
			retInt += additet(ele - point)
		}
	}
	return retInt
}

func get_mean(data []int) int {
	retInt := 0
	for _, ele := range data {
		retInt += ele
	}
	retInt = retInt / len(data)
	return retInt
}

func solve_A() {
	data := getStartData()
	sort.Ints(data)
	median := 0
	if len(data)%2 == 0 {
		median = (data[len(data)/2] + data[(len(data)/2)+1]) / 2
	} else {
		median = data[len(data)/2-1]
	}
	solution := get_fuel_used_at(data, median)
	fmt.Println(solution)
}

func solve_B() {
	// not happy with this solution
	data := getStartData()
	sort.Ints(data)
	mean := get_mean(data)
	solution := get_prog_fuel_used_at(data, mean)
	fmt.Println(solution)
}

func main() {
	solve_A()
	solve_B()
}

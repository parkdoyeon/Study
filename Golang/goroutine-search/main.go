package main

import (
	"bufio"
	"fmt"
	"os"
	"path/filepath"
	"strings"
)

type LineInfo struct {
	lineNo int
	line   string
}

type FindInfo struct {
	filename string
	lines    []LineInfo
}

func main() {
	fmt.Println("Args = ", os.Args)
	fileArg, query := os.Args[1], os.Args[2]

	filenames, err := getFileNames(fileArg)
	if err != nil {
		panic(err)
	}
	fmt.Println("Files = ", filenames)

	findInfos := gatherInfos(filenames, query)
	printResult(findInfos)
}

func gatherInfos(filenames []string, query string) []FindInfo {
	ch := make(chan FindInfo)
	for _, filename := range filenames {
		go search(filename, query, ch)
	}

	findInfos := []FindInfo{}
	cnt := 0
	for findInfo := range ch {
		findInfos = append(findInfos, findInfo)
		cnt++
		if cnt == len(filenames) {
			break
		}
	}
	close(ch)
	return findInfos
}

func getFileNames(fileArg string) ([]string, error) {
	return filepath.Glob("data/" + fileArg)
}

func printResult(findInfos []FindInfo) {
	for _, findInfo := range findInfos {
		fmt.Println(findInfo.filename)
		fmt.Println("------------------------------------------")
		for _, lineInfo := range findInfo.lines {
			fmt.Println("\t", lineInfo.lineNo, "\t", lineInfo.line)
		}
		fmt.Println("------------------------------------------")
	}
}

func search(filename string, query string, ch chan FindInfo) {
	file, err := os.Open(filename)
	if err != nil {
		panic(err)
	}

	findInfo := FindInfo{}
	scanner := bufio.NewScanner(file)
	lineNo := 0
	for scanner.Scan() {
		line := scanner.Text()
		if strings.Contains(line, query) {
			findInfo.lines = append(findInfo.lines, LineInfo{lineNo, line})
		}
		lineNo++
	}
	ch <- findInfo
	defer file.Close()
}

package main

import (
	"fmt"
	"os"

	argparse "github.com/akamensky/argparse"
)

func main() {
	parser := argparse.NewParser("hello", "Hello Something-er")
	s := parser.String("n", "name", &argparse.Options{Required: true, Help: "Who do you want to say hello to?"})
	if err := parser.Parse(os.Args); err != nil {
		fmt.Print(parser.Usage(err))
		return
	}
	fmt.Printf("Hello %s!\n", *s)
}

package main

import (
	"fmt"
	"os"

	argparse "github.com/akamensky/argparse"
	"github.com/hawkaa/experimenting/code/hello-world-go/internal"
)

func main() {
	parser := argparse.NewParser("hello", "Hello Something-er")
	s := parser.Float("s", "seed", &argparse.Options{Required: true, Help: "Seed number"})
	if err := parser.Parse(os.Args); err != nil {
		fmt.Print(parser.Usage(err))
		return
	}
	magic, err := internal.DoMagic(*s)
	if err != nil {
		fmt.Printf("%s\n", err)
		return
	}
	fmt.Printf("%v\n", magic)
	internal.PrintHello()
}

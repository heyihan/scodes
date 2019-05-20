package main

import (
    "fmt"
    "os"
    "github.com/heyihan/scodes/euler/go/mymath"
)

func main() {

    sum1 := mymath.SumOfSeries(3, 10)
    fmt.Println("sum ", sum1)


    os.Exit(0)
}

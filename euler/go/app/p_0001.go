package main

import (
    "fmt"
    "os"
    "github.com/heyihan/scodes/euler/go/mymath"
)

func main() {

    sum1 := mymath.SumOfSeries(3, 999)
    sum2 := mymath.SumOfSeries(5, 999)
    sum3 := mymath.SumOfSeries(3*5, 999)

    fmt.Printf("%d + %d - %d = %d\n", sum1, sum2, sum3, sum1+sum2-sum3)


    os.Exit(0)
}

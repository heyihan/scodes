package main

import (
    "fmt"
    "os"
    "github.com/heyihan/scodes/euler/go/mymath"
)

func main() {

    sum := uint(0)

    mymath.FibonacciScan(func(num uint) bool {
        fmt.Println(num)
        if num < 20 {
            sum += num
            return true
        }
        return false
    })

    fmt.Println("sum ", sum)

    os.Exit(0)
}

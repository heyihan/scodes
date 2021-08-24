package testgo

import(
    "fmt"
    "sort"
    "testing"
)

func TestSort(t *testing.T) {
    vals := []int{1,3,4,6,5,7,2,9}
    sort.Ints(vals)
    fmt.Println(vals)
}

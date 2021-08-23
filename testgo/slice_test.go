package testgo

import(
    "testing"
    "fmt"
)

//结论：
//1, v地址不变
//2, 修改v不会改变原始数据
func TestUpdateInFor(t *testing.T) {
    a := []int{1,2,3,4,5}

    for _, v := range a {
        v++
        j := v
        fmt.Println(&v, &j)
    }

    fmt.Println(a)
}

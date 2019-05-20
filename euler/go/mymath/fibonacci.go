package mymath

type ScanFunc func (num uint) bool

func FibonacciScan(f ScanFunc) {
    if !f(1) {
        return
    }

    if !f(2) {
        return 
    }

    var n1, n2 uint = 1, 2

    for {
        tmp := n1 + n2
        if !f(tmp) {
            break
        }

        n1, n2 = n2, tmp
    }
}

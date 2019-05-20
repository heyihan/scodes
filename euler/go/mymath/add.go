package mymath

func SumOfSeries(factor, max uint) uint {
    if factor == 0 {
        return 0
    }

    n := max / factor

    return factor * n * (1 + n) / 2
}

package practice_test

//pipeline测试
func inc(x: Array<Int64>): Array<Int64> { // Increasing the value of each element in the array by '1'
    let s = x.size
    var i = 0
    for (e in x where i < s) {
        x[i] = e + 1
        i++
    }
    x
}

func sum(y: Array<Int64>): Int64 { // Get the sum of elements in the array.
    var s = 0
    for (j in y) {
        s += j
    }
    s
}

let arr: Array<Int64> = Array<Int64>([1, 3, 5])
let res = arr |> inc |> sum // res = 12

//composition测试
//测试1
func f(x: Int64): Float64 {
    Float64(x)
}
func g(x: Float64): Float64 {
    x
}

var fg = f ~> g // The same as { x: Int64 => g(f(x)) }

//测试2
func fcom(x: Int64): Float64 {
    Float64(x)
}

let lambdaComp = ({x: Int64 => x}) ~> fcom // The same as { x: Int64 => f({x: Int64 => x}(x)) }



//测试3
func h1<T>(x: T): T { x }
func h2<T>(x: T): T { x }
var hh = h1<Int64> ~> h2<Int64> // The same as { x: Int64 => h2<Int64>(h1<Int64>(x)) }
package practice_test

//闭包测试
func returnAddNum(): (Int64) -> Int64 {
    let num: Int64 = 10

    func add(a: Int64): Int64 {
        return a + num
    }

    add
}

//变长参数测试
class Counter {
    var total = 0
    init(data: Array<Int64>) { total = data.size }
    operator func ()(data: Array<Int64>) { total += data.size }
}
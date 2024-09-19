package practice_test

import std.console.Console

main() {
    let num_array:Array<Int64> = [1, 0, 3, 0, 5, 6, 0, 0, 0, 10, 11, 0, 0, 0, 15, 0, 17, 18, 29, 0, 21, 22, 0, 0]
    println()
    println("双指针排序测试")
    doubleIndex(num_array)
    println("\nlambda表达式测试")
    lambdaTest1()
    lambdaTest2()
    println("\n闭包测试")
    println("returnAddNum()(10) = ${returnAddNum()(10)}")
    println("\n变长参数测试")
    let counter = Counter(1, 2)
    println(counter.total)
    counter(3, 4, 5)
    println(counter.total)
    println("\npipeline和composition测试")
    println("pipeline测试：")
    println("res = ${res}")
    println("\ncomposition测试：")
    println("fg = ${fg(3)}")
    println("lambdaComp = ${lambdaComp(4)}")
    println("hh = ${hh(12)}")
    println("操作符重载测试：")
    let p1 = Point(8, 24)
    let p2 = -p1
    let p3 = p1 + p2
    println("p1.x = ${p1.x}, p1.y = ${p1.y}")
    println("p2.x = ${p2.x}, p2.y = ${p2.y}")
    println("p3.x = ${p3.x}, p3.y = ${p3.y}")

    
    //程序结束时打印按任意键继续
    print("按任意键结束")
    var r = Console.stdIn.readln()
    return 0
}
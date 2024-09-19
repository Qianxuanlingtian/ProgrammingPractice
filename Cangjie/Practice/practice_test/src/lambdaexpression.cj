package practice_test

/*
lambda表达式形式：
{ p1: T1, ..., pn: Tn => expressions | declarations }
Lambda 表达式不管有没有参数，都不可以省略 =>，除非其作为尾随 lambda
*/
func lambdaTest1(): Unit {
    let display = { => println("Hello") }
    display()
    func f2(lam:() -> Unit): Unit {
        println("Now excute lam():")
        lam()
    }
    let f2Res = f2{ println("World") }
    f2Res
}

/*Lambda 表达式中参数的类型标注可缺省。以下情形中，若参数类型省略，编译器会尝试进行类型推断，当编译器无法推断出类型时会编译报错：
Lambda 表达式赋值给变量时，其参数类型根据变量类型推断；
Lambda 表达式作为函数调用表达式的实参使用时，其参数类型根据函数的形参类型推断。*/
func lambdaTest2(): Unit {
    // 后面lambda表达式的参数类型由变量sum1的类型进行推断
    let sum1: (Int64, Int64) -> Int64 = { a, b => a + b}
    let sum2: (Int64, Int64) -> Int64 = { a: Int64, b => a + b}

    func f(a1: (Int64) -> Int64): Int64 {
        a1(1)
    }

    println("sum1(2, 3) = ${sum1(2, 3)}")
    println("sum2(2, 3) = ${sum2(2, 3)}")
    println("f({a2 => a2 + 10}) = ${f({a2 => a2 + 10})}")
}

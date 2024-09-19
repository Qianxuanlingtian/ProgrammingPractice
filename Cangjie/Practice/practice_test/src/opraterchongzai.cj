package practice_test
//操作符重载
/*
- 实现对一个 Point 实例中两个成员变量 x 和 y 取负值，然后返回一个新的 Point 对象，
+ 实现对两个 Point 实例中两个成员变量 x 和 y 分别求和，然后返回一个新的 Point 对象。
*/
open class Point {
    var x: Int64 = 0
    var y: Int64 = 0
    public init(a: Int64, b: Int64) {
        x = a
        y = b
    }

    operator func -(): Point {
        Point(-x, -y)
    }

    operator func +(right: Point): Point {
        Point(this.x + right.x, this.x + right.x)
    }
}
package calculator

import std.console.Console

public class TempA {
    
}

main(): Int64 {
    var a = TempA(1, 2)
    println("a.getOriginXValue() = ${a.getOriginXValue()}")
    println("a.getOriginYValue() = ${a.getOriginYValue()}")
    println("a.getXValue() = ${a.getXValue()}")
    println("a.getYValue() = ${a.getYValue()}")
    a.setXValue(10)
    a.setYValue(12)
    println("a.getOriginXValue() = ${a.getOriginXValue()}")
    println("a.getOriginYValue() = ${a.getOriginYValue()}")
    println("a.getXValue() = ${a.getXValue()}")
    println("a.getYValue() = ${a.getYValue()}")

    for (i in 0..1000) {
        Console.stdOut.writeln("${i}: hello, world!")
    }
    Console.stdOut.flush()

    return 0
}
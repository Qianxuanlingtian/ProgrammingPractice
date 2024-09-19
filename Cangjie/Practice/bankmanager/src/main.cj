package bankmanager

import std.console.Console

main(): Int64 {
    let TXT = Console.stdIn.readln()

    println(TXT ?? "")

    Console.stdIn.readln()
    return 0
}
package helloworld

main(args: Array<String>): Unit {
    println("Hello World!")

    for (arg in args) {
        println(arg)
    }
}
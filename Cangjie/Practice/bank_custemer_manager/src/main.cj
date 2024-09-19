package bank_custemer_manager

import std.collection.HashMap
import std.console.Console
import std.console.ConsoleReader
import std.console.ConsoleWriter

let INPUT: ConsoleReader = Console.stdIn
let OUTPUT: ConsoleWriter = Console.stdOut

func menu(input: ConsoleReader): String {
    println("""
Please select menu(
1.Create new customer
2.Query customer if exsist
3.Query balance
4.Change balance
5.Change password
6.Delete customer
7.Exit system):
""")
    
    return input.readln().getOrThrow()
}

func addCustomer(cus_dict: HashMap<String, Customer>): Unit {
    var name: String
    var password: String
    var age: String
    var gender: String
    var balance: String
    var flag: String

    while (true) {
        OUTPUT.writeln("Please input customer's name:")
        name = INPUT.readln().getOrThrow()
        OUTPUT.writeln("Please input customer's password:")
        password = INPUT.readln().getOrThrow()
        OUTPUT.writeln("Please input customer's age:")
        age = INPUT.readln().getOrThrow()
        OUTPUT.writeln("Please input customer's gender:")
        gender = INPUT.readln().getOrThrow()
        OUTPUT.writeln("Please input customer's balance:")
        balance = INPUT.readln().getOrThrow()
        cus_dict.put(name, Customer(name, password, age, gender, balance))
        OUTPUT.writeln("Continue?(Y/N)")
        flag = INPUT.readln().getOrThrow()
        if (flag == "Y" || flag == "y") {
            continue
        }
        else if (flag == "N" || flag == "n") {
            break
        }
    }
}

func queryCustomer(cus_dict: HashMap<String, Customer>): Unit {
    var name: String
    OUTPUT.writeln("Please input name who you want to query:")
    name = INPUT.readln().getOrThrow()

    if (cus_dict.contains(name)) {
        OUTPUT.writeln("The customer exsist.")
    }
    else {
        OUTPUT.writeln("There is no ${name.toAsciiUpper()}")
    }
}

func queryCustomerBalance(cus_dict: HashMap<String, Customer>): Unit {
    while (true) {
        OUTPUT.writeln("Please input customer's name:")
        var name = INPUT.readln().getOrThrow()
        OUTPUT.writeln("Please input customer's password:")
        var password = INPUT.readln().getOrThrow()
        if (cus_dict.contains(name)) {
            while (true) {
                if (password == cus_dict[name].getPassword()) {
                    OUTPUT.writeln("${name.toAsciiUpper()}'s balance: ${cus_dict[name].getBalance()}")
                    break
                }
                else {
                    OUTPUT.write("The password is wrong, do you want to try again?(Y/N):")
                    var passwordretry = INPUT.readln().getOrThrow()
                    if (passwordretry == "Y" || passwordretry == "y") {
                        OUTPUT.writeln("Please input customer's password:")
                        password = INPUT.readln().getOrThrow()
                        continue
                    }
                    else {
                        break
                    }
                }
            }
        }
        else {
            OUTPUT.writeln("There's no ${name.toAsciiUpper()}")
        }
        OUTPUT.writeln("Continue query?(Y/N)")
        var conti_flag = INPUT.readln().getOrThrow()
        if (conti_flag == "Y" || conti_flag == "y") {
            continue
        }
        else {
            break
        }
    }
}

func changeCustomerBalance(cus_dict: HashMap<String, Customer>): Unit {
    while (true) {
        OUTPUT.writeln("Please input customer's name:")
        var name = INPUT.readln().getOrThrow()
        OUTPUT.writeln("Please input customer's password:")
        var password = INPUT.readln().getOrThrow()
        if (cus_dict.contains(name)) {
            while (true) {
                if (password == cus_dict[name].getPassword()) {
                    OUTPUT.writeln("Please input the new balance:")
                    var newbalance = INPUT.readln().getOrThrow()
                    cus_dict[name].setBalance(newbalance)
                    OUTPUT.writeln("${cus_dict[name].gerName()}'s new balance is ${cus_dict[name].getBalance()}")
                    break
                }
                else {
                    OUTPUT.write("The password is wrong, do you want to try again?(Y/N):")
                    var passwordretry = INPUT.readln().getOrThrow()
                    if (passwordretry == "Y" || passwordretry == "y") {
                        OUTPUT.writeln("Please input customer's password:")
                        password = INPUT.readln().getOrThrow()
                        continue
                    }
                    else {
                        break
                    }
                }
            }
        }
        else {
            OUTPUT.writeln("There's no ${name.toAsciiUpper()}")
        }
        OUTPUT.writeln("Continue?(Y/N)")
        var conti_flag = INPUT.readln().getOrThrow()
        if (conti_flag == "Y" || conti_flag == "y") {
            continue
        }
        else {
            break
        }
    }
}

main(): Int64 {
    var customer_dict = HashMap<String, Customer>()

    while (true) {
        var menu_select = menu(INPUT)
        match (menu_select) {
            case "1" => addCustomer(customer_dict)
            case "2" => queryCustomer(customer_dict)
            case "3" => queryCustomerBalance(customer_dict)
            case "4" => changeCustomerBalance(customer_dict)
            case "5" => println("5")
            case "6" => println("6")
            case "7" => println("7")
            break
            case _ => println("错误，请重新输入：")
            continue
        }
    }

    return 0
}
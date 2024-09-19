package breadth_first_algorithm
import std.collection.HashMap

main(): Int64 {
    let PHONEBOOK: HashMap<String, Array<String>> = HashMap<String, Array<String>>()
    PHONEBOOK['you'] = ["alice", "bob", "claire"]
    PHONEBOOK["bob"] = ["anuj", "peggy"]
    PHONEBOOK["alice"] = ["peggy"]
    PHONEBOOK["claire"] = ["thom", "jonny"]
    PHONEBOOK["anuj"] = []
    PHONEBOOK["peggy"] = []
    PHONEBOOK["thom"] = []
    PHONEBOOK["jonny"] = []

    println(PHONEBOOK)
    return 0
}
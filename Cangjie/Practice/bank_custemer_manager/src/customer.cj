package bank_custemer_manager

public class Customer {
    //用于更新记录用户的uid
    static var UID: Int64 = 100000
    public let USER_ID: Int64
    public let USER_NAME: String
    public var user_password: String
    public var user_age: String
    public let USER_GENDER: String
    public var user_balance: String

    public init(name: String, password: String, age: String, gender: String, balance: String) {
        UID++
        this.USER_ID = UID
        this.USER_NAME = name
        this.user_password = password
        this.user_age = age
        this.USER_GENDER = gender
        this.user_balance = balance
    }

    public func getID (): Int64 {
        return this.USER_ID
    }
    public func gerName (): String {
        return this.USER_NAME
    }
    public func getPassword (): String {
        return this.user_password
    }
    public func getAge (): String {
        return this.user_age
    }
    public func getGender (): String {
        return this.USER_GENDER
    }
    public func getBalance (): String {
        return this.user_balance
    }
    public func setPassword (ps: String): Unit {
        this.user_password = ps
    }
    public func setAge (age: String): Unit {
        this.user_age = age
    }
    public func setBalance (balance: String): Unit {
        this.user_balance = balance
    }
}


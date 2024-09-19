package lc04rob

import std.collection.{min, max}

class Solution {
    func rob(nums: Array<Int64>): Int64 {
        var money1 = 0
        var money2 = 0
        func otherInt(): Int64 {
            return 0
        }

        for (i in 0..nums.size:2) {
            money1 = money1 + nums[i]
            if (i + 1 < nums.size) {money2 = money2 + nums[i+1]}
        }
        
        return max([money1, money2]).getOrDefault(otherInt)
    }
}

main(): Int64 {
    let ARR = [2, 7, 9, 3, 1]
    println(Solution().rob(ARR))
    return 0
}
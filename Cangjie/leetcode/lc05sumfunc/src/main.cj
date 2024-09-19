package lc05sumfunc

class Solution {
    func arrSum(arr: Array<Int64>): Int64 {
        if (arr.size < 2) {
            return arr[0]
        }
        else {
            return arr[0] + arrSum(arr.slice(1, arr.size - 1))
        }
    }
}

main(): Int64 {
    println(Solution().arrSum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    return 0
}
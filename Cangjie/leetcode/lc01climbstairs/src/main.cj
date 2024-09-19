package lc01climbstairs
/*
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

 

示例 1：

输入：n = 2
输出：2
解释：有两种方法可以爬到楼顶。
1. 1 阶 + 1 阶
2. 2 阶
示例 2：

输入：n = 3
输出：3
解释：有三种方法可以爬到楼顶。
1. 1 阶 + 1 阶 + 1 阶
2. 1 阶 + 2 阶
3. 2 阶 + 1 阶

题解：https://leetcode.cn/problems/climbing-stairs/solutions/286022/pa-lou-ti-by-leetcode-solution
*/

class Solution {
    //递归recursion
    func climbStairsRecursion(n: Int64): Int64 {
        if (n == 1) {
            return 1
        }
        if (n == 2) {
            return 2
        }

        return climbStairsRecursion(n - 1) + climbStairsRecursion(n - 2)
    }

    //记忆性递归Memory recursion
    func climbStairsMemoryRecursion(n: Int64): Int64 {
        let MEMO = Array<Int64>(n + 1, item: 0)
        if (MEMO[n] > 0) {
            return MEMO[n]
        }
        if (n == 1) {
            MEMO[n] = 1
        }
        else if (n == 2) {
            MEMO[n] = 2
        }
        else {
            MEMO[n] = climbStairsMemoryRecursion(n - 1) + climbStairsMemoryRecursion(n - 2)
        }

        return MEMO[n]
    }

    //动态规划Dynamic programming
    func climbStairsDanamicProgramming(n: Int64): Int64 {
        let DP = Array<Int64>(n + 1, item: 0)
        DP[1] = 1
        DP[2] = 2

        if (n == 1) {
            return 1
        }
        for (i in Range(3, n, 1, true, true, true)) {
            DP[i] = DP[i - 1] + DP[i - 2]
        }

        return DP[n]
    }

    //斐波那契数列Fibonacci sequence
    func climbStairsFibonacciSequence(n: Int64): Int64 {
        var first = 1
        var second = 2
        var third = 0

        if (n == 1) {
            return 1
        }
        if (n == 2) {
            return 2
        }
        for (i in Range(3, n, 1, true, true, true)) {
            third = first + second  //滚动数组
            first = second
            second = third
        }

        return third
    }
}

main(): Int64 {
    println(Solution().climbStairsRecursion(20))
    println(Solution().climbStairsMemoryRecursion(20))
    println(Solution().climbStairsDanamicProgramming(20))
    println(Solution().climbStairsFibonacciSequence(20))
    return 0
}
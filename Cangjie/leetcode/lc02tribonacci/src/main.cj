package lc02tribonacci
/*泰波那契序列 Tn 定义如下： 

T0 = 0, T1 = 1, T2 = 1, 且在 n >= 0 的条件下 Tn+3 = Tn + Tn+1 + Tn+2

给你整数 n，请返回第 n 个泰波那契数 Tn 的值。

 

示例 1：

输入：n = 4
输出：4
解释：
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4
示例 2：

输入：n = 25
输出：1389537*/

class Solution {
    //动态规划
    func tribonacciDynamicProgramming(n: Int64): Int64 {
        var t0 = 0
        var t1 = 1
        var t2 = 1
        var t3 = 0
        if (n < 2) {
            return n
        }
        else if (n == 2) {
            return 1
        }
        else {
            for (_ in Range(3, n, 1, true, true, true)) {
                t3 = t0 + t1 + t2
                t0 = t1
                t1 = t2
                t2 = t3
            }
        }
        return t3
    }
    /*矩阵快速幂Matrix fast power
    https://leetcode.cn/problems/n-th-tribonacci-number/solutions/1/gong-shui-san-xie-yi-ti-si-jie-die-dai-d-m1ie*/
    func tribonacciMatrixFastPower(n: Int64): Int64 {
        let N: Int64 = 3
        if (n == 0) {
            return 0
        }
        if (n <= 2) {
            return 1
        }

        func multiply(a: Array<Array<Int64>>, b: Array<Array<Int64>>): Array<Array<Int64>> {
            //let M: Array<Array<Int64>> = Array<Array<Int64>>(N, item: Array<Int64>(N, item: 0))是有问题的，可考虑改用VArray
            //否则构造矩阵时，item是复用同一个引用的，所以应该用 Array<Int>(3, { _ => Array<Int64>(3, item: 9) }) lambda表达式动态赋值
            let M: Array<Array<Int64>> = Array<Array<Int64>>(N, {_ => Array<Int64>(N, item: 0)})
            for (i in Range(0, N, 1, true, true, false)) {
                for (j in Range(0, N, 1, true, true, false)) {
                    M[i][j] = a[i][0] * b[0][j] + a[i][1] * b[1][j] + a[i][2] * b[2][j]
                }
            }
            return M
        }
        
        func matrixPow(a: Array<Array<Int64>>, n: Int64): Array<Array<Int64>> {
            var p = a
            var num = n
            var ret: Array<Array<Int64>> = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

            while (num > 0) {
                if ((num & 1) == 1) {
                    ret = multiply(ret, p)
                }
                num >>= 1
                p = multiply(p, p)
            }

            return ret
        }

        let Q = [[1, 1, 1], [1, 0, 0], [0, 1, 0]]
        let RES = matrixPow(Q, n)
        return RES[0][2]
    }
}

main(): Int64 {
    println(Solution().tribonacciDynamicProgramming(20))
    println(Solution().tribonacciMatrixFastPower(20))
    return 0
}
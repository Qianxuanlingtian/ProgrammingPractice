package tibonacci

class Solution {
    func tibonacci(n: Int64): Int64 {
        let BASE = [[1, 1, 1], [1, 0, 0], [0, 1, 0]]
        func matrixMultiply(ma: Array<Array<Int64>>, mb: Array<Array<Int64>>): Array<Array<Int64>> {
            let ANS: Array<Array<Int64>> = Array<Array<Int64>>(3, {_ => Array<Int64>(3, item: 0)})
            for (i in 0..3) {
                for (j in 0..3) {
                    ANS[i][j] = ma[i][0] * mb[0][j] + ma[i][1] * mb[1][j] + ma[i][2] * mb[2][j]
                }
            }
            return ANS
        }

        func matrixPow(m: Array<Array<Int64>>, num: Int64): Int64 {
            var ret = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
            var n = num
            var temp = m
            while (n > 0) {
                if ((n & 1) == 1) {
                    ret = matrixMultiply(ret, m)
                }
                n >>= 1
                temp = matrixMultiply(temp, temp)
            }
            return ret[0][0]
        }

        return matrixPow(BASE, n)
    }
}

main(): Int64 {
    println(Solution().tibonacci(10))
    return 0
}
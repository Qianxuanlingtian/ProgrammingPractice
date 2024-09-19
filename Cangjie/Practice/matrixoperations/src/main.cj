package matrixoperations

class MatrixTwo {
    let ROW: Int64
    let COLUMN: Int64
    let MATRIX2: Array<Array<Int64>>
    MatrixTwo (m: Array<Array<Int64>>) {
        ROW = m.size
        COLUMN = m[0].size
        MATRIX2 = m
    }

    public func multiply(ma: Array<Array<Int64>>): Array<Array<Int64>> {
        let MULMATRIX: Array<Array<Int64>> = Array<Array<Int64>>(ROW, {_ => Array<Int64>(COLUMN, item:0)})
        if (this.COLUMN == ma.size) {
            for (i in 0..this.ROW:1) {
                for (j in 0..ma[0].size:1) {
                    for (k in 0..ma.size) {
                        MULMATRIX[i][j] += this.MATRIX2[i][k] * ma[k][j]
                    }
                }
            }
            return MULMATRIX
        }
        return [[]]
    }
}

main(): Int64 {
    let MARR1 = MatrixTwo([[1, 2, 3], [4, 5, 6]])
    let MARR2 = MatrixTwo([[3, 4], [6, 7], [1, 2]])

    println(MARR1.multiply(MARR2.MATRIX2))

    return 0
}
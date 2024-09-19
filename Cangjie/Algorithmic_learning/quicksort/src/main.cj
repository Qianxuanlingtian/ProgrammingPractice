package quicksort

import std.collection.ArrayList

extend ArrayList<Int64> {   //通过类型扩展实现对ArrayList类型数组的+拼接运算符重载
    operator func +(that: ArrayList<Int64>): ArrayList<Int64> {
        this.appendAll(that)
        return this
    }
}

class QuickSort {
    func qsort(list: Array<Int64>): ArrayList<Int64> {
        var less: ArrayList<Int64> = ArrayList<Int64>()
        var greater: ArrayList<Int64> = ArrayList<Int64>()
        let PIVOT: Int64 = list[0]
        if (list.size < 2) {
            return ArrayList(list)
        } else {
            for (i in list) {
                if (i < PIVOT) {
                    less.append(i)
                } else if (i > PIVOT) {
                    greater.append(i)
                }
            }

            return qsort(less.toArray()) + ArrayList(PIVOT) + qsort(greater.toArray())
        }
    }
}

main(): Int64 {
    println(QuickSort().qsort([4, 10, 3, 1, 7, 8, 3, 5, 3]))
    return 0
}

package practice_test

func doubleIndex(arr:Array<Int64>) {
    println("双指针排序前数组情况为：${arr}")

    for (right in 0..arr.size) {
        if (arr[right] != 0) {
            for (left in 0..right) {
                if (arr[left] == 0) {
                    arr[left] = arr[right]
                    arr[right] = 0
                }
            }
        }
    }
    println("双指针排序后数组情况为：${arr}")
}
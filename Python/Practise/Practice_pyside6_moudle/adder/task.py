from typing import Union

def add(a: Union[float, int], b: Union[float, int]):
    """
    计算两个数之和（取到小数点后两位）
    ：param a：第一个数
    ：param b：第二个数
    ：return：两数之和
    """

    return round(a + b, 2)
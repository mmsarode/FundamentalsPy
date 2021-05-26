import numpy as np
def reverseInt(x: np.int32) -> int:
    # 123 -> 321
    # -123 -> -321

    maxLimitBeforeOverflow = 2**31//10
    minLimitBeforeOverflow = (-2**31 - 1)//10

    xIn = x
    reversed32 = np.int32(0)
    sign = np.int32(1)

    while xIn:
        if reversed32 > maxLimitBeforeOverflow or reversed32 < minLimitBeforeOverflow:
            return 0
        if xIn < 0:
            xIn = -1 * xIn
            sign = -1
        reversed32 = reversed32 * 10 + xIn % 10
        xIn = xIn//10

    return sign * reversed32
    
    

    return sign * reversed32




num =  np.int32(-2**31)
print(num, reverseInt(num))

num =  np.int32(2**31 - 1)
print(num, reverseInt(num))

num =  np.int32(1234)
print(num, reverseInt(num))

num =  np.int32(-3251)
print(num, reverseInt(num))
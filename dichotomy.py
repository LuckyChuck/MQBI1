import math
const = 1e-10
def sqrt10():
    low,high = 3,4
    mid = (low+high)/2
    while high - low > const:
        if mid * mid > 10:
            high = mid
        else:
            low = mid
        mid = (low+high)/2
    return mid

print("二分法计算结果:"+ str(sqrt10()),"math函数计算结果："+str(math.sqrt(10)))
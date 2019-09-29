class Solution:
    def divide(self, dividend, divisor):
        sig = True if dividend*divisor > 0 else False  # 判断二者相除是正or负
        dividend, divisor= abs(dividend), abs(divisor)  # 将被除数和除数都变成正数
        res = 0                               # 用来表示减去了多少个除数，也就是商为多少
        while divisor <= dividend:              # 当被除数小于除数的时候终止循环
            tmp_divisor, count = divisor, 1     # 倍增除数初始化
            while tmp_divisor <= dividend:      # 当倍增后的除数大于被除数重新，变成最开始的除数
                dividend -= tmp_divisor
                res += count
                count += 1                      # 更新除数扩大的倍数
                tmp_divisor = divisor*count     # 更新除数
        res_value = res if sig == True else -res  # 给结果加上符号
        return max(min(res_value, 2**31-1), -2**31)
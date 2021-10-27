def reverse(x):
    num = 0
    if x == 0:
        return 0
    if x < 0:
        x =-x
        while x != 0:
            num = num*10 + x%10
            x = x/10
        num = -num
    if x>0:
        while x != 0:
            num = num*10 + x%10
            x = x//10 #整数除法//，python3后，数字的除法运算默认使用浮点数运算
            
            """
            学习python3遇到问题：
            今天在学习python时，想利用（121/100）得到的结果为整数 1，
            121/100
            outout:1.21
            但是实际结果是浮点数 1.21
            原因：python3后，数字的除法运算默认使用浮点数运算
            解决：将 / 运算符改为 // 即可
            """

    if num > pow(2,31)-1 or num < pow(2,-31):
        return 0
    return num

if __name__== '__main__':
    x = pow(2,32)
    y=reverse(x)
    print(y)
    
    """
    题目链接https://leetcode-cn.com/problems/reverse-integer/
    """
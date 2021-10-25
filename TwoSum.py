def twosum(nums,target):
    n=len(nums) #数组长度n
    for x in range(n) :  #x从0到n取值。不包括n
        a = target - nums[x] 
        if a in nums : #用in关键字查询nums列表中是否有a
            y = nums.index(a) #用index函数取得a的值在nums列表中的索引
            if x == y :#假如x=y,那么就跳过,否则返回x,y
                continue
            else:
                print(x,y)
                return x,y
                break
        else:
            continue

if __name__ == '__main__':
    twosum([1,2,3],4)


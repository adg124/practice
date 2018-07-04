class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]                
        """
        r = []
        
        for x in range(len(nums)):            
            for y in range(len(nums)):                
                if(x == y):
                    y = y + 1                    
                else:
                    if(nums[x] + nums[y] == target):
                        r = [x,y]                        
                        return r
                    else:
                        y = y + 1
            x = x + 1



def main():
    ret = Solution().twoSum([2, 7, 11, 15], 9)
    print(ret)

if __name__ == '__main__':
    main()
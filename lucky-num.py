def findLuckyNumber(nums):
    # implement this function
	# for x in nums:
	# 	if nums.count(x)==x:
	# 		return x
	# return -1
    lucky = {}
    for i in range(len(nums)):
        if nums[i] in lucky:
            lucky[nums[i]]+=1
        else:
            lucky[nums[i]] = 1
    
    for x in lucky:
        if int(x) == lucky[x]:
            return x
        return -1        

 

# DO NOT change anything below this line
if __name__ == "__main__":
    num_elems = int(input())
    input_arr = []
    for index in range(num_elems):
        input_arr.append(int(input()))
    
    print(findLuckyNumber(input_arr))
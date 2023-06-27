#this problem gives a list "nums", and an integer "target"
#it has to return the index's 2 numbers that his sum will be equal to the integer "target"
#for submitting just copy the code and paste it in leetcode inside of the method of the class "solution".
#you will have to erase the variable nums for its the argument on the method

nums = [3,2,4]

target = 6

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            print(i,j)



    
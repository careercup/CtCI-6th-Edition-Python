
#sorted list by height,weight respectively
#first element is larger than next element
#in simpler terms, trying to build the tower from bottom to up

#a = [(65,100),(70,150),(56,90),(75,190),(60,95),(68,110)]
a = [(65,100),(55,40),(75,90),(80,120)]
#sort on second dimension in decreasing order
a.sort(key= lambda x:-x[1])
#then, problem is lis in first dimension
dp = [float('inf') for _ in range(len(a))]
dp[0]= 1
max_so_far = 1
for i in range(1,len(a)):
    #look at the elements in the range [0,i-1] (does not include i)
    choices = [1]
    for j in range(0,i):
        if a[i][0]<a[j][0]:
            #then feasible candidate
            choices.append(1+ dp[j])
    dp[i] = max(choices)
    max_so_far = max(max_so_far,dp[i])
print(max_so_far)
print(dp)


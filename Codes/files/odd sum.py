def oddSum(n) :
    sum = 0
    curr = 1
    i = 0
    while i < n:
        sum = sum + curr
        curr = curr + 2
        i = i + 1
    return sum
 
# Driver Code
n = int(input("Enter number at which you want the sum: "))
print (" Sum of first" , n, "Odd Numbers is: ",
                                oddSum(n) )

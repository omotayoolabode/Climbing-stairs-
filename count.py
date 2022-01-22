# A program to count the number of ways to reach n'th stair
steps = int(input("Please enter the number of stairs"))
ways = int(input("Please enter the number of ways"))

def countWaysUtil(n, m):
    if n <= 1:
        return n
    res = 0
    i = 1
    while i<= m and i<= n: 
        res = res + countWaysUtil(n-i, m)
        i = i + 1
    return res
    
# Returns number of ways to reach s'th stair    
def countWays(steps, ways):
    return countWaysUtil(steps + 1, ways)

count = countWays(steps, ways)
print ("Number of ways = %d"  %count)


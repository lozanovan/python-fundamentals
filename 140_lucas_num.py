import functools
from datetime import datetime

#variable that holds each call of the recurssion
finish_time=datetime.now()-datetime.now()

def memory(f):
    memo = {}
    def helper(x):
        if x not in memo:            
            memo[x] = f(x)
        #print("Buffer in memory: ", memo[x])
        return memo[x]
    return helper

def timer(func):
    
    @functools.wraps(func)
    def time_closure(*args, **kwargs):
        global finish_time

        start = datetime.now()
        result = func(*args, **kwargs)
        buffer_time = datetime.now() - start
        finish_time += buffer_time
#       print(f"Time needed for the call: {buffer_time}")
        return result

    return time_closure

@memory
@timer
def lucas(num):

    if num==0:
        return 2
    if num==1:
        return 1
    result=lucas(num-1) + lucas(num-2)
    return (result)

n=input("Choose a number to calculate the Lucas one:")
#it takes about 37 seconds for n=35 without the memory decorator and 0:00:00.006920 seconds with it
result=lucas(int(n))

print(f"The {n}'th lucas number is: {result}")
print(f"Lucas function for n={n} passed for: {finish_time} seconds")
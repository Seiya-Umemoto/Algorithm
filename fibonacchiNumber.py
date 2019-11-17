# def fibonacchi(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return fibonacchi(n-1) + fibonacchi(n-2)
# n=100
# print(fibonacchi(n))

def fibonacchi(n):
    prev_prev = 1
    prev = 1
    count = 2
    while(2<=count<=n):
        new = prev + prev_prev
        prev_prev = prev
        prev = new
        count+=1
    return prev
n = 4
print(fibonacchi(n))

# 0 1 1 2 3 5 8 13 21 34
#User Input : Invalid
#1 ;l [0]
#2: [0,1]
#3: [0,1,1,2,3]
# num : local variable for get_fibonacci series 
def get_fibonacci_series(num):
    if (num<=0):
        print("Invalid Number. It should be positive number :")
        return False
    
    
    fibonacci_series =  [0,1]
    for i in range(num-2):
        next_item = fibonacci_series[-1] + fibonacci_series[-2]
        fibonacci_series.append(next_item)
    
    return fibonacci_series
    
    
import fibonacci

def main():
    print("Starting Main function ")
    number = int(input("Enter the length of number :"))
    
    
    
    series =  fibonacci.get_fibonacci_series(number)
    print(series)

main()
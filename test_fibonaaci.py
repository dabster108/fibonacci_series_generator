import unittest # built in module
import fibonacci
class TestFibonaaci(unittest.TestCase):
    def test_fibonacci_with_positive_input(self):  #case number 1 
        number = 10
        result = fibonacci.get_fibonacci_series(number)
        assert result  == [0,1,1,2,3,5,8,13,21,3 4]
        
        number = 5
        result = fibonacci.get_fibonacci_series(number)
        assert result  == [0,1,1,2,3]
        
        
    
    def test_fibonacci_with_negative_input(self):    #case number 2 
        pass
        
    
    def test_fibonacci_with_zero_input(self):       #case number 3
        number = 0 
        result = fibonacci.get_fibonacci_series(number)
        assert result == False
        
    
    def test_fibonacci_with_one_input(self):         #case number 4
        number = 1
        result = fibonacci.get_fibonacci_series(number)
        assert result == [0]
        
    
    def test_fibonacci_with_wrong_input_type(self):   #case number 5
        number = 0.1
        result = fibonacci.get_fibonacci_series(number)
        assert result == None 


unittest.main()

import src.task3 as task3
#checks if the function result is the same as positive, negative or 0
def test_check_number():
    assert task3.check_number(5) == "positive"
    assert task3.check_number(-1) == "negative"
    assert task3.check_number(0) == "zero"

def test_first_primes():
    #sends a lsit of numbers to find the first 10 primes
    assert task3.first_primes() == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

def test_sum_to_100():
    # makes sure 1 + 2 + 3 .... + 99 + 100 = 5050
    assert task3.sum_to_100() == 5050


from demo import add, subtract, multiply, divide

x = 1
y = 1

def test_add_should_return_correct_sum():
    sum = x + y
    assert add(x, y) == sum

def test_subtract_should_return_correct_difference():
    diff = x - y
    assert subtract(x, y) == diff

def test_multiply_should_return_correct_product():
    product = x * y
    assert multiply(x, y) == product

def test_divide_should_return_correct_quotient():
    quotient = x / y
    assert divide(x, y) == quotient

test_add_should_return_correct_sum()
test_subtract_should_return_correct_difference()
test_multiply_should_return_correct_product()
test_divide_should_return_correct_quotient()
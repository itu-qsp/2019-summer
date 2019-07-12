## define function (incrementor) with one argument (number) that returns a number (new_number)
## body: new_number is number plus 1

def incrementor(number):
    new_number = number + 1
    return new_number
    
print(incrementor(41))
print(incrementor(-23043480))
print(incrementor(41.999945))
print(incrementor(12/4))
print(incrementor(12//4))
print(incrementor(13//4))
print(incrementor(13/4))
# def func(p1,p2,*args,k,**kwargs):
#     print(f"positional- or -keywords:...{p1}, {p2}")
#     print(f"var-positional(*args):.......{args}")
#     print(f"keyword:.......................{k}")
#     print(f"var-keyword:....................{kwargs}")
#
# func(1,2,3,4,5,6,7,k=6,key1=7,key2=8)

def sum_numbers(*value:float) -> float:
    """ calculates the sum of all the numbers passed as arguments """

    result = 0
    for number in value:
        result = result + number
    return result


print(sum_numbers(1, 2, 3))
print(sum_numbers(8, 20, 2))
print(sum_numbers(12.5, 3.147, 98.1))
print(sum_numbers(1.1, 2.2, 5.5))
from ast import arg


def get_numbers():
    nums=[]
    product = 1.0
    print("Enter numbers and a random symbol to stop entering:")

    while True:
        buffer=input(':')

        if buffer.isdigit():
            nums.append(float(buffer))

        else:
            break

    return nums

def num_product(*args):
    result = 1.0
 
    for x in args[0]:
        result *= x
    return result

input=get_numbers()
result=num_product(input)


print(f"Product = {result}; number of parameters = {len(input)}")
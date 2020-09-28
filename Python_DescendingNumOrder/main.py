# Descending Order
# Your task is to make a function that can take any non-negative integer as an argument and return it with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.
# Examples:
# Input: 42145 Output: 54421
# Input: 145263 Output: 654321
# Input: 123456789 Output: 987654321

def descending_order(num):
    num_string = str(num)
    num_split = sorted(num_string, reverse = True)
#     print(num_split)
    new_num_string = ''.join(num_split)
#     print(new_num_string)
    output = int(new_num_string)
    print(output)
    return output

descending_order(119)
descending_order(819)
descending_order(90)
descending_order(8119)

# also written
def Descending_Order(num):
    return int("".join(sorted(str(num), reverse=True)))


def odd_index_sum(numbers_list):
    odd_numbers=0
    for number in range(len(numbers_list)):
        if number % 2 != 0:
            odd_numbers+=numbers_list[number]
    return odd_numbers


result=odd_index_sum([1,2,3,4,5,6,7,8,])
print(result)




# def odd_index_sum(numbers):
#     total = 0
#     for index in range(len(numbers)):
#         if index % 2 != 0:  # Check if index is odd
#             total += numbers[index]
#     return total
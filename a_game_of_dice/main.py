def binary_sum(first, second):

    # first_number_array = range(int(first))
    # second_number_array = range(int(second))
    # result = []

    # i = len(first_number_array) - 1
    # j = len(second_number_array) - 1
    # number_in_mind = 0

    # while i > 0:
    #     while j > 0:

    #         if i < 0:
    #             result_numeral = second_number_array[j] + number_in_mind

    #         if j < 0:
    #             result_numeral = first_number_array[i] + number_in_mind

    #         else:
    #             result_numeral = first_number_array[i] + second_number_array[j] + number_in_mind

    #         if result_numeral > 1:
    #             number_in_mind = result_numeral // 2
    #         result.append(result_numeral % 2)
    #         i -= 1
    #         j -= 1

    first_number = first[::]
    second_number = second[::]
    result = ''
    number_in_mind = 0
    index_in_first_number = len(first_number) - 1
    index_in_second_number = len(second_number) - 1

    while index_in_first_number >= 0 and index_in_second_number >= 0:
        result_numeral = int(first_number[index_in_first_number]) + int(second_number[index_in_second_number]) + number_in_mind

        result += str(result_numeral % 2)
        number_in_mind = result_numeral // 2

        index_in_first_number -= 1
        index_in_second_number -= 1




            

            
    print(result)


binary_sum('10', '11')
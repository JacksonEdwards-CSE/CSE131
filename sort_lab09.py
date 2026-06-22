# 1. Name:
#      Jackson Edwards
# 2. Assignment Name:
#      Lab 09 : Sub-List Sort Program
# 3. Assignment Description:
#      Sort a list using only one other list, moving items between the two while sorting sub-sets each time.
# 4. What was the hardest part? Be as specific as possible.
#      The hardest part was fixing my original pseudocode to actually sort the list.
#      It didn't actually move around the sub-set items, just moved the sub-sets back and forth.
# 5. How long did it take for you to complete the assignment?
#      2 hours

def sort_list(source_list):

    #Create a new destination list:
    destination_list = [0] * len(source_list)

    still_sorting = True

    while still_sorting:

        start_index = 0

        number_of_subsets = 1

        start_end_index_dict = {}

        #Create the sub-sets:
        for number in range(1, len(source_list)):

            if source_list[number] < source_list[number-1]:

                start_end_index_dict[number_of_subsets] = (start_index, number-1)

                number_of_subsets = number_of_subsets + 1

                start_index = number

        #Add sub-set start and end indexes to a dictionary:
        start_end_index_dict[number_of_subsets] = (start_index, len(source_list)-1)

        #Check if list is completely sorted:
        if number_of_subsets == 1:

            still_sorting = False

        #Run the sorting algorithm:
        else:

            destination_index = 0

            for subset in range(1, number_of_subsets + 1, 2):

                #If there is a subset leftover, copy over the rest of the items to the destination list:
                if subset == number_of_subsets:

                    start = start_end_index_dict[subset][0]
                    end = start_end_index_dict[subset][1]

                    for i in range(start, end + 1):
                        destination_list[destination_index] = source_list[i]
                        destination_index += 1

                #Sorting 2 sub-sets at a time:
                else:

                    left_index = start_end_index_dict[subset][0]
                    left_end = start_end_index_dict[subset][1]

                    right_index = start_end_index_dict[subset+1][0]
                    right_end = start_end_index_dict[subset+1][1]

                    while left_index <= left_end and right_index <= right_end:

                        if source_list[left_index] <= source_list[right_index]:

                            destination_list[destination_index] = source_list[left_index]

                            left_index += 1

                        else:

                            destination_list[destination_index] = source_list[right_index]

                            right_index += 1

                        destination_index += 1


                    #If one sub-set is shorter than the other, add the rest of the longer sub-set to the destination list:
                    while left_index <= left_end:

                        destination_list[destination_index] = source_list[left_index]

                        left_index += 1

                        destination_index += 1

                    while right_index <= right_end:

                        destination_list[destination_index] = source_list[right_index]

                        right_index += 1

                        destination_index += 1

            #Swap the source and destination list:
            source_list, destination_list = destination_list, source_list

    return source_list

def sort_list_tests():

    test_lists = [], [1], [1,2,3,4], [2,3,1,4], [3,8,5,9,6,4,1,7,2,10], [1,6,4,7,5,6,8,1], ["b","k","a","t","g","e","h","g","s"], [3, "apple", 1]

    for list in range(len(test_lists)):

        print(f"{list + 1}) {test_lists[list]}")
        try:
            sorted_list = sort_list(test_lists[list])
        
            print(sorted_list)
            input("Test Passed.\n")
        except TypeError:
            print(test_lists[list])
            print("Test Failed.\n")

def main():

    sort_list_tests()

if __name__ == "__main__":
    main()
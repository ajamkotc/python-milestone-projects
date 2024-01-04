class Sort:
    '''Sorting class containing various sorting methods.

    Methods
    -------
    merge_lists(list1, list2)
        Merges two lists
    merge_sort(unsorted_list)
        Sorts a list using the merge-sort algorithm'''

    @classmethod
    def merge_lists(cls, list1, list2):
        '''Merges two sorted lists into a sorted list.

        Params
        ------
        list1 : list
        list2 : list

        Returns
        -------
        return_list : list
            Sorted list containing list1 and list2'''

        return_list = []

        list1_index = list2_index = 0

        while list1_index < len(list1) and list2_index < len(list2):
            # Add items to return_list maintaining sort
            if list1[list1_index] <= list2[list2_index]:
                return_list.append(list1[list1_index])
                list1_index += 1
            else:
                return_list.append(list2[list2_index])
                list2_index += 1

        while list1_index < len(list1):
            # Add whatever items not added previously from list1
            return_list.append(list1[list1_index])
            list1_index += 1

        while list2_index < len(list2):
            # Add whatever items not added previously from list2
            return_list.append(list2[list2_index])
            list2_index += 1

        return return_list

    @classmethod
    def merge_sort(cls, unsorted_list):
        '''Sorts an unsorted list using the merge sort algorithm.

        Params
        ------
        unsorted_list : list

        Returns
        -------
        sorted_list : list'''

        sorted_list = []

        if len(unsorted_list) > 1:
            # Finds the midpoint of the list, rounded down
            list_midpoint = len(unsorted_list) // 2

            # Splits the list into two smaller lists
            left_half = unsorted_list[:list_midpoint]
            right_half = unsorted_list[list_midpoint:]

            # Recursively splits the list until get two lists each of length 1
            sorted_left = cls.merge_sort(left_half)
            sorted_right = cls.merge_sort(right_half)

            # Combine the two sorted lists
            sorted_list = cls.merge_lists(sorted_left, sorted_right)
        else:
            # Base case: list of length 1 is always sorted
            return unsorted_list

        return sorted_list

if __name__ == '__main__':
    print(Sort.merge_sort([5, 3, 9, 10, 1]))

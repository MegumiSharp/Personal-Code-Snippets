'''Binary search is an efficient algorithm for finding a specific value in a sorted array or list. The core idea is to repeatedly divide the search space in half until you find the target value or determine it doesn't exist. (When you're looking up a word in a physical dictionary, you don't start at page 1 and flip through every page. Instead, you naturally use the same strategy as binary search.)

1: Start with the entire sorted array and identify the middle element
2: Compare the target value with the middle element:
3: If they match, you've found the target
4: If the target is smaller, search the left half
5: If the target is larger, search the right half
6: Repeat the process on the chosen half until you find the target or the search space becomes empty

Example
Let's say you're searching for the number 7 in the sorted array: [1, 3, 5, 7, 9, 11, 13]

Let's search for 5 instead:
Step 1: Middle is 7. Since 5 < 7, search left half: [1, 3, 5]
Step 2: Middle is 3. Since 5 > 3, search right half: [5]
Step 3: Middle is 5. Found it!

Binary search has O(log n) time complexity, which makes it extremely efficient. This means that for an array of 1 million elements, you'd need at most about 20 comparisons to find any element. Compare this to linear search, which might need up to 1 million comparisons in the worst case.The algorithm requires the data to be sorted beforehand. If your data isn't sorted, you'd need to sort it first.
'''

# My implementation of the task
def binary_search(sorted_list, value):
    """
    Performs a binary search on a sorted list to find the given value.
    Parameters:
        sorted_list (list): The sorted list of elements to search.
        value (any): The value to search for in the list.
    Returns:
        int: The index of the value in the sorted list if found.
    Raises:
        ValueError: If the value is not found in the list.
    """

    high = len(sorted_list) - 1
    low = 0

    while low <= high:
        mid = (low + high) // 2

        if sorted_list[mid] == value:
            return mid
        elif sorted_list[mid] > value:
            high = mid - 1
        else:
            low = mid + 1

    raise ValueError("value not in array")


# This is not a binary search, but it give the same result, it is slower than binary search
def find(search_list, value):

    if value in search_list:
        return search_list.index(value)
    else:
        raise ValueError("value not in array")
    
# Given two string return true if the two strings are anagrams of each other

'''Sorting algorithms like Timsort in python have O(n log n) complexity, so this solution have O(n log n)'''
def isAnagram(s: str, t: str) -> bool:
    list_s = sorted(list(s))
    list_t = sorted(list(t))

    return list_s == list_t



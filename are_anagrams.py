def are_anagrams(str1, str2):
    """
    This function checks if two strings are anagrams of each other.

    Parameters:
    ----------
    str1 : str
        The first string to be compared.
    str2 : str
        The second string to be compared.

    Returns:
    -------
    bool:
        Returns True if the two strings are anagrams, otherwise False.

    Example:
    --------
    are_anagrams("listen", "silent")  # Output: True
    are_anagrams("hello", "world")    # Output: False
    """

    # Function implementation here ...
    str1= str1.lower()
    str2= str2.lower()
    if (sorted(str1) == sorted(str2)):
        output = True
    else:
        output = False

    return output
print(are_anagrams("listen","silent"))
print(are_anagrams("hello","world"))
## Example 
# print(are_anagrams("listen", "silent"))  # Expected output: True
# print(are_anagrams("hello", "world"))    # Expected output: False

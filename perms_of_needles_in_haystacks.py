'''
Find all the permutations of a needle from a haystack.
'''


def totalPermutations(needle, haystack):
    # base case
    if not needle or not haystack:
        return 0

    if len(needle) > len(haystack):
        # raise Error('Needle cannot be greater than haystack')
        return 0

    # lengths
    n, h = len(needle), len(haystack)

    # set of needle
    needle_set = set(needle)
    counts = {}

    # count how many times a character is present in needle
    for char in needle_set:
        counts[char] = needle.count(char)

    # output
    perms = []

    # Window Sliding:
    for i in range(h-n+1):
        new_needle = haystack[i:i+n]
        new_needle_set = set(new_needle)
        new_counts = {}
        for char in new_needle_set:
            new_counts[char] = new_needle.count(char)
        if new_counts == counts:
            perms.append(new_needle)

    return perms


print(totalPermutations(haystack='cbabcacabcaz', needle='abc'))
print(totalPermutations(haystack='', needle='abc'))
print(totalPermutations(haystack='cbabcacabcaz', needle=''))
print(totalPermutations(haystack='aaaaaaaaaaaaaaa', needle='abc'))
print(totalPermutations(haystack='aaaaaaaaaaaaa', needle='a'))
print(totalPermutations(haystack='aaaaaaaaaaaaa', needle='aaaaaaaaaaaaa'))
print(totalPermutations(haystack='aaaaaaaaaaaaa', needle='aaaaaaaaaaaaaaa'))

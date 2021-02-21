def find_needle_from_haystack(needle, haystack):
    if not needle or not haystack:
        return 'NO'
    n, h = len(needle), len(haystack)

    needle_set = set(needle)
    counts = {}

    for char in needle_set:
        counts[char] = needle.count(char)

    for i in range(h-n+1):
        new_needle = haystack[i:i+n]
        new_needle_set = set(new_needle)
        new_counts = {}

        for char in new_needle_set:
            new_counts[char] = new_needle.count[char]
            
        return 'YES'
    return 'NO'


t = int(input())
for _ in range(t):
    needle = str(input())
    haystack = str(input())
    print(find_needle_from_haystack(needle=needle, haystack=haystack))

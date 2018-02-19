# Given two strings s and t, t is a substring of s if t is contained as a
# contiguous collection of symbols in s (as a result, t must be no longer than s).
#
# The position of a symbol in a string is the total number of symbols found to
# its left, including itself (e.g., the positions of all occurrences of 'U' in
# "AUGCUUCAGAAAGGUCUUACG" are 2, 5, 6, 15, 17, and 18). The symbol at position i
# of s is denoted by s[i].
#
# A substring of scan be represented as s[j:k], where j and k represent the
# starting and ending positions of the substring in s; for example, if
# s = "AUGCUUCAGAAAGGUCUUACG", then s[2:5] = "UGCU".
#
# The location of a substring s[j:k] is its beginning position j; note that t
# will have multiple locations in s if it occurs more than once as a substring
# of s (see the Sample below).
#
# Given: Two DNA strings s and t (each of length at most 1 kbp).
#
# Return: All locations of t as a substring of s.
#
# Sample Dataset
# GATATATGCATATACTT
# ATAT
#
# Sample Output
# 2 4 10

s = 'GATATATGCATATACTT'
t = 'ATAT'

# iterate over the entire S.
# look for matches in t[0] through t[-1].
    # s[x] through s[y] must match t for len(t)
# if everything matches, save the index position of s that matched t[0]

def match_substrings(s, t):
    positions = []
    for i in range(len(s)):
        j = 0
        match = ''
        # if first letter matches keep checking sequence until match fails or match == t
        while i+j < len(s) and s[i+j] == t[j]:
            match += t[j]
            if match == t:
                positions.append(i+1)
                break
            j += 1

    print(*positions)

match_substrings(s, t)


s2 = 'GTTCTCTCATACCTCTCATACGTGTCTCTCATACCGCTCATACCTCATACCCTCATACGACTCATACTTCTCATACCCTCATACTATTCGTCTCATACTCCAGCTCATACACCTCATACGGGCTCATACTGGTGCTCATACTCTCATACCTACCTCATACGCTCATACGGCTCATACCTATCTCATACCCTCATACTCTCATACGTGTACTCATACACCTCATACGCCTCATACCTCATACTGAATCTCATACTCAACTCATACTCCTCATACAGATCTAACTCATACCTCATACCTCATACCCTCTCATACCGACCTAAGCTCATACTTTCCAACTCATACAGCGAGAGTCTCATACCTCATACGAAACTCATACCTCATACCTCTCATACGAAGTCTCATACCAACCTCATACCGTCTCATACGTGTCTCATACCTCATACCTCATACCCTCATACACTCATACCCTCATACCCTCATACCTCATACGCGTTCCTCATACGGGAAACTATCTCATACCTCATACCTCATACCCTCATACTCCTCATACTTCTCATACTGACTCATACGGGTCTCATACTCCTGAGATCTCATACAGCTCATACACTCATACTCTCATACGCTCATACCGTACCTCATACCTCATACCCTCATACTGCGATCTCTCATACCACTGCTCATACCCCTCATACGGAGCTCATACACCTCATACGAGTCTCATACAATCTCATACTGATCGAACTCATACAACTCATACGATAGGCTCATACTCGCCTCATACAGTAGCCCTCATACACTCATAC'
t2 = 'CTCATACCT'
match_substrings(s2, t2)


#### A better solution:

def match_substrings2(s, t):
    positions = []
    for i in range(len(s)):
        if s[i:].startswith(t):
            positions.append(i+1)

    print(*positions)

match_substrings2(s2, t2)
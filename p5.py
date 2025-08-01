#Given two strings s and t and, t is a substring of s
#  if t
#  is contained as a contiguous collection of symbols in s
#  (as a result, t
#  must be no longer than s
# ).

# The position of a symbol in a string is the total number of symbols found to its left, including itself (e.g., the positions of all occurrences of 'U' in "AUGCUUCAGAAAGGUCUUACG" are 2, 5, 6, 15, 17, and 18). The symbol at position i
#  of s
#  is denoted by s[i]
# .

# A substring of s
#  can be represented as s[j:k]
# , where j
#  and k
#  represent the starting and ending positions of the substring in s
# ; for example, if s
#  = "AUGCUUCAGAAAGGUCUUACG", then s[2:5]
#  = "UGCU".

# The location of a substring s[j:k]
#  is its beginning position j
# ; note that t
#  will have multiple locations in s
#  if it occurs more than once as a substring of s
#  (see the Sample below).

# Given: Two DNA strings s
#  and t
#  (each of length at most 1 kbp).

# Return: All locations of t
#  as a substring of s """
#############################
#Pseudocode#
# input s
# input t

# len(s) = s_len
# len(t) = t_len
# for i = 0: (s_len = t_len):
#         if s[i : i + t_len] = t
#         add (i+1) to position
#             go back into loop
##########################
#ask for input
s_input_string = input("Please enter a string of DNA (larger set): ")
t_input_string = input("Please enter a string of DNA (smaller set): ")
#get sizes and initialize
s_len = len(s_input_string)
t_len = len(t_input_string)
position_list = []
#check_match
for i in range(s_len - t_len + 1):
    if s_input_string[i : i + t_len] == t_input_string:
        position_list.append(i + 1)
result_space = " ".join([str(pos) for pos in position_list])
print(result_space)
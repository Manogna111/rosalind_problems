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

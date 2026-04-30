"""
Given 3 lists, a, b and c. Find out the numbers that occur exactly in 2 lists out of the 3.
Constraint: Cannot use loops and if statements
"""

def numbers_in_two_out_of_three_lists(a, b, c):
    set_a = set(a)
    set_b = set(b)
    set_c = set(c)

    a_and_b = set_a.intersection(set_b)         # Or, '&' operator can be used. E.g. set_a & set_b
    b_and_c = set_b.intersection(set_c)
    c_and_a = set_c.intersection(set_a)
    a_and_b_and_c = set_a & set_b & set_c

    # To get elements that are in either list but not both use the symmetric difference operator (^)
    # '-' operator is equivalent to the difference() function for sets
    return (a_and_b ^ b_and_c ^ c_and_a) - a_and_b_and_c

if __name__ == "__main__":
    list1 = [1, 2, 3, 4, 5, 6, 7]
    list2 = [4, 8, 13, 7, 14, 9]
    list3 = [10, 0, -1, 4, 5, 17, -23]
    print("Result: ", numbers_in_two_out_of_three_lists(list1, list2, list3))

def print_upper_words(str_list, must_start_with):
    
    """Converts any lowercase characters of a string to uppercase
    """

# Prints entire string as uppercase
#     upper_case = str.upper()

#     print(upper_case)


# print_upper_words('Mongolian Doggo')

    # if str.startswith('e') or str.startswith('E'):
    #     print(str.upper())
    # else:
    #     print('string does not start with an e')


# this should print "HELLO", "HEY", "YO", and "YES"

    for str in str_list:
        for char in must_start_with:
            if str.startswith(char):
                print(str)

print_upper_words(["hello", "hey", "goodbye", "yo", "yes"],
                   must_start_with={"h", "y"})
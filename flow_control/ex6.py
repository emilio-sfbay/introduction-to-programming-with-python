# Write a function that takes a string as an argument
# and returns an all-caps version of the string when the string is longer than 10 characters.
# Otherwise, it should return the original string.
# Example: change 'hello world' to 'HELLO WORLD', but don't change 'goodbye'.

def up_if_ten(a_string):
    if len(a_string) > 10:
        return a_string.upper()
    else:
        return a_string

print(up_if_ten('Joe Stevens'))

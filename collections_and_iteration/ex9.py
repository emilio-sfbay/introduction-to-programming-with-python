my_list = [1, 2, 3, [4, 5, 6]]
another_list = list(my_list)

# 1. Yes, they are equal. The values of both variables are identical.
# 2. No, they are not the same object. The list constructor function creates a new object.
# 3. Yes, they are equal. The values of both nested lists at index 3 are identical.
# 4. Yes, they are the same object. Using the list constructor creates a shallow copy.
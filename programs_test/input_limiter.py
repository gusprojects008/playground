def input_user_limit(limit_char):
    input_user = input()[:limit_char]
    return input_user

print("use ... ==>\n")
limit = 5
input_user = input_user_limit(5)
print(input_user)

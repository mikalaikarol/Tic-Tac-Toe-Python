user_input = input().split("_")
new_list = []

if len(user_input) == 1:
    word = "".join(user_input)
    print(word.capitalize())
if len(user_input) > 1:
    x = 0
    for cap in user_input:
        word = user_input[x].capitalize()
        x = x + 1
        new_list.append(word)

result = "".join(new_list)
print(result)

# other guys solution
# user_input = input()
#
# output = user_input.replace('_', ' ').title().replace(' ', '')
#
# print(output)

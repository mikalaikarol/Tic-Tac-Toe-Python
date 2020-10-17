# put your python code here
grades_list = input().split(" ")
count = 0

for i in grades_list:
    if i == "A":
        count += 1

x = float(count / len(grades_list))
print(round(x, 2))

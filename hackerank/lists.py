arr = []
n = int(input())

'''
insert i e
print
remove e
append e
sort
pop
reverse
'''

for i in range(n):
    str_input = input().split()
#    print(str_input)
    if str_input[0] == "insert":
        arr.insert(int(str_input[1]),int(str_input[2]))
    elif str_input[0] == "print":
        print(arr)
    elif str_input[0] == "remove":
        arr.remove(int(str_input[1]))
    elif str_input[0] == "append":
        arr.append(int(str_input[1]))
    elif str_input[0] == "sort":
        arr.sort()
    elif str_input[0] == "pop":
        arr.pop()
    elif str_input[0] == "reverse":
        arr.reverse()
    else:
        print("Enter valid input") 


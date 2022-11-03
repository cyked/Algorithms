if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
list1 = list([i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1))
#print(list1)

list2 = []
for i,j,k in list1:
    if (i+j+k) != n:
        list2.append([i,j,k])

print(list2)
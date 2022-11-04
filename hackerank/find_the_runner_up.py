if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
list1 = list(arr)
sorted_no_duplicates = sorted(set(list1))
print(sorted_no_duplicates[-2])


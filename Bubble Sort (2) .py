def swap(list1,s1,s2):
    list1[s1],list1[s2]=list1[s2],list1[s1]
def BubbleSort(list1):
    size = len(list1)
    for i in range (size):
        for j in range (size-i-1):
            if list1[j]>list1[j+1]:
                swap(list1,j,j+1)

A = [1,3,5,6,7,8,4,2]
BubbleSort(A)
print(A)
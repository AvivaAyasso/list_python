#1
array=[]
for i in range(5):
    x=input("enter number")
    array.append(x)
print(array,array[0:3])


#2
list=[1,2,3,4]
list.append(11)
print(list)


#3
list1=[1,3,4,5,6,5,5,9]
count=0
for i in list1:
    if i==5:
        count=count+1
print(count)


#4
list2=list1.copy()*2
print(list2)


#5
numlist=[1,2,7,4]
new=[]
for i in numlist:
    new.append(i)
print(new)


#6
aviva=[1,3,4,1,5,5,6]
for i in range(len(aviva)):
    for j in aviva:
        if aviva[i]==aviva[j]:
            print(i)

#7
list=[]
for i in range(6):
    x=int(input("enter number"))
    list.append(x)
print(list)


#8
e=[1,2,3,4,6,7,8,0,8]
print(len(e))

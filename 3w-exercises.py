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

#9
values = input("insirt a number : ")
list = values.split(",")
tuple = tuple(list)
print('List : ',list)
print('Tuple : ',tuple)

10
color_list = ["Red","Green","White" ,"Black"]
print( "%s %s"%(color_list[0],color_list[-1]))
 #10a
color_list = ["Red", "Green", "White", "Black"]
print((color_list[0], color_list[-1]))

#11
numbers = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958, 743, 527]


for x in numbers:
    if x == 237:
        print(x)
        break;
    elif x % 2 == 0:
        print(x)


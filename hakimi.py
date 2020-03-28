def hh_remove(list):
    i=0
    leng=len(list)
    list3=[]
    list1 =[]
for item in list:
    if item == 0 is False:
        list1.append(item)
list = list1
if list==[]:
    return True
    break
list2=sorted(list,reverse=True)   
n=list2.pop(0)
        # print(n)
        # print(list2)
if n>len(list2):
    return False
    break
else:
    list=  [j-1 for j in list2]
    print(list)
    return hh_remove(list)
        
 
    
list=[5, 3, 0, 2, 6, 2, 0, 7, 2, 5]
# print(list)
print(hh_remove(list))      
















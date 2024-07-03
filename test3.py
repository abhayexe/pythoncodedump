from array import *
a1=array('i',[4,5,7,1,2])
print('Array 1: ',a1)
c=a1[-3]
print('Third element form the last is: ',c)
a1.append(6)
print('After the append; ',a1)
a1.extend([4,5,1,9,12])
print('After the extend of one array to array 1: ',a1)
a1.insert(2,17)
print('After inserting 17 at 3rd (2) place', a1)
pp=a1.pop()
print('Array after pop: ',a1)
print('popped element is: ',pp)
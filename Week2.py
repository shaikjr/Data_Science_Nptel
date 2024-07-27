'''1)Which of the following object does not support indexing?
 tuple
 list
 dictionary
 set '''
 
 #ans
 #dictionary

'''2)Given a NumPy array, arr = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]]]), what is the output of the command, print(arr[0][1])?'''
import numpy as np
arr=np.array([[[1,2,3],[4,5,6],[7,8,9]]])
print(arr[0][1])

'''3)What is the output of the following code?'''
s={1,2,4,5}
l=[]

for i in range(len(s)):
    l+=[1+i]
print(l)

'''4)What is the output of the following code?'''
import numpy as np
arr1=np.array(np.arange(0,15))
print(arr1.reshape(3,5))

'''5)Which of the following code gives output My friend’s house is in Chennai?'''
place='chennai'
print("My friend's house is in {}".format(place))

'''6)Let t
1 = (1, 2, “tuple”, 4) and t
2 = (5, 6, 7). Which of the following will not give any error after the execution?
t1.append(5)

x=t2[t1[1]]

t3=t1+t2

t3=(t1,t2)

t3=(list(t1),list(t2))'''

t1=(1,2,"tuple",4) 
t2 = (5, 6, 7)
x=t2[t1[1]]
t3=t1+t2
t3=(t1,t2)
t3=(list(t1),list(t2))
print(t3)

'''7)Let d
 = {1 : “Pyhton”, 2 : [1, 2, 3]}. Which among the following will not give the error after the execution?

d[2].append(4)

x=d[0]

d[“one”]=1

d.update(‘one′:2)'''

d={1:"python",2:[1,2,3]}
d[2].append(4)
d['one']=1
print(x)

'''8)Which of the following data type is immutable?
 list
 set
 tuple
 dictionary'''
 
 #ans
 #set
 
'''9)student = {‘name’: ‘Jane’, ‘age’: 25, ‘courses’: [‘Math’, ‘Statistics’]}
Which among the following will return
{‘name’: ‘Jane’, ‘age’: 26, ‘courses’: [‘Math’, ‘Statistics’], ‘phone’: ‘123-456’}
 student.update({‘age’ : 26})
 student.update({‘age’ : 26, ‘phone’: ‘123-456’})
 student[‘phone’] = ‘123-456’
student.update({‘age’ : 26})
 None of the above'''
 
student = {'name': 'Jane', 'age': 25, 'courses': ['Math', 'Statistics']}
student['phone']='123-456'
student.update({'age':26})
student.update({'age':26,'phone':'123-456'})
print(student)

'''10)What is the output of the following code?'''
name="Mahesh"
l=[]
for i in name:
    l.append(i.capitalize())
print(l)
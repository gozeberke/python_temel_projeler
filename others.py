#identity operator : is
x=y=[1,2,3]
z=[1,2,3]
'''
print(x==y)
print(x==z)
print(x is y) # x ile y aynı adreste mi diye sorgular 
print(x is z)
'''
# membership operator : in
x=['apple', 'banana']
print('banana' in x) #dizisinin içinde banana bilgisi var mı ?
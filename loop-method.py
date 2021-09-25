#range
#1 den başla 10a kadar git
'''
for item in range(1,10):
    print(item)
'''
#2 den başla 2 şer 2 şer artarak 20 ye kadar git 
for m in range(2,20,2):
    print(m)

#döngünün dışında da kullanılabilir
#1 den başlayıp 10 a kadar 2 şer 2 şer artar bunun list çevririr ve ekrana yazdırır.
print(list(range(1,20,2)))    
#enumerate

greeting=('HELLO')
index=0
for letter in greeting:
    print(f'index: {index}   letter: {letter}')
    index +=1

greeting=('HELLO')

for index,letter in enumerate(greeting):
    print(f'index: {index}   letter: {letter}')
        

greeting=('HELLO')

for item in enumerate(greeting):
    print(item)

#zip

list1=[1,2,3,4,5] 
list2=['a','b','c','d','e']
print(list(zip(list1,list2)))   
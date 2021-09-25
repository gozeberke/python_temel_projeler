'''
name ='Berke Göze'
for i in name:
    if i =='G':
        break
    print(i)

name ='Berke Göze'
for i in name:
    if i =='G':
        continue
    print(i)    
'''
x = 1
toplam=0
while x <= 100:
    x+=1
    if x%2==0:
        continue
    toplam +=x

print(f'Çift sayıların toplam : {toplam}')    
        
   



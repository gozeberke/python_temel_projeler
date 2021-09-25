'''
sayilar=[1,3,5,7,9,12,19,21]
# sayilar listesini while ile ekrana yazdırma.
i=0
while (i< len(sayilar)):
    print(sayilar[i])
    i+=1 
'''
'''
#başlangıç ve bitiş değerlerini kullanıcıdan alıp aradaki tek sayıları yazdırma
x = int(input('Başlangıç: '))
y = int(input('Bitis: '))

i=x
while i < y:
    i+=1
    if (i%2==1):
        print(i)
'''
#kullanıcıdan alıcağınız 5 sayıyı ekrana sıralı bir şekilde yazdırın
numbers = []
i=0 
while i < 5:
    sayi = int(input('Bir sayi girin: '))
    numbers.append(sayi)
    i+=1   
numbers.sort()
print(numbers)

 
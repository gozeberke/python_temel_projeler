'''
#Gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonk.
def yazdir(kelime,adet):
    print(kelime*adet)

yazdir('Berke\n',2)    
'''
#Kendine gönderilen sınırsız sayıdaki parametreyi bir listeye çeviren fonksiyon
'''
def listeyeCevir(*args):
    liste=[]

    for arg in args:
        liste.append(arg)

    return liste

result=listeyeCevir(10,20,30,'Berke')
print(result)
'''
# Gönderilen 2 sayı arasındaki tüm sayıları bulun
'''
def asalMi(a,b):
    for sayi in range(a,b+1):
        if sayi > 1:
            for i in range(2,sayi):
                if(sayi%i==0):
                    break

            else:
                print(sayi)    
        
asalMi(20,40)        
'''
#Kendisine gönderilen sayının tam bölenlerini nulan fonksiyon
def tamBolen(sayi):
    tamBolenler=[]
    for i in range(2,sayi):
        if(sayi%i==0):
            tamBolenler.append(i)
    return tamBolenler


print(tamBolen(30))    


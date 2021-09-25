names=['Berke','Yağmur','Efe','Deniz']
years=[1998,2000,1998,1987]

names.append('Cenk')
names.insert(0,'Sena')
#names.remove('deniz')
names.count('Deniz')
index=names.index('Deniz')
result='Ali' in names #names dizisinde ali var mı 
names.reverse()
names.sort()
years.sort()
min=min(years)
max=max(years)
print(years)
print(min)
print(max)
print(years.count(1998))
years.clear()
markalar=[]
marka=input("Marka giriniz: ")
markalar.append(marka)
print(marka)

#print(result)
#print(index)
#print(names)
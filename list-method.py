numbers=[1,10,16,4,9,10]
letters=['a','g','s','b','y','a','s']
val=min(numbers)
val=max(numbers)
val=min(letters)
val=max(letters)
val=numbers[:3]
numbers[4]=39
numbers.append(49)#eleman ekleme
numbers.insert(3,78)#3. indeksin yerine 78 rakamını ekler 3. indeksi sağa kayar
numbers.insert(-1,52)#en son sayıdan bi önce 52 ekler
numbers.pop()#en son sayı silinir. parametre verirsek ordaki sayı silinir.
numbers.remove(10)#59 siler
numbers.sort()#sayısal büyüklük olarak sıralanır.
letters.sort()#alfabetik olarak sıralar.
numbers.reverse()#tersten yazar
print(len(numbers))#kaç eleman olduğunu görüyoruz 
print(numbers.count(10))#10 kaç tane var ?
print(letters.count('a'))#a kaç tane var ?
numbers.clear()#bütün elemanları siler
print(numbers)
print(val)
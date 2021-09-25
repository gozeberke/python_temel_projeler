
'''
message=message.upper() #harfleri büyük yapar.
message=message.lower()#harfleri küçük yapar.
message=message.title()#her kelimenin baş harfi büyük harfe çevrilir.
message=message.capitalize()#İlk kelimenin ilk harfi büyük olur diğerleri küçük olur.
message=message.strip()#eğer kulanıcı ilk kelimeden önce boşluk kullandıysa onu siler.
message=message.split()#içine parametre göndermezsek cümleyi parçalara ayırır boşluklardan başlayarak
message= ' '.join(message)#cümle parçalanmışsa eski haline getirir.
index=message.find('Berke')#cümlede ararma yapmak için negarif gelirse index o kelimenin olmadığını gösterir.
isFound=message.startswith('H')#cümlenin H harfi ilie başlayıp başlamadığını öğreniriz.
isFound=message.endswith('n')#cümelenin son harfi n mi ona bakar
message=message.replace('Berke','İsmail Berke')#cümlede Berke yerine İsmial Berke yazar.
message=message.center(100)#stringleri ortalamak için
print(isFound)

print(index)

print(message)
'''

# coding: utf-8

# In[ ]:


'''
Напишите программу, которая считывает текст из файла (в файле может быть больше одной строки) 
и выводит самое частое слово в этом тексте и через пробел то, сколько раз оно встретилось. 
Если таких слов несколько, вывести лексикографически первое (можно использовать оператор < для строк).
Слова, написанные в разных регистрах, считаются одинаковыми.
'''

lst=[]
slov={}
with open('path_to_file','r') as f:
    for string in f.readlines():
        string=string.lower()
        string=string.split()
        for word in string:
            
            if word not in slov:
                slov[word]=1
            else:
                slov[word]+=1
                
        for key,value in slov.items():#создаем список из пар (значение ключ)
            lst.append((value,key))
    
    print(max(lst))#находим наибольшее значение в этом списке
    


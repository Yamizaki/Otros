import os
from re import A 
cap= os.getcwd()

cat=(os.listdir())
lsitavacia=[]
print("*****Estas son todas las categorias:*****")
for i in cat:
    if not i.endswith(".py"):
        print(i)
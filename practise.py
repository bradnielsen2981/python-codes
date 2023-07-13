# python list
fruitbasket = ['apple','banana','cherry','mango']
print(fruitbasket[0]) #indice

print(len(fruitbasket))

fruitbasket.append("watermelon")
fruitbasket.remove("cherry")

for fruit in fruitbasket:
    print(fruit)

for i in range(len(fruitbasket)):
    print(i)
    print(fruitbasket[i])

#----------------------------------------------------

# python dictionary practice
fruitdict = {'apple':10, 'banana':3, 'watermelon':1}
#keys   #values

print(fruitdict['apple'])
print(fruitdict['banana'])

print(fruitdict.keys()) #returned a list of keys
print(fruitdict.values()) #returned a list of values

fruitdict['coconut'] = 100  #creates a key

for item in fruitdict:      #cycles through the keys
    print(item)
    print(fruitdict[item])

for value in fruitdict.values():
    print(value)

del fruitdict['apple'] #delets a key

fruitdict['alist'] = [1,2,3] # a list inside a dictionary
print(fruitdict['alist']) 
alist = [fruitdict, fruitdict, fruitdict] #A list of diction
print(alist[0])

#CREATE TWO DIFFERENT DICTIONARIES REPRESENTS A POKEMON
pikachu = {"name":"pikachu", "poketype":['electric'], "hp":[20] }
charizard = {"name":"charizard", "poketype":['flying','fire'], "hp":[340] }

#CREATE A LIST CONTAIN THE TWO POKEMON
pokelist = [pikachu,charizard]

#RANDOMLY CHOOSE ONE OF THOSE POKEMON TO PRINT OUT OF THE 
import random
num = random.randint(0,1)
print(pokelist[num])
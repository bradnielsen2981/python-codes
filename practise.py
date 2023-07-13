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

fruitdict['coconut'] = 100

for item in fruitdict:      #cycles through the keys
    print(item)
    print(fruitdict[item])

for value in fruitdict.values():
    print(value)

del fruitdict['apple']
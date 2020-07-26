"""
Advance data type - Lists,tulpe,dict,set
"""
#list
names=["Max","Nina","Rosy"]
print(names)

#length of a list
len(names)

#list index starting from 0
print(names[0])

#to update a member of the list
names[1]="Polina"

#sorting inside list
lottery=[23,121,34,212]
print(sorted(lottery)) #sorted inc
print(lottery) #original list unchanged
print(sorted(lottery, reverse=True)) #sorted desc

#second of sorting list
#this method permanent
lottery.sort
lottery.reverse

#to extend list .append, .insert(pos,value)
# and combining two list firstlist.extend(secondlist)

#lookup in list this is SLOW
23 in lottery

#count method of list
lottery.count(23)

#other method of list remove,pop
from linked_list import LinkedList

list = LinkedList()

names = ['John', 'Diane', 'Mike', 'Lisa', 'Mae', 'Luca']

for i in names : 
	list.add(i)


print list.get('Luca')

'''
	Written-by : John Mezzanotte
	LinkedList Implementation. Last piece is we need some sort of iteration
'''

class LinkedList:

	# Nested node class 
	class Node:

		def __init__(self, data, next):
			self.data = data
			self.next = next


		def __str__(self):
			return 'data:{data}'.format(data=self.data)


	def __init__(self):
		self.head = None
		self.tail = None
		self.items = 0


	def add(self, data):

		# setup your new node
		new_node = self.Node(data, None)

		if self.is_empty() : 
			self.head = new_node
			self.tail = new_node
			self.items += 1
		else:
			new_node.next = self.head
			self.head = new_node
			self.items += 1

	def remove_first(self):

		# remove first is O(1)
		if not self.is_empty():
			self.head = self.head.next
			self.items -= 1

	def remove_last(self):
		
		cursor = self.head 

		if self.size() >= 2 :
			while cursor.next.next is not None:
				cursor = cursor.next 

			cursor.next = None
			self.tail = cursor
			self.items -= 1 
		else :
			self.tail = None
			self.head = None
			self.items -= 1


	def is_empty(self):
		return self.head == None

	def get_head(self):
		
		if not self.is_empty():
			
			return self.head.data
		
		return None

	def get_tail(self):
		
		if not self.is_empty():
			return self.tail.data

		return None

	def size(self):
		return self.items

	def __str__(self):

		answer = '[ '
		cursor = self.head

		while cursor is not None:
			answer += cursor.data + ' ]-->[ '  
			cursor = cursor.next

		return answer


if __name__ == '__main__':


	list = LinkedList()
	list.add('John')
	list.add('Joe')
	list.add('Jill')

	print list

	list.remove_last()
	print list
	list.remove_first()
	print list
	print list.get_tail()
	print list.get_head()
	list.remove_last()
	print list.size()
	print list.get_tail()
	print list.get_head()




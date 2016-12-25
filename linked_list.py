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

	# Is there a way we can make this remove method take care of remove last, or first

	def remove(self, last=False):
		# remove first is O(1), this will remove the first item from the list

		if not self.is_empty():
			if last:
				self.remove_last()
			else:
				self.head = self.head.next
				self.items -= 1


	def remove_last(self):

		'''helper method to remove last node of linked list'''

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


	def get(self, item):

		if not self.is_empty():
			cursor = self.head
			while cursor is not None:
				if cursor.data == item:
					return item
				cursor = cursor.next

			return None


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

	def __iter__(self):
		return LinkedListIterator(self.head)
	


class LinkedListIterator:

	''' takes a head node reference '''

	def __init__(self, head):
		self.head = head	

	def __iter__(self):
		return self

	def next(self):
		if self.head is None:
			raise StopIteration
		else:
			cursor = self.head
			self.head = self.head.next
			return cursor




if __name__ == '__main__':


	list = LinkedList()
	list.add('John')
	list.add('Joe')
	list.add('Jill')
	list.add('Johnny')

	list.remove_last()
	
	for i in list:
		print i.data






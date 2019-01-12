from abc import ABCMeta, abstractmethod

class Book(object, metaclass=ABCMeta):
    def __init__(self,title,author):
        self.title=title
        self.author=author 

    @abstractmethod
    def display(): pass

#Write MyBook class

class MyBook(Book):
	"""docstring for MyBook"""
	def __init__(self, title,author,price):
		Book.__init__(self,title, author)
		self.price = price
	
	def display(self):
		print("Title:",self.title)
		print("Author:",self.author)
		print("Price:",self.price)

title=input()
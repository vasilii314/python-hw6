class Animal:
	def voice():
		pass

class Cat(Animal):
	def voice(self):
		print("Meow-meow")

class Dog(Animal):
	def voice(self):
		print("Woof-woof")

class Bird(Animal):
	def voice(self):
		print("Tweet-tweet")

cat = Cat()
dog = Dog()
bird = Bird()

cat.voice()
dog.voice()
bird.voice()
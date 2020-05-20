# Python - Advanced Topics
* probably not that advanced at all for experienced python developers


## Scope

```
x = "This is X"

def printX():
	print(x)

# X is printed
```
#### Sequence

1. **Local**
2. **Global**
3. **Bult-in**
4. **Enclosed**

## OOP

Every in python is an object.
A class defines the nature of an object.
Attributes - Characteristic
Method - Operations

#### OOP - Magic Methods

* **Default**
```


class Sample():


	def __init__(self):
		pass


x = Sample()
print(type(x))
# prints class '__main__.Sample'
# that's the standard string representation of the class


print(len(x))
# TypeError -> object of type'Sample' has no len()
# As default an instance has no length

```
 * **Modifing**
```
class Sample():
	def __init__(self):
	pass
	def __str__(self):
	return "Message returned when printed"
	def __len__(self):
	return 42
	def __del__(self):
		print("This message is printed by deletion 'del instance_of_sample'")

x = Sample()
print(x) #return the new string representation defined by __str__
print(len(x)) #return the new length representation defined by __int__
del x #prints message
```


## RegEx

```
import re

text = 'I'm trying to find this word1'
match = re.search('word1', text)
match.start() #return 6... position of the word's start


re.findall('1', '1010101010101') 
#returns ['1', '1', '1', '1', '1', '1', '1']


re.findall('ala*', 'ala, la, la, la, ala, al, al, allalalala, la')
# returns ['ala', 'ala', 'al', 'al', 'al', 'ala', 'ala']

re.findall('a[al]+', 'ala, la, la, la, ala, al, al, allalalala, la, laaaa, lll')
# if one or more a, or one or more al
# returns ['ala', 'ala', 'al', 'al', 'allalalala', 'aaaa']


re.findall('[^!.?]+', 'Atention! Thats what I said. Did you hear it?')
# ^ stands for remove the sign.
# returns ['Atention', ' Thats what I said', ' Did you hear it']

re.findall('[A-Z] ','')

```


## Decorators

The decorator wraps the inner function and modify it's behaviour.

#### Defining a decorator
```
def new_decorator(func):
	def wrap_func():
	print("CODE HERE BEFORE EXECUTING FUNC")
	func()
	print("FUNC() HAS BEEN CALLED")

	return wrap_func
```

#### Applying the decorator
```
def func_needs_decorator():
	print("This function is in need of a decorator!")


func_needs_decorator = new_decorator(func_needs_decorator)
func_needs_decorator()
```
**is the same as**
```
@new_decorator
def func_needs_decorator():
	print("This function is in need of a decorator")
```
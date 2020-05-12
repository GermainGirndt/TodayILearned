# Efficient Programming

## 1. Reducing unnecessary ifs (12/05/2020)

#### Before:

````
input = "I like to eat apples"

def check_if_apple_in_input(input):
	if "apple" in input.lower():
		return True
	return False
````

#### After:

````
input = "I like to eat apples"

def check_if_apple_in_input(input):
	return "apple" in input.lower()
````

#### Takeaway:
* Remember that "<VALUE> in <VARIABLE>" expressions already return a boolean.


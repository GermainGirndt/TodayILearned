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


## 2. Rejoining splits

Capitalizing every word of a sentence

#### Before:
```
def to_jaden_case(string):
    list_capitalized = [s.capitalize() for s in string.split()]
    return " ".join(list_capitalized)
```
#### After:
```
def to_jaden_case(string):        
    return " ".join(w.capitalize() for w in string.split())
#using generator
```

## 3. Calling dictionaries directly

#### Before:
```
def get_planet_name(id):
    dict = {1: "Mercury",
            2: "Venus",
            3: "Earth",
            4: "Mars",
            5: "Jupiter",
            6: "Saturn",
            7: "Uranus", 
            8: "Neptune"
            }
    return dict[id]
```

#### After:
```
def get_planet_name(id):
    return {
        1: "Mercury",
        2: "Venus",
        3: "Earth",
        4: "Mars",
        5: "Jupiter",
        6: "Saturn",
        7: "Uranus",
        8: "Neptune",
    }.get(id, None)
```



## 4. Using a generator

If fn returns true, find_in_array muss return True
If none of the iterations return True, muss return -1

#### Before:
```
def find_in_array(seq, fn): 
	for index, e in enumerate(seq):
	    if fn(e, index):
	        return index
	return -1
```
#### After:
```
def find_in_array(seq, fn): 
    return next((i for i, e in enumerate(seq) if fn(index, i)), -1)
```



---

## 

#### Before:
```

```
#### After:
```

```
## Generating Infinite Numbers

* **Infinite generator**
```

def infinite_gen():
    x = 0
    while 1:
        yield x
        x += 1


for n in infinite_gen():
    print(n)


```
* **Alternatively**

```
def infinite_gen():
    x = 0
    while True:
        yield x
        x += 1


my_gen = infinite_gen()

for n in my_gen:
    print(n)

```
# Iterating over generators

* **Iterating over a generator object**
```
gen = (x * x * x for x in range(1000))

print(gen)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
```

* **Iterating over a generator function**
```


def infinite_gen():
    x = 0
    while 1:
        yield x
        x += 1


gen = infinite_gen()

print(gen)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
```

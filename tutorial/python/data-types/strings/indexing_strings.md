<!-- @format -->

# Indexing Strings

Every character in a string has a particular index. Generally, in programming, indexing starts from 0 i.e. the first item in the string will be 0, the second item will have an **index of _1_**, the third, an **index of _2_** and so on

So now that we know that, how do we get the items of the strings with their index?
Well, we use the square bracket notation

```python
name = "Kingsley"

#Recall that the first item (K) has an index of 0

print(name[0])
#Output: K

print(name[1])
#Output: i

print(name[2])
#Output: n

print(name[7])
#Output: y
```

You should however note that if we try to get an index that doesn't exist, we get an index error

```python
greet_message = "Hello"

print(greet_message[10])
#Output: IndexError

```

### Negative Indexing

---

Negative indexing actually means accessing items from the back. The last item has the **index of _-1_**

```python
greeting = "hello user"

print(greeting[-1])
#output: r

print(greeting[-2])
#output: e

print(greeting[-3])
#output: s
```

### Grouped Indexing (Slicing)

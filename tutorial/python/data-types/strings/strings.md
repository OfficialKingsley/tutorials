<!-- @format -->

# Introduction to strings

Strings are basically anything withing quotes single ( 'This is a string' ) or double(" This is a string in double quotes ")

```python
print("Hi, how are you")
# Output: Hi, how are you
```

If you want the "how are you" to be on a new line,

```python
print("Hi, \nhow are you")
# Output:
# Hi,
# how are you
```

The \n is an example of a special character (which actually means "new line")

One thing to also note is that, when using single quotes for your code, do not add single quotes in between if not the string will end at that point

```python
print('He's Wrong') '

# You'll notice that the highlight for the string
# Stopped after "He"
#To avoid this, we can escape the single quote using a backslash or we use double quotes
```

```python
print("He's wrong")
# OR
print('He\'s wrong')

```

## Multiline line strings

---

These are strings that can span across multiple lines. Above we created a new line using the "_\n_" character. However, this could become some pain if we want something that spans across let's say like 20 lines

### Writing the multiline strings

---

To write multi-lines, we use the tripple quotes.

```python
"""
This is a multiline string

It can span across multiple lines

Hurray!!!!
"""

#With single quotes,

'''
This is a multiline string

It can span across multiple lines

Hurray!!!!
'''

```

## Formatted strings

---

There are some cases where you would want to use variables inside your strings. Normally, what you'll do is to concatenated using the plus (_+_) operator like so

```python
name = "Kingsley"
age = 17
print("my name is " + name + ", I am [", age "] years old")
#Output:
# my name is Kingsley , I am [17] years old
```

What if you want to use many variables or operations; you will have to concatenate and I pity you 😂😂😂.

That is where formatted strings come in; Formatted strings are basically strings that start with an f before the quotes

```python
print(f"This is a formatted string")
print(f'This is another formatted string')
print(f'''This is yet another formatted string''')
```

So how do we add variables?

Well, we do that with curly braces ( **{}** )

```python
name = "Kingsley"
age = 17
print(f"my name is {name}, I am [{age}] years old")
#Output:
# my name is Kingsley , I am [17] years old
```

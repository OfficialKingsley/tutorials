<!-- @format -->

# Working with text

In javascript, we usually change text using _innerHTML_ (where we could actually add html code and normal text ) or _value_ (for input elements)

There are actually two ways to go about it

### Method 1

---

```js
$("h1").text("The text that you want in the element");
```

### Method 2

---

```js
$("h1").html("<em>The text that you want in the element</em>");
```

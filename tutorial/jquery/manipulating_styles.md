<!-- @format -->

# Changing styles of elements

```js
//$("selector").css("property", 'value')
$("h1").css("color", "green");
```

The above code will change the color property of our h1 element to green.

To get the current value of that property, we can simply type

```js
const colorValue = $("h1").css("color");

console.log(colorValue);
//Output: rgb(0, 0, 0)
```

## Working with classes classes

---

```js
//Adding classes
$("h1").addClass("big-title");

//Removing classes
$("h1").removeClass("big-title");
```

What if we want to add multiple classes?

Well you can simply do that by separating the classes by a space

```js
//Adding two classes
$("h1").addClass("big-title margin-50");
```

Another cool feature is tha we can check if an element has a particular class

```js
$("h1").hasClass("big-title");
//This returns true or false
```

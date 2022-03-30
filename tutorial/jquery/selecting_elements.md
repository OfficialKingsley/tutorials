<!-- @format -->

# Selecting Elements

In this tutorial, we are going to be looking at selecting an element in jquery.

From the introduction page, it can be seen that

```js
//Javascript
document.querySelector("");

//jQuery
$("");
```

Just like using the querySelector, the parameter passed could be an id, element or even a class

```js
$("h1"); //Selecting an h1 element

$(".btn"); //Selecting an element with a class of btn

$("#btn-primary"); //Selecting an item with an id of btn-primary

$("h1.title"); //Select an h1 with the class of title

$("#container h1"); //Select an h1 which is a descendant of the element with the id container
```

## Selecting Multiple Elements

---

```js
//Javascript
document.querySelectorAll("button");

//jQuery
$("button");
```

Once again you see how much shorter our code has been by just using the dollar sign from jQuery

<!-- @format -->

# Working with elements

In jQuery, you can add and remove elements

For example, if I want to add an element before my h1 element, I can simply type:

```js
$("h1").before("<button>New Button</button>");
```

To create an element after another element

```js
$("h1").after("<button>New Button After the h1</button>");
```

## Prepending and appending

---

To prepend an element is that it will add the new element into the front of the content selected element and append will add it to the back of the selected element as part of the element

```js
$("h1").prepend("<button>New Button</button>");
```

Now the h1 will contain a button

```js
$("h1").append("<button>New Button</button>");
```

## Removing Elements

Incase you would like to remove let's say all the buttons in the document,

```js
$("button").remove();
```

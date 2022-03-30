<!-- @format -->

# Making animations

jQuery also comes with some animations inbuilt with that make working with animations quite easy.

Let's say we want to hide an element on the click of a button,

```js
$("button").on("click", () => {
  $(".special-text").hide();
});
```

To show the button,

```js
$("button").on("click", () => {
  $(".special-text").show();
});
```

Also, you can toggle the hide and show

```js
$("button").on("click", () => {
  $(".special-text").toggle();
});
```

---

Since hiding and showing elements can be sudden changes, we can fade it in and fade it out

```js
$("button").on("click", () => {
  $(".special-text").fadeOut();
});
```

```js
$("button").on("click", () => {
  $(".special-text").fadeIn();
});
```

And you can also toggle the fading

```js
$("button").on("click", () => {
  $(".special-text").fadeToggle();
});
```

For event more presentable animations, we can slide our elements up and down which will present a really nice collapsing of the element

```js
$("button").on("click", () => {
  $(".special-text").slideUp();
});
```

```js
$("button").on("click", () => {
  $(".special-text").slideDown();
});
```

```js
$("button").on("click", () => {
  $(".special-text").slideToggle();
});
```

### The animate method

---

The animate method is used when you want to change to a particular style. With the animate method, you can tell what style you want to change to

```js
$("button").on("click", () => {
  $(".special-text").animate({ opacity: 0.5 });
});
```

It is also advised that when using the animate method that you always use properties that have numeric values

```js
$("button").on("click", () => {
  $(".special-text").animate({ margin: "50%" });
});
```

You can also chain these effects

```js
$("button").on("click", () => {
  $(".special-text").slideUp().slideDown().animate({ opacity: 0.5 });
});
```

Note that the animations will happen one after another because for example you can't slide up and slide down at the same time or how do you want to do that 🙄👀😂

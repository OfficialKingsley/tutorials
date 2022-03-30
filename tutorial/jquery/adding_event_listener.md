<!-- @format -->

# Working with events

This is actually a whole lot simpler than when working with vanilla javascript

For example, if we want to add the click event, we could just type

```js
$("button").click(() => {
  $("h1").addClass("purple");
});
```

You should also note from the above code, the above will be added to all the buttons in the document

It's not only the click event that you can add to an element. You can also add the keypress event

```js
$("input").keypress((event) => {
  $("h1").text(event.key);
});
```

The other way of using events is with the on method which takes the event and then a call back

```js
$("h1").on("mouseover", (e) => {
  $("h1").css("color", "purple");
});
```

0170950081
GT Bank
Oladapo Olusola Fadonu

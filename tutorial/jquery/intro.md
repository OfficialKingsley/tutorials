<!-- @format -->

# Introduction to jQuery

What is jQuery?

Well, jQuery is a javascript library (in fact the most popular) created by **_John Resig_**.

There are so many javascript libraries out there but none has been used or downloaded.

For example, if you just take a look at the code below

```javascript
for (i = 0; i < document.querySelectorAll("button").length; i++) {
  document.querySelectorAll("button")[i].addEventListener("click", function () {
    document.querySelector("h1").style.color = "red";
  });
}
```

You'll see that what the code is just doing is that it finds all the buttons in the document and adds the event listener to them so when they are clicked, the change the color of the first h1 in the document

You see that this is long code for such simple task

If we want to write all the above javascript code in jQuery you'll just type something simple as:

```jsx
//Javascript
document.querySelector("h1");

//jQuery
jQuery("h1");

//An even shorter syntax
$("h1");
```

You can see that the code is shorter

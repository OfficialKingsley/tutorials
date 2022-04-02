<!-- @format -->

# Self calling functions

You can make a function to call itself after you have defined it

```js
(function () {
  //Do something
})();
```

Notice that the function definition was put in parentheses and another parentheses was put after the

The second parentheses actually takes in arguments for the function if parameters are specified

```js
(function (name) {
  console.log(`my name is ${name}`);
})("Kingsley");
```

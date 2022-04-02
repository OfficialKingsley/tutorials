<!-- @format -->

# The While Loop

The while loop loops through a block of code as long as a specified condition is true.

```js
while (condition) {
  /*code block to be executed*/
}
```

In the following example, the code in the loop will run, over and over again, as long as a variable (i) is less than 10:

```js
while (i <= 10) {
  text += "The number is " + i;
  i++;
}
```

Note If you forget to increase the variable used in the condition, the loop will never end. This will crash your browser.

You can also type a loop to keep running unless a break statement is found

```js
let i = 0;
while (true) {
  if (i < 10) {
    break;
  }
  console.log("He is a good boy");
  i++;
}
```

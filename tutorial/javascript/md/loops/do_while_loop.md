<!-- @format -->

# The do ... while loop

The do/while loop is a variant of the while loop. This loop will execute the code block once, before checking if the condition is true, then it will repeat the loop as long as the condition is true.

```js
do {
  //code block to be executed
} while (condition);
```

```js
do {
  text += "The number is " + i;
  i++;
} while (i <= 10);
```

```js
do {
  //the best you can
} while (youStillHaveTime);
```

Do not forget to increase the variable used in the condition, otherwise
the loop will never end!

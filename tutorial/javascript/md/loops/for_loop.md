<!-- @format -->

# For loop

The for loop is often the tool you will use when you want to create a loop to iterate over something like maybe an array or a string. The for loop has the following syntax:

```js
for (statement1; statement2; statement3) {
  //code block to be executed
}
```

## Meaning of these statements

---

Statement 1 is executed before the loop (the code block) starts. So that statement 1 is usually an assignment of the iterator to a value (since it is run before the loop starts)

> The first statement is used to assign a value to the iteration variable which is often called `i` but can be any other variable

Statement 2 defines the condition for running the loop (the code block). That means the loop will keep running as long as that condition is true

> The second statement is a condition for the condition to keep running. Once that statement is false, the loop will stop

Statement 3 is executed each time after the loop (the code block) has been executed. It is usually an increment so that we keep increasing the value till a point where the condition becomes false

> It should also be noted that the loop will stop after each item in the array has been iterated over

```js
for (let i = 0; i < 5; i++) {
  text += "The number is " + i + " ";
}
```

For the above example:

> Statement 1 sets a variable before the loop starts (var i = 0).

> Statement 2 defines the condition for the loop to run (`i must be less than5` for the loop to keep running).

> Statement 3 increases a value (`i++`) each time the code block in the loop has been executed.

## The statements are optional

---

### Statement 1

---

Statement 1 Normally you will use statement 1 to initiate the variable used in the loop (`let i = 0`). This is not always the case as javaScript doesn't care meaning that Statement 1 is optional.

And you can omit statement 1 (like when your values are set before the loop starts):

```js
let i = 0;
for (; i < 5; i++) {
  console.log(i);
}

// 0
// 1
// 2
// 3
// 4
```

```js
var i = 2;
var len = cars.length;
var text = "";
for (; i < len; i++) {
  text += cars[i] + "";
}
```

You can initiate many values in statement 1 (separated by comma):

```js
for (i = 0, len = cars.length, text = ""; i < len; i++) {
  text += cars[i] + "";
}
```

### Statement 2

---

Often statement 2 is used to evaluate the condition of the initial variable. This is not always the case as JavaScript doesn't care. making Statement 2 also optional. If statement 2 returns true, the loop will start over
again, if it returns false, the loop will end.

> Note If you omit statement 2, you must provide a break inside the loop. Otherwise the loop will never end. This will crash your browser.

```js
const numbers = [10, 20, 30, 40, 50];
const len = numbers.length - 1;
let i = 0;

for (; ; i++) {
  console.log(numbers[i]);
  if (i === len) {
    break;
  }
}
```

### Statement three

---

Often statement 3 increases the initial variable. This is not always the case, JavaScript doesn't care, and statement 3 is optional.

Statement 3 can do anything like negative increment or decrement to be correct (i--), positive increment (i = i + 15), or anything else so it doesn't have to just be `i++`

Statement 3 can also be omitted (like when you increment your values inside the loop):

```js
var i = 0;
var len = cars.length;
for (; i < len; ) {
  text += cars[i] + "";
  i++;
}
```

<!-- @format -->

# Loops

Loops are code that are used for doing something over and over again for a specified number of times

A loop is a statement or function that helps code to run over and over again

```js
//For example we have an array of cars
let cars = ["Volvo", "Benz", "Toyota", "Nissan", "Innoson"];
```

From the list of cars, we maybe want to get each item and do something with it

Instead of writing:

```js
let cars = ["Volvo", "Benz", "Toyota", "Nissan", "Innoson"];

console.log(cars[0]);
console.log(cars[1]);
console.log(cars[2]);
console.log(cars[3]);
console.log(cars[4]);
```

What we can do is that we loop through it and do something with it

```js
let text = "";
let cars = ["Volvo", "Benz", "Toyota", "Nissan", "Innoson"];
for (let i = 0; i < cars.length; i++) {
  console.log(cars[i]);
}
```

## Examples of loops

- `for` loop
- `for ... in` loop (for objects)
- `for ... of` loop (for arrays)
- `while` loop
- `do ... while` loop

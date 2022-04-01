<!-- @format -->

# Getters and setters in classes

These are used to define methods on a class which are then used as if they are properties

## Getters

---

These are functions (or methods) that return values. However, they are not accessed as methods; instead, they are accessed as attributes will be accessed

```js
class Square {
  constructor(width) {
    this.width = width;
    this.height = width;
  }

  //Creating a Getters
  get area() {
    return this.width * this.height;
  }
}

const mySquare = new Square(5);

console.log(mySquare.area);

//See that we don't need to use parentheses
//This outputs 25
```

## Setters

---

Similar to getters, we have setters which allow us to assign new values to the object

```js
class Square {
  constructor(width) {
    this.width = width;
    this.height = width;
  }
  //Creating a Getters
  get area() {
    return this.width * this.height;
  }

  set area(area) {
    this.width = Math.sqrt(area);
    this.height = this.width;
  }
}

const mySquare = new Square(4);
//This outputs 25

mySquare.area = 25;
//Now we are setting it
console.log(this.width, this.height);
//Output: 5, 5
```

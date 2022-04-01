<!-- @format -->

## Static methods

---

This is a method that you define in a class but it is not part of the instance methods.
They are also called helper methods. You don't need an instance of the object to use the
helper method. They don't have an object bound to them

These methods are called on the constructor or on the class itself and not on the
objects created by the class

```js
class Square {
  constructor(width) {
    this.width = width;
    this.height = width;
  }
  static equals(a, b) {
    //Checks if the squares are of equals
    //Width and height

    return a.width === b.width;
  }
}

let mySquare = new Square(8);
let mySquare2 = new Square(5);

console.log(Square.equals(mySquare, mySquare2));

//Output false
```

```js
class Square {
  constructor(width) {
    this.width = width;
    this.height = width;
  }
  static equals(a, b) {
    //Checks if the squares are of equals
    //Width and height

    return a.width === b.width;
  }
}

let mySquare = new Square(5);
let mySquare2 = new Square(5);

console.log(Square.equals(mySquare, mySquare2));
// Output: true;
```

Notice that the equals method was called on the `Square` class itself and not on any object which is an instance of the class

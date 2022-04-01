<!-- @format -->

# Introduction to Javascript Classes

Classes are used to make objects. They are like constructors. An object could be defined
as a creation from a class

These objects can have (instance) properties. These are the properties that the object
has. These properties can be defined using the class.
<br />
For example, a human being has properties like hands, legs, eyes, name, age, height etc.

These objects also have what we call (instance) methods. These arae functions or
possible actions of the object.
<br />
For example, a human can eat, run, walk etc.

These properties are unique to any object that is created from the class definition

## Creating a class

---

To create a class we use the `class` keyword

```js
class className {
  //class definition
}
```

## Naming convention

---

When naming classes, we make the first letter uppercase
<br/>
<br/>
<br/>

## Class constructor

---

A constructor can be defined as a method which is ran only once during the life of the
object. It only runs once and it is ran when the object is being created from the class.
<br />
A constructor can also be said to be a function to setup the object from the class

```js
class Rectangle {
  constructor() {
    console.log("The rectangle is being created");
  }
}
```

### Creating an object from the class

---

To create an object from the class, we do:

```js
let objectName = new ClassName();
```

> For example

```js
let myRectangle = new Rectangle();
//Notice the parentheses.
//That is the effect of the constructor
```

> If you have read our notes on constructor functions you'll see that a constructor is a function used to create an object

we can specify the object properties in the constructor method

To create a property we use the `this` keyword like so:

`this.propertyName = value;`

The this keyword refers to the current object or the object that has been created with
the class

```js
class Rectangle {
  constructor() {
    console.log("An object is being created");

    this.width = 5;
    this.height = 3;
    this.color = "blue";
  }
}

let myRectangle = new Rectangle();
//Now we can access these properties using the dot notation;

console.log(myRectangle.width);

//Output: 5;
```

Usually, what you will want to do is to make the user specify how he or she wants the
rectangle to be <br/>
To do this, we have to specify parameters in the constructor function or method

```js
class Rectangle {
  constructor (width, height, color) {
    console.log("An object is being created");

    this.width = width;
    this.height = height;
    this.color = color;
  }
}

let myRectangle = new Rectangle(5, 3, b"blue");
//Now we can access these properties using the dot notation;

console.log(myRectangle.width)

//Output: 5;

```

## Methods

---

Recall that a method is an action that can be carried out by an object

To create a method, you can do this

```js
methodName () {
  //operations of the method
}

//Accessing the method
Rectangle1.methodName();

```

```js
class Rectangle {
  constructor(length, breadth) {
    this.length = length;
    this.breadth = breadth;
  }

  getArea() {
    return this.length * this.breadth;
  }
}
```

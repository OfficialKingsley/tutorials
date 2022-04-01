<!-- @format -->

# Inheritance in javascript classes

What is inheritance?
<br/>
Inheritance is the process of getting some attributes or methods from a parent (or higher class) and embedding it into another

As the name implies, inheritance refers to having properties or methods in
a child class from a parent (generic) class while the child still has its
own properties and characteristics

The extends keyword helps us to use the concept of inheritance.

```js
class Person {
  constructor(name, age) {
    this.name = name;
    this.age = age;
  }

  describe() {
    console.log(`I am ${this.name} and I am {this.age} years old`);
  }
}
//Now we can access all the properties and methods of the Parent (Person)

class Programmer extends Person {
  constructor(name, age, years_of_experience) {
    super(name, age);
    //Same thing as doing Person(name, age)
  }
}

//Now we can access the methods and props of this parent object from the parent object

function developSoftware(programmers) {
  //developSoftware
}
```

Notice the `super` function that was called. It signifies calling the parent class which in the above case was the `Parent` class

Even if we extend to a parent class, we can still perform operations specific to the new class

## Polymorphism

---

This refers to changing a method in a child that has already been defined in the parent and making it perform a new task. However this polymorphisized method will only accessible in the children

```js
class Animal {
  constructor(name) {
    this.name = name;
  }
  makeSound() {
    console.log("i am an animal making a sound");
  }
}

class Dog extends Animal {
  constructor(dogName) {
    super(dogName);
  }
  makeSound() {
    console.log("I am a barking dog");
  }
}

let myAnimal = new Animal("Animal name");
myAnimal.makeSound();
//Output: i am an animal making a sound

let myDog = new Dog("this dog");
myDog.makeSound();
//Output: I am a barking dog
```

We can also access the values of a method of a parent when
polymorphisizing

```js
class Animal {
  constructor(name) {
    this.name = name;
  }
  makeSound() {
    console.log("i am an animal making a sound");
  }
}

class Dog extends Animal {
  constructor(dogName) {
    super(dogName);
  }
  makeSound() {
    super.makeSound();
    console.log("I am a barking dog");
  }
}

let myAnimal = new Animal("Animal name");
myAnimal.makeSound();
//Output: i am an animal making a sound

let myDog = new Dog("this dog");
myDog.makeSound();
//Output: i am an animal making a sound
//Output: I am a barking dog
```

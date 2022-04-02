<!-- @format -->

# The For/In Loop

The JavaScript for/in statement loops through the properties of an object:

```js
var person = {
  firstName: "John",
  lastName: "Doe",
  age: 25,
};

var text = "";
var x;

for (attribute in person) {
  if (typeof attribute === "string") {
    text += person[attribute];
  }
}
```

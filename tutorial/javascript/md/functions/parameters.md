<!-- @format -->

# Function Parameters

When you create a function, you might want this function to be able to accept some data and do something with this accepted data. This is made possible by function parameters and arguments

A parameter can be defined as a variable defined with a function definition

```js
function myFunction(parameter) {
  console.log(parameter);
}
```

> When calling the function, you also have to specify the parameter i.e. pass in an argument

```js
myFunction("Kingsley");
//This will log out Kingsley
```

## Multiple parameters

<p>You can also specify multiple parameters</p>

```js
function myFunction(name, age) {
  console.log(name + " is" + age + " years old");
}
```

If you are not sure of the number of parameters passed, you can use the `rest operator`

```js
function (...names) {
  console.log(names[0])
}
```

The names parameter above will be an array containing the argument/arguments that are passed in

## Predefining parameter values

You can also predefine the parameter values

```js
function myFunction(name = "Kingsley", age) {
  console.log(name + " is" + age + " years old");
}
```

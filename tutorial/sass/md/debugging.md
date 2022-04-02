<!-- @format -->

# Debugging

There are some cases where you may want debug or get the value of a calculation in your console when working. To do this you will need the `@debug` command

```scss
@debug "Hello world";
//Output: Hello world
```

The above will actually log out Hello world to the con sole

```scss
@use "sass:math";

@debug "Hello world";
@debug math.div(10, 3);
@debug math.floor(2.6);
@debug math.max(1px, 20px, 15px, 12px);

//Outputs:
// Hello world
// 3.33333333333
// 2
```

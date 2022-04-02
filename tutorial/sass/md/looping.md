<!-- @format -->

# Looping in sass

One very handy feature in sass is that you can loop through a map or an iterable object and do something with it

To loop through, we use the `@each ... in` syntax for maps

```scss
@each $key_iterator_name, $value_iterator_name in map_name {
  // Do something
}
```

```scss
@each $key, $value in colors {
  .text-#{$key} {
    color: $val;
  }
  .bg-#{$key} {
    background-color: $val;
  }
}
```

So for each iteration it generates a key-value pair and then we created a new class with it

Notice the syntax we used to dynamically create new classes. Therefore to use a `#{$key_name}`

## For loop

---

From the above, it can be seen that the each loop is used to iterate over something however for the for loop, we normally want to perform a task for a specific object a number of times

```scss
@for $iteration-variable from start through final {
  //do something
}
```

```scss
@each $key, $value in colors {
  .text-#{$key} {
    color: $val;
  }
  .bg-#{$key} {
    background-color: $val;
  }

  @for $i from 1 through 9 {
    .text-#{$key}-light-#{$i} {
      color: mix(white, $val, $i * 10);
    }
    .bg-#{$key}-light-#{$i} {
      background-color: mix(white, $val, $i * 10);
    }
  }
}
```

> The `mix` function is used to mix two different colors together

> The first parameter is the the value you want to mix, the second parameter is the base color

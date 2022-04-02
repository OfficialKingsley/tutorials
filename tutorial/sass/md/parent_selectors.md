<!-- @format -->

# Parent Selectors

These are going to help us create variations of classes to effects like hover and other pseudo selectors. In some cases you might want to add a class when you hover over something

The parent selector is actually the `&` sign which can be nested in what it references and when it is called it actually gets that element

```scss
//CSS
h1 {
  color: red;
}
h1:hover {
  color: green;
}

// SCSS
h1 {
  color: red;
  &:hover {
    color: green;
  }
}
```

> The `&` sign references the h1 which is the parent element of where it is nested

```scss
@each $key, $value in colors {
  .text-#{$key} {
    color: $val;
  }
  .text-hover-#{$key} {
    &:hover {
      color: $val;
    }
  }
  .bg-#{$key} {
    background-color: $val;
  }
}
```

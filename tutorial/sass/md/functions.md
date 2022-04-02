<!-- @format -->

# Functions

A function is a code that may take in arguments and returns just one value un like mixins which return multiple values or properties

If for example we want to create a button that will get a complementary color as text. That is a contrasting color from its background

> In a function file

```scss
@function light-comp($color) {
  $complement = complement($color);
  $light-complement: lighten($complement, 30%)
  @return $light-complement;
}
```

```scss
@each $key, $val in $colors {
  .btn-complement-#{$key} {
    @include btn($val);
    color: light-comp($val);
    &:hover {
      color: $val;
      color: light-comp($val);
    }
  }
}
```

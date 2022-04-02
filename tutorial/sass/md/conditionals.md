<!-- @format -->

# Conditional statements

Just like other programming languages, we can also have `if ... else` statements in sass

```scss
@if (10 > 5) {
  .test-if {
    color: blue;
  }
} @else {
  .test-if-2 {
    color: white;
  }
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

  @if ($val != black and $val != white) {
    @for $i from 1 through 9 {
      .text-#{$key}-light-#{$i} {
        color: mix(white, $val, $i * 10);
      }
      .bg-#{$key}-light-#{$i} {
        background-color: mix(white, $val, $i * 10);
      }
    }
  }
}
```

That way, we are not going to get variations for the black and white colors

<!-- @format -->

# Mixins

Mixins are a way for us to group css properties and values so they can be included in different css rules

It could be that some selectors have maybe the same margin and padding or same properties and values so instead of writing the same for all the selectors, you can uses `mixins`

```scss
@each $key, $val in $colors {
  .btn-#{$key} {
    text-decoration: none;
    cursor: pointer;
    display: inline-block;
    border: 0;
    padding: $base-padding $base-padding * 2;
    border-radius: $base-border-radius;
    background-color: $val;
  }
  .btn-#{$key} {
    text-decoration: none;
    cursor: pointer;
    display: inline-block;
    border: $base-border-thickness;
    padding: $base-padding $base-padding * 2;
    border-radius: $base-border-radius;
    background-color: white;
  }
}
```

Now you can see that there is a repitition of code

```scss
@mixin btn() {
  text-decoration: none;
  cursor: pointer;
  display: inline-block;
  border: $base-border-thickness;
  padding: $base-padding $base-padding * 2;
  border-radius: $base-border-radius;
}
```

```scss
@each $key, $val in $colors {
  .btn-#{$key} {
    @include btn();
    background-color: $val;
  }
  .btn-#{$key} {
    @include btn();
    background-color: white;
  }
}
```

We need to know that mixins can actually accept values and use them in the styles

```scss
@mixin btn($bg-color) {
  text-decoration: none;
  cursor: pointer;
  display: inline-block;
  border: $base-border-thickness;
  padding: $base-padding $base-padding * 2;
  border-radius: $base-border-radius;
  background-color: $bg-color;
}
```

```scss
@each $key, $val in $colors {
  .btn-#{$key} {
    @include btn($val);
  }
  .btn-#{$key} {
    @include btn(white);
  }
}
```

You can also pass in default values for your parameters just incase it is not specified

```scss
@mixin btn($bg-color: #e2e2e2) {
  text-decoration: none;
  cursor: pointer;
  display: inline-block;
  border: $base-border-thickness;
  padding: $base-padding $base-padding * 2;
  border-radius: $base-border-radius;
  background-color: $bg-color;
}

// We decide to create a new generic class

.btn {
  @include btn;
  &:hover {
    background-color: lighten(green, 50%);
  }
}

// Without the parentheses
```

Lighten is an inbuilt function

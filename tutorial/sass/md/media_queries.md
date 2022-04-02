<!-- @format -->

# Media queries

```scss
$break-points: (
  "xs": 0,
  "sm": 480px,
  "md": 720px,
  "lg": 960px,
  "xl": 1200px,
);

@mixin xs {
  @media (min-width: map.get($breakpoints: "xs")) {
    @content;
    //The content is added so whenever we use that mixin
    // and put content in it, it is added to the mixin
  }
}

@mixin breakpoint($bp: 0) {
  @media (min-width: $bp) {
    @content;
  }
}

.responsive-test {
  @include xs {
    color: red;
  }
  @include sm {
    color: green;
  }
  @include md {
    color: yellow;
  }
  @include lg {
    color: orange;
  }
  @include xl {
    color: purple;
  }
  @include breakpoint(350px) {
    color: mix(red, blue, 50%);
  }
}
```

<!-- @format -->

# Grid sample

```scss
@use "sass:math" $grid-columns: 12 .container {
  width: 100%;
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
  box-sizing: border-box;
}
.row {
  display: flex;
  flex-flow: row wrap;
}

// col classes
// .col-12-xs Whatever has this class should have a width of 12 columns in extra-small screens

@include lg {
  @for $i from 1 through $grid-columns {
    .col-#{$i}-lg {
      box-sizing: border-box;
      flex-grow: 0;
      width: math.div($i * 100%, $grid-columns);
    }
  }
}
```

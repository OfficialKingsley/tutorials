<!-- @format -->

# Lists in sass

Lists in sass are different from the maps. They are just comma separated items

```scss
$layout-values: flex-start, flex-end, center, space-between, space-around;
```

## Looping through lists

```scss
@each $val in $layout-values {
  .justify-#{val} {
    justify-content: $val;
  }
}
```

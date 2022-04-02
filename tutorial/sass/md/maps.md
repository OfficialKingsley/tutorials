<!-- @format -->

# Maps in sass

These are a way of getting a collection of items in key value pairs like objects in javascript or associative arrays in other programming languages

```scss
$primary: #326dee;
$secondary: #1ac888;
$error: #d32752;
$info: #f6c31c;

// color palette (map)

$colors: (
  "primary": $primary,
  "secondary": $secondary,
  "error": $error,
  "info": $info,
  "blue": #1919e6,
  "red": #e61919,
  "yellow": #e6e619,
  "green": #19e635,
  "orange": #ffa600,
  "purple": #9900ff,
  "gray": #808080,
  "black": black,
  "white": white,
);
```

## Getting the data

---

```scss
// Syntax
// map-get(map-name, key)

@debug map-get($colors, "purple");

// Output: #9900ff
```

## Checking for values

---

```scss
@debug map-has-key($colors, "secondary");

// Output: true
@debug map-has-key($colors, "tertiary");

// Output: false
```

## Removing a key

---

```scss
@debug map-remove($colors, "primary");

/*

Output:

(
  "secondary": $secondary,
  "error": $error,
  "info": $info,
  "blue": #1919e6,
  "red": #e61919,
  "yellow": #e6e619,
  "green": #19e635,
  "orange": #ffa600,
  "purple": #9900ff,
  "gray": #808080,
  "black": black,
  "white": white,
);

*/
```

Notice that it logged out the map with the `primary` no longer there

## Adding new items

---

To add something to a map the syntax is as follows

```scss
// map-merge(map_to_add_to, new_map_to_be_added)

@debug map-merge(
  $colors,
  (
    "pink": #ffc0cb,
  )
);
```

We can also use these maps in selectors

```scss
.test {
  background-color: map-get($colors, "purple");
}
```

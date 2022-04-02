<!-- @format -->

# Variables in SASS

Sass variables are created with the dollar sign and then followed by the variable name

```scss
$primary: #326dee;
$secondary: #1ac888;
$error: #d32752;
$info: #f6c31c;
```

```scss
// Variables
  // Theme colors
  $primary: #326dee;
  $secondary: #1ac888;
  $error: #d32752;
  $info: #f6c31c;

  // Spacing
  $base-padding: 0.75rem;
  $base-margin: 0.75rem;

  // Borders
  $base-border-thickness: 1px;
  $base-border-radius: 20px;

// Styles
h1 {
  color: $primary;
}
a {
  color: $secondary;
}
button {
  color: white;
  border: 0;
  background: $primary;
  padding: $base-padding;
  border-radius: $base-border-radius;
}

.error {
  color: $error;
  border-color: $error;
  border-style: solid;
  margin: $base-margin;
  padding: $base-padding;
  border-radius: $base-border-radius;
  border-width: $base-border-thickness;
}

.notification {
  color; $secondary;
  border-color: $secondary;
  border-style: solid;
  margin: $base-margin;
  padding: $base-padding;
  border-radius: $base-border-radius;
  border-width: $base-border-thickness;
}
```

So from the above, we can see that the variables are not just used in colors but can also be used in spacing or border

<!-- @format -->

# Partials

This is actually a way of separating our code into different (partial) files. For example, we could have a file for buttons,
a file for variables etc

So for example we could create a `variables.scss` file and put all our variables in that file

> In the `variables.scss`

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

//box-shadow
$base-box-shadow: 1px 3px 5px rgba(0, 0, 0, 0.1);

// font-size
$base-font-size: 1rem;
```

Before we can use it in our `index.scss` we have ti import it

```scss
@import "variables";

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

As you can see, we don't need to type the extension `.scss` or `.sass` as the compiler is smart enough to detect that

In some gulp files, the programmer might decide to watch all the scss files by using the wild card `*` selector

```js
const { src, dest, watch, series } = require("gulp");

const sass = require("gulp-sass")(require("sass"));

function buildStyles() {
  return src("*.scss").pipe(sass()).pipe(dest("css"));
}

//Function that watches the sass file
function watchTask() {
  watch(["*.scss"], buildStyles);
}

exports.default = series(buildStyles, watchTask);
```

In the above, we are telling the compiler to watch every sass file and for each sass file, create a new css file in the css directory

Programmers usually do this because there are some times where you might have or want special sass files for different pages.

However, we do not want our partial files to also be compiled into new css files. To avoid our partial files being compiled, we change the naming convention

Instead of saving our partials as `something.scss`, we add an underscore in front of the name to tell the compiler to ignore it like `_something.scss` or in the above case, `_variables.scss`

Note that the method of import is actually very import. For example if you want to use variables in a base file and then you import the base before you import variables, you will get an error

> In short, Always import a dependent partial after what it depends on

```scss
// variables & functions
// base and layout
// colors
// components (button, card, navbar)
//utilities (margin, padding, opacity)
```

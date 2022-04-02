<!-- @format -->

# Using the default keyword

If there are some cases where the user might override the (global variables) you have to used the `!default` keyword

Normally in the files this won't be possible because

```scss
@import "library/index.scss";
// The same as
@import "library/index";
// Also the same as
@import "library";
// Because css automatically imports the index.scss file of a folder
```

```scss
@import "library";
$primary: red;
```

Even though we are resetting the value of that variable, operations have already been performed with those variables and the values have already been used

If we also try:

```scss
$primary: red;
@import "library";
```

So we decide to change the variable before importing the file, the thing is that even though we have set the variable in our own file, the value will be overridden in the library folder

So how do we fix this?

Well when creating a library, we make the current values of our variables the default incase a user might decide to change the values

> In the library \_variables.scss

```scss
$primary: #45638f !default;
$secondary: #ab2e11 !default;
$global-size: 2rem !default;
```

The default keyword tells sass that if there is not any defined value then use these values given

> And in our own sass folder and file

```scss
$primary: red;
@import "library";
```

Notice that we declared the variable before importing

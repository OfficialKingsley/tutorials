<!-- @format -->

# Performing Maths

Another thing about sass or css in general is that you can perform mathematical operations with your variables and other units

> Variables

## Multiplication

---

```scss
$base-font-size: 1rem;

$font-size-sm: $base-font-size * 0.75;
$font-size-lg: $base-font-size * 1.5;
$font-size-xl: $base-font-size * 2;
$font-size-xxl: $base-font-size * 3;
```

## Division

---

Division is a little different from multiplication because you have to use the math package to divide

> If you type:

```scss
.button {
  border-radius: $base-border-radius / 4;
}
```

You'll actually get an error; therefore the way of doing a division is by using the math package

When you want to use an inbuilt package in sass, we use the `@use` command

```scss
@use "sass:math";

.button {
  border-radius: math.div($base-border-radius, 4);
}
```

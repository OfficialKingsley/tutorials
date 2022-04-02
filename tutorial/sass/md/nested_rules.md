<!-- @format -->

# Nested Rules

One amazing feature about `sass` is the ability to nest css rules

> In css:

```css
.card {
  display: block;
}
.card .card-title {
  font-size: 1.5rem;
}
.card .card-body {
  color: green;
}
```

> In scss:

```scss
.card {
  display: block;
  .card .card-title {
    font-size: 1.5rem;
  }
  .card .card-body {
    color: green;
    a {
      text-decoration: underline;
    }
  }
}
```

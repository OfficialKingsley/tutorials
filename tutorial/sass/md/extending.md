<!-- @format -->

# Extending features

You can extend some properties from other rules

```scss
.flex-layout {
  width: 100%;
  display: flex;
  align-items: center;
}
.navbar {
  @extend .flex-layout;
  padding: $base-padding;
  .site-title {
    font-size: 2rem;
  }
  .container {
    @extend .flex-layout;
  }
}
```

## Using the placeholder rule

---

The place holder rule is used when you don't want that particular rule to be compiled into the css but you may want to extend it or reuse that particular rule. To do this, we make use of the percentage `%` sign

```scss
%flex-layout {
  width: 100%;
  display: flex;
  align-items: center;
}
.navbar {
  @extend %flex-layout;
  padding: $base-padding;
  .site-title {
    font-size: 2rem;
  }
  .container {
    @extend %flex-layout;
  }
}
```

<!-- @format -->

# Props in React

Since we are using functions, the props are the parameters of the function components

```jsx
const Header = (props) => {
  return (
    <header>
      <h1>{props.title}</h1>
    </header>
  );
};
export default Header;
//Notice that we exported it
```

## Passing in the props

---

Depending on where it is imported, you can do this:

```jsx
import Header from "Header";
<Header title="my Title" />;
```

What the above will do is that it will display my Title which was defined as <code>props.title</code> in the h1 element.

## Default Props

---

You can also give default values to the props since the props is an object. This can be done as follows

> In the `Header.js`

```jsx
Header.defaultProps = {
  title: "Task Tracker",
};
```

So if the `props.title` is not given, then the default is used

## Datatype of props

---

Similar to `state`, props is also an object

Since the props is an object, we can destructure and the above can be done as follows:

```jsx
const Header = ({ title }) => {
  //See that we used an object
  //In better terms, we destructured the props object
  return (
    <header>
      <h1>{title}</h1> //We removed props
    </header>
  );
};
export default Header;
```

  </body>
</html>

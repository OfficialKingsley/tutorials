<!-- @format -->

# Prop types

```jsx
import PropTypes from "prop-types";

Header.propTypes = {
  title: PropTypes.string,
};
```

## Required propTypes

---

```jsx
import PropTypes from "prop-types";

const Header = ({ title }) => {
  return (
    <>
      <h1>{title}</h1>
    </>
  );
};
Header.propTypes = {
  title: PropTypes.string.isRequired,
};
```

> So if we do what is below, we get an error

```jsx
import Header from "Header";
const App = () => {
  return <Header title={2} />;
};
```

The error gotten is because we specified the `title` prop to be a string and we were passing in a number

> Notice the use of curly braces

> We use curly braces when the prop is not a string

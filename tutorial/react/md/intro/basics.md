<!-- @format -->

```jsx
ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById("root")
);
```

In the above, we are telling react to render the app in strict mode inside the html with an id of root

## JSX

---

JSX is actually a new extension added to react to make writing both the
HTML and the logic in the same component possible

In the app.js, we must have only one container that is the container for all your work.

You can put javaScript in JSX using curly braces.

```jsx
const Header = (props) => {
  return (
    <header>
      <h1>{props.title}</h1>
    </header>
  );
};
export default Header;
```

## Naming convention of Components

---

The naming convention for components is to start it with a capital letter - just like when naming classes

`Header.js`

> To use a component, you need to import the component from the folder where it was defined

```jsx
import Header from Header.js
// If it was exported as default
import { Header } from Header.js
//If it was exported but not as default
```

This imported component can be embedded into the JSX as an XML e.g. if we
have a Header Component, `<Header />`

```jsx
import Header from Header;

const App = () => {
  return (
    <Header/>
  )
}

export default App
// This is what I mean by export default
```

> Remember to always put the backslash before the closing brackets (because react uses strict mode)

> Also remember that if you want to use a component, outside where it was defined, you have to export it

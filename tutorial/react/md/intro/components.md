<!-- @format -->

# Components in React

In react, we think of every part of the app as a component. We shouldn't make the mistake of thinking an html tag is a component. They are two different things <br />
In react almost every part is a component. A button is a component. the tweets section is a component. Each tweet in the tweets section is

In react, each component could be either a function or a class

> For the functional based component 👇🏾👇🏾👇🏾

```jsx
export const Header = () => {
  return (
    <div>
      <h1>My Header</h1>
    </div>
  );
};
```

> Now the class based component

```jsx
export default class Header extends React.Component {
  render() {
    return (
      <div>
        <h1>My Header </h1>
      </div>
    );
  }
}
```

A component can simply be defined as a part of the app. It doesn't necessarily mean an html element. <br />
For example, a blog of posts is a component, each post is also a component.

These components are made up of html elements or other components in them

## States

---

Components can contain states. **_States_** are objects that determine how a component renders and behaves. e.,g a collapsible menu that will have a close and open state. You may have an state object that has a value of `true` or `false`. <br />
State could also be defined as the data of a component

Any data used in your component is part of state. You can share your states across multiple component using app state or global state. Some times you have many apps states that can get difficult to manage. You could react's context API or an external state manager like Redux.

> Prior to react 16.8, we had to use class components if we wanted to hold state but in 16.8, hooks were introduced in function components to allow the use of states

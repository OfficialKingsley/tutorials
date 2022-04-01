<!-- @format -->

# useEffect Hook

This is a function called whenever any item in the page re-renders. <br />
It is also powerful because you can call it only when specific states are re-rendered. <br />
You can also specify that it should be called once on first load of the page

> Called every time the page re-renders a state

```jsx
import { useEffect } from "react";

useEffect(() => {
  //Do something
});
```

The above `useEffect` will be called every single time the page rerenders. Whether it is necessary for it to run or not

## useEffect for specific occassions

---

To make the `useEffect` to run only when something changes, we pass those things into an array as the second parameter containing the specific items we want the `useEffect` to run when they change

```jsx
useEffect(() => {
  //Do something when the state called hello is re-rendered.
}, [hello]);
```

Notice the use of the an array to hold the specific states. These specific states are called the dependencies and the array is called a _dependency array_

If you want the useEffect to run only once and that is when the page is first rendered, you can do the following

```jsx
useEffect(() => {
  //Do something when the state called hello is re-rendered.
}, []);
```

Notice the use of the an array that has no values So after the first time it is called, it doesn't render again

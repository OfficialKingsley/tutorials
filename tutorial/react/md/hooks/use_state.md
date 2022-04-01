<!-- @format -->

# useState Hook

The state of an element refers to all the characteristics of the elements. The color, the values, the size, the UI etc.

It should however be noted that a state cannot be changed instead it can be recreated and re-rendered automatically to the browser.
<br />
For example if we are to create a counter app with a button, the counter will increase but won't show on the page. This is because we haven't told react to rerender the state of the counter when the button is clicked
<br />

> With vanilla javascript, we'll do the following

```jsx
const StateTutorial = () => {
  let counter = 0;

  const increment = () => {
    counter += 1;
    console.log(counter);
  };

  return (
    <div>
      <div>
        {counter}
        <button onClick={increment}>Increment</button>
      </div>
    </div>
  );
};

export default StateTutorial;
```

Actually, any time you click that button, the counter variable actually does increase but since a variable doesn't rerender the page, it doesn't reshow on the page

> That's where the `useState()` hook comes in

The useState hook is used to store the present state of an element and also gives a function to update itself (i.e. the state)

```jsx
import { useState } from "react";

const Component = () => {
  const [name, setName] = useState(defaultValue);
};
```

> The first item in the array is the name of the state

> The second item in that array is the name of the function that will update that paticular state

> Notice that the `useState()` hook was used inside of the component definition i.e. it wasn't declared outside the component declaration

```jsx
import { useState } from "react";

const Component = () => {
  const [count, setCount] = useState(0);

  const increment = () => {
    counter += 1;
    console.log(counter);
    //using the above method will cause an error because state cannot be changed
    //Instead we use the function for updating it which is the setCount function as follows

    setCount(count + 1);
  };

  return (
    <div>
      {counter}
      <button onClick={increment}>Increment</button>
    </div>
  );
};
```

Note that when using the `useState()` hook, you have to make sure that when setting the state with the setState function you have to make sure that the datatype that you are setting it to is equal to the data type of the
initial value

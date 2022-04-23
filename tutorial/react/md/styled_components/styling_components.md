# Adding styles to components

---

You can also add styles to your components

```jsx
import styled from "styled-components";
import Button from "./Button.jsx";

const StyledButton = styled(Button)`
  width: 200px;
  height: 50px;
`;
```

> In `Button.jsx`

```jsx
const Button = ({ className, buttonLabel }) => {
  return <button className={className}>{buttonLabel}</button>;
};
```

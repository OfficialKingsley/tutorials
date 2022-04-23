# Using themes in styled components

To do this, we import the ThemeProvider from
styled components

> In `App.js`

```jsx
import { Container } from ".components/styled/Container.styled";
import { ThemeProvider } from "styled-components";

const theme = {
  colors: {
    header: "#ebfbff",
    body: "#fff",
    footer: "#003333",
  },
};
function App() {
  return (
    <ThemeProvider theme={theme}>
      <Container bg="red">
        <h1>Hello</h1>
      </Container>
    </ThemeProvider>
  );
}
export default App;
```

> Notice that it was imported in the App.js

> The ThemeProvider takes in a prop called theme which accepts an object

> So we wrap everything around the ThemeProvider

This theme prop can be passed to any child styled component

```js
import { createGlobalStyle } from "styled-components";

const lightTheme = {
  body: "#fff",
  formColor: "#000",
};

const darkTheme = {
  body: "#000",
  formColor: "#fff",
};

export const GlobalStyles = createGlobalStyle`
  body {
    background-color: ${(props) => props.theme.body}
  }
`;
```

> Now in `app.js`

```jsx
import React, { useState } from "react";
import "./index.css";
import styled, { ThemeProvider } from "styled-components";
import { lightTheme, darkTheme, GlobalStyles } from "./themes.js";

const AppDiv = styled.div`
  color: ${(props) => props.theme.formColor};
`;
function App() {
  const [theme, setTheme] = useState("light");

  const themeToggle = () => {
    theme === "light" ? setTheme("dark") : setTheme("light");
  };
  return (
    <ThemeProvider theme={theme === "light" ? lightTheme : darkTheme}>
      <GlobalStyles />
      <AppDiv className="App">Hello world</AppDiv>
    </ThemeProvider>
  );
}
```

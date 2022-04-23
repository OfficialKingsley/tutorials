# Starting

---

> You should have a react app

```bash
npx create-react-app my-app
```

> Next you install styled components

```bash
npm i styled-components
```

> Next, start the server

```bash
npm run start
```

## Clearing

---

You can delete the boiler plate code that comes with create-react-app

In the root directory, create a file called `themes.js`

> In `themes.js`

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

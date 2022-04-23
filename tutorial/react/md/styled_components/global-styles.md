# Global Styles

If you want a style to be global or to be applied to all components, we use the createGlobalStyle from styled-component

```js
import { createGlobalStyle } from "styled-components";

const GlobalStyles = createGlobalStyle` * { box-sizing: border-box; }`;
export default GlobalStyles;
```

```js
import GlobalStyles from "Globals.styled.js";

function App() {
  <ThemeProvider theme={theme}>
    <GlobalStyles />
  </ThemeProvider>;
}
```

Right after it has been wrapped, by the `ThemeProvider`, we make it the first component.

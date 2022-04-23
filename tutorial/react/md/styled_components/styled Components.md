# Introduction

---

> In `Container.styled.js`

```jsx
import styled from "styled-components";

//const name_of_component = styled.name_of_element_you_want_it_to_be``
//inside the backticks (``), we have our styles or css

export const Container = styled.div`
  width: 100px;
  max-width: 100%;
  padding: 0 20px;
  margin: 0 auto;
`;
```

> In `App.js`

```js
import { Container } from ".components/styled/Container.styled";

//Note that we put it in curly braces. This is because we didn't say export default for it. So it is not the default export <br/>

function App() {
  return (
    <Container>
      <h1>Hello</h1>
    </Container>
  );
}

export default App;

//You'll see that when it is compiled, it will be compiled to a div
```

You can also nest in styled components just like in sass or less

```js
import styled from "styled-components";

export const Container = styled.div`
  width: 100px;
  max-width: 100%;
  padding: 0 20px;
  margin: 0 auto;

  h1 {
    color: red;
  }
  &:hover {
    background-color: green;
  }
`;
```

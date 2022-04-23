# Props

---

Styled components can also take in props

> In `app.js`

```js
import { Container } from ".components/styled/Container.styled";

function App() {
  return (
    <Container bg="red">
      <h1>Hello</h1>
    </Container>
  );
}

export default App;
```

You'll see that when it is compiled, it will be compiled to a div

> In `Container.styled.js`

```js
import styled from "styled-components";

export const Container = styled.div`
  width: 100px;
  max-width: 100%;
  padding: 0 20px;
  margin: 0 auto;
  background-color: ${(props) => props.bg};
  background-color: ${({ bg }) => bg};
`;
```

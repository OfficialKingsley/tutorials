# React Query Dev Tools

In the App.js we import react query dev tools

```js
import { QueryClient, QueryClientProvider, ReactQueryDevtools } from "react-query/devtools"
//Then the last component of the in the App.js that is wrapped around the QueryClientProvider tag
function App () {
cosnt queryClient = new QueryClient();
  return (
    <QueryClientProvider client={queryCient}>
      <ReactQueryDevtools initialIsOpen={false} position="bottom-right"/>
    </QueryClientProvider>
  )
}
```

> The initialIsOpen attribute is set to false as we do not want the ReactQueryDevTools to be open initially

> The position prop sets the position of the ReactQueryDevtools button

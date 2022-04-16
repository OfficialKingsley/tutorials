# <u>Basic queries with react-query</u>

> In the `app.js`

```js
import { QueryClientProvider ,QueryClient} from "react-query";

function App () {
  cosnt queryClient = new QueryClient();

  return (
    <QueryClientProvider client={queryCient}>
      // Every other thing in the app
    </QueryClientProvider>
  )
}
```

## Basic Data Fetching

```js
import { useQuery } from "react-query"
{
  syntax: useQuery(key,() => {
  data-fetching-function-that-returns-a-promise
  })
}
export const RQSuperHeroesPage = () => {
const {isLoading, data} = useQuery("super-heroes", ()=> {
  return axios.get("http://super-heroes.api.com/superheroes")
})

if (isLoading) {
  return <div>React Query Super Heroes</div>
}
return (
  <>
    <h2>RQ super Heroes Page</h2>
    {data?.data.map((hero)=>{
      return <div key={hero.name}>hero.name</div>
    })}
  </>
  )
}

```

> Take note of the following

> The `useQuery()` hook comes with the isLoading and data variables o we destructured them out

> The `data` variable is the total response

> `data.data` is the actual data gotten

//?. is known as the optional chaining method
//data?.data
//The above checks the first data so if it is not found it doesn't

## Normal way without react-query

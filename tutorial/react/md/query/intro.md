# <u>React Query</u>

## Meaning of Querying

What is the meaning of querying. When you use the fetch api, you're the browser cache. The concept of cache is not

React query is like this caching layer that just lives inside the memory of your application. It doesn't take over the responsibility of using the right headers and doserving er side and browser level caching. It's more of a cache that improves the user experience and fill in some of those gaps.
It is used to improve user experience and developer experience.

React just need to know your promise caching hydrating the react app when it gets to a client
You fetch data into a cache and you send that cache with your html to your client and then you hydrate the client

## <u>Introduction</u>

React query is a library for fetching data in react.
React query is a library for fetching. Since react is a UI library, there is no specific pattern for data fetching

We usually use the `useEffect` hook and `useState` hook and if the data is needed, we use a state management library like redux

Most of the state management libraries are good for working with client state like the theme for the application or whether a user is authenticated or not.
These libraries are not good for asynchronous code or server side state.

This is because _server state_ is different from _client state_

Client state persists in your app memory and accessing the data is synchronous.
In server state, the state persists remotely in a database perhaps and requires async api or data fetching to get this data.
For example, the search results from google.
Another thing to note is that server state has shared ownership i.e. it can be used in different applications and also, data can be updated by someone else without your knowledge which can lead to the UI data not being in sync with the remote data.

This becomes even more challenging when you have to do with caching, deduping multiple requests for the same data, updating state data in the background, performance optimization when it comes to pagination and lazy loading etc.

If you want to resolve all the issues, it will be time consuming and you will have to do all that yourself. Or you can just use a library which is react query.

Note that server state doesn't just about fetching It also needs updating

<ul>
<li>Basic queries</li>
<li>Poll data</li>
<li>RQ dev tools</li>
<li>Create reusable query hooks</li>
<li>Query by ID</li>
<li>Parallel queries</li>
<li>Dynamic queries</li>
<li>Dependent queries</li>
<li>Infinite and paginated queries</li>

<li>Update data using mutations</li>
<li>Invalidate</li>
<li>Optimistic updates</li>
<li>Axios interceptor</li>
</ul>

### To Begin With

Nobody wants to see an application where everything you click has to load especially when you're developing applications

### Queries

In react-query we have a hook called `useQuery` but before we get into that, we have to make sure we set up our queryclient and all

> Syntax

```jsx
// In the app.js or index.js
import { QueryClientProvider, QueryClient } from "react-query";

const App = () => {
  const queryClient = new QueryClient();
  // From the above, it can be seen that
  // QueryClient() is a class
  return (
    <QueryClientProvider client={queryClient}>
      <Home />
    </QueryClientProvider>
  );
};
```

> Probably in the home page or where you need the data,

```jsx
import { useQuery } from "react-query";

useQuery(identifier, async_function);
```

> The `identifier` is the name of the thing you are fetching

> The `async_function` is a function that fetches your data and returns an error if an error is found

```js
import { useQuery } from "react-query";

const { data } = useQuery("posts", () => {
  return axios.get("this.api.com");
});
```

> The useQuery handles the state and reducers of your async work and react-query also handles the life cycle around all of your fetching

> useQuery returns an object containing everything like the status enums, it has booleans, data property, error

What it does is that. If you've visited a page before, since it has been loaded, it won't load again. It instantly gets your data. So it keeps your data in a cache in your html so when you open the page, we see that the it automatically loads

Another thing that can be done is that we use an external function to fetch the data and put the data in the useQuery hook.

```js
const fetchData = () => {
  return axios.get("http://super-heroes.api.com/superheroes");
};
const RQSuperHeroespage = () => {
  const { isLoading, data } = useQuery("super-heroes", fetchData);
};
```

<h3>refecthOnMount</h3>
<p>
This is a boolean in the onject passed in to useQuery. <br />
By defult it is true and that is why the background refetch is triggered
anytime we go to the route
</p>
<p>
Even though the property is a boolean value, we can also pass in the
string "always" as its value. <br />
What this does is that it will make sure on every mount of the page that
the data is fetched even if a staleTime is set
</p>
<h3>refetchOnWindowFocus</h3>

    <h2>Polling data</h2>
    <p>
      This refers to fetching data at regular intervals. To do this, we use the
      refetchInterval in the object of the useQuery hook
    </p>
    <p>
      By default it is set to false (a boolean) but you can assign it to a
      number in milliseconds. So it will fetch the data after the specified
      interval. <br />
      However, it should be noted that when the window loses focus, this polling
      also stops. If you do not want it to stop, we set
      refetchIntervalInBackgroud to true
    </p>
    <h3>Events with useQuery</h3>
    <p>
      In this example, we are going to fetch data only when the button is
      clicked. <br />
      First, we set the enabled property of the useQuery object to false. <br />
      This will make sure the data won't be fetched on mount or focus
    </p>
    <p>
      To use an event like onClick, useQuery returns a function called refetch
      that we can destructure from it. This functions helps us to manually fetch
      data
    </p>
    &lt;button onClick={refetch}>&lt;/button>

    <h2>Callbacks in useQuery</h2>
    <fieldset>
      <code>
        <pre>

const onSuccess = () => {
console.log("This was a success so we want to do something else")
}

</pre>
</code>
</fieldset>
<p>
There are values that we call in the useQuery Object which are onSuccess
and onError
</p>
<p>
These two accept functions (call back) that will be called if there is
either a success or an error
</p>
<p>
Another thing to note is that react-query will automatically pass in
either the data or error to their specified functions as parameters
</p>
<h2>Data Transformation</h2>
<p>in the useQuery</p>
<fiedset>
<code>
<pre>
{
select: (response) => {
const superHeroes = response.data.map(hero +> hero.name)
return superHeroes
}
}
</pre>
</code>
</fiedset>
<p>
since the is put in the object of the usequery hook, it changes the data
that was destructured to what we exported from the select property which
in this case is superHeroes. <br />
so whenever we call the data variable that was destructured, we are
actually referring to the superHeroes array
</p>
<h2>customQuery</h2>
<p>
The above way is good especially for small apps. <br />
in larger apps, we might to use the same data fetching in another
component and this might lead us to duplicating the code and we know that
it is not right to duplicate code <br />
To fix this issue, we create custom query hooks that drags around the use
useQuery
</p>
<p>Create a new file for custom Hooks</p>
<p>
After that we just move the code for the useQuery hook into the function
</p>
<fieldset>
<code>
<pre></pre>
</code>
</fieldset>
<h3>Querying by Id</h3>
<p>
To query by id, we can actually just set the queryKey to an array with a
name and a unique id like so: <br />
<code>
<pre
          contenteditable="false"
          style="
            border: 2px solid gray;
            background-color: black;
            color: white;
            padding: 5px;
            overflow-x: scroll;
          "
        >
["superHero", heroId]
<span class="comment" style="color: gray;">//This is a very very very very very very very long comment</span>

</pre>
      </code>
    </p>
    <p>
      You should note that the when you pass a function to the useQuery hook,
      the data gotten from the query is passed as an argument and we can access
      the queryKey from destructuring it
    </p>
    <h3>Parrallel queries</h3>
    <p>
      This is useful if we want to make different requests or fetch two sets of
      data from a page. These queries run independently and run on their own
    </p>
    <p>
      When destructuring and you do this, <br />
      <code>
        <pre>
const {data: superHeroes} = useQuery("super-heroes", fetchSuperHeroes)</pre
        >
      </code>
      <br />
      What you are doing is that you are setting the data which was destructured
      to superHeroes
    </p>
    <h3>Dynamic parallel queries</h3>
    <p>
      We need to import useQueries. This returns an array of queryResults
      useQueries containing the number of times the query was made
    </p>
    <fieldset>
      <code>
        <pre>
        export const DynamicParallelPage = ({heroIds}) => {
          const queryResults = useQueries(
            heroIds.map(id => {
              return {
                queryKey: ["super-hero", id]
                queryFn: () => fetchSuperHero(id)
              }
            })
          )
        }
      </pre
        >
      </code>
    </fieldset>
    <h3>Dependent queries</h3>
    <p>
      You might need queries to be done sequentially i.e. one after the other.
      For example, we want to get the channels of a user. We have to first
      import the user.
    </p>
    <p>
      Thing i've learned... <br />
      Object chaning with ?. <br />
      Double negation !! which converts a value to a boolean
    </p>
    <h3>Initial queryData</h3>

    <fieldset>
      <code>
        <pre>

export const useSuperHeroData = heroId => {
const queryClint = useQueryClient(); //Import the hook
//The above actually has access to the cached data
return useQuery(["super-hero", heroId], fetchSuperHero, {
initialData: () => {
const hero = queryClient.getQueryData("super-heroes")?.data?.find(hero => {
hero.id === parseInt(heroId)
}

      if(hero) {
        return {
          data: hero;
        }
      } else {
        return undefined
      })
    }

})
}

</pre>
</code>
</fieldset>

  </body>
</html>
````

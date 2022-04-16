# Query Cache

When you navigate to a page in react, it fetches the data all over again irrespective of the number of times you open the link. However, if you open a link that its data was fetched with react-query, when you click the link again after you've left the page, it doesn't re-fetch the data again instead which makes UI and UX even better

This action is as a result of the query cache provided by react-query.
By default, each query result has a temporary cache storage of about 5mins

The first time useQuery is fired, isLoading is set to true and a network request is sent to fetch the data. When the data is completed, it is cached with the query key and the function as the unique identifiers

When ever we make a request, react-query will check if the data exists in cache and if it contains the data in the cache, the data is immediately rendered and the isLoading is not set to true.
Also, react-query knows that the data might be changed so it also runs a background re-fetch and passes the data to the component and if the data is the same as the cached data we do not see any change in the UI

`react-query` also provides an isFetching flag (or variable) which is the boolean for the background fetching of data after the cached data has been passed to the component

If we console.log({isLoading, isFetching}), when the request is made at first, both are true. When the data has been loaded, both then become false.

If the data is updated (or not), we will see that the cached data is displayed in the UI first and in the console, isLoading is still false but isFetching is true.

If there's a change in data, the data will then be rendered to the UI and then we will see that isFetching is then set to false

## Life of the cached data

By default, the cached data lasts for 5 minutes. To configure it, we can pass in a third argument to useQuery.
This third argument is an object contain configurations for different
properties and cacheTime is one of them

```js
const fetchData = () => {
  axios.get("http://super-heroes.api.com/superheroes");
};
const RQSuperHeroespage = () => {
  const { isLoading, data, isError, error, isFetching } = useQuery(
    "super-heroes",
    fetchData,
    {
      cacheTime: 5000,
    }
  );
};
if (isLoading) {
  return <div>React Query Super Heroes</div>;
}
if (isError) {
  return <div>{error.message}</div>;
}
```

> The unit of the time is in ms

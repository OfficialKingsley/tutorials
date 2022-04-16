# Stale time

If we do not want a backround fetch of data and we just want to use the cached data for a period of time, we configure a property called
`staleTime`.

There will be no background data fetch for as long as that staleTime

```js
const fetchData = () => {
  axios.get("http://super-heroes.api.com/superheroes");
};
const RQSuperHeroespage = () => {
  const { isLoading, data, isError, error, isFetching } = useQuery(
    "super-heroes",
    fetchData,
    {
      staleTime: 30000,
    }
  );
};
//The unit of the time is in ms
if (isLoading) {
  return <div>React Query Super Heroes</div>;
}
if (isError) {
  return <div>{error.message}</div>;
}
//The data still remains fresh in the react query dev tools
//After the stale time has elapsed,
//The background fetch will be if the link is clicked
//then the new data will still remain fresh again for anothe 30 seccs
```

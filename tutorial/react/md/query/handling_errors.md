# Handling Errors

The `useQuery` hook also returns an isError variable and an error from the api call. Therefore, we do not need to catch the error ourselves instead it is made available by react-query
We can therefore destructure the error and isError from the useQuery hook

```js
const fetchData = () => {
  axios.get("http://super-heroes.api.com/superheroes");
};
const RQSuperHeroespage = () => {
  const { isLoading, data, isError, error } = useQuery(
    "super-heroes",
    fetchData
  );
};
if (isLoading) {
  return <div>React Query Super Heroes</div>;
}
if (isError) {
  return <div>{error.message}</div>;
}
```

If there is an error, there is a higher waiting for data as react-query automatically retries to fetch the data from the api again and then if it is not found, it then returns the error message

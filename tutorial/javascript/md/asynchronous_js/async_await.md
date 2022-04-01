<!-- @format -->

# Async Await

This provides a simpler way of creating promises.

The "async" keyword applied to a function creates a new promise. The await keyword in the async function makes the function wait for the promise to be fulfilled or rejected

```js
async function myFunction() {
  return "Hello";
}
```

> The above is the same as...

```js
async function myFunction() {
  return Promise.resolve("Hello");
}

//OR

const myPromise = new Promise((res, rej) => {
  if (successful) {
    res("Hello");
  } else {
    rej("Error");
  }
});
```

Just like using promises, you can use the .then syntax

> **Note:** Make sure you always await the results from the promise if you are using async await (if not you may get errors or messages saying pending requests) otherwise if you don't want to await, you use the .then and the .catch methods

> **Also Note** that a promise always returns a value. The two functions that are passed in the resolve and reject must return values which will be passed to the consuming code afterwards

```js
const myPromise = new Promise((resolve, reject) => {
  if (condition === true) {
    resolve("This is good"); //Return this if the condition is true
  } else {
    reject("This is bad"); //Return this if the condition is bad
  }
});
myPromise
  .then((response) => {
    console.log(response); //The response refers to the data returned from the promise
    //(either the resolve or reject but in most use cases, the resolve)
  })
  .catch((err) => {
    console.log(err);
    //The err (error) refers to what was returned from the reject function
  });
```

Remember that an async function always returns a promise. So when we create an async function, we can use the .then and .catch on it

```js
const getUsers = async () => {
  const users = await axios.get("http://myDataAPI/users");
  //Note that axios also returns a promise so we had to await the response of the promise
  return users;
};

getUsers.then((response) => {
  console.log(response);
  //The response refers to the data gotten from the asynchronous getUsers function
});

const logOutUsers = async () => {
  const users = await getUsers();
  console.log(users);
};
//You see that we awaited the response from the async getUsers function
//Now, we do not have to use the .then and .catch methods
```

If we want to do the above with a promise, we will do,

```js
const myUsers = new Promise((resolve, reject) => {
  resolve(axios.get("http://myDataAPI/users"));
});

myUsers.then((response) => {
  console.log(response);
  //The response still refers to the data gotten from the API
});
```

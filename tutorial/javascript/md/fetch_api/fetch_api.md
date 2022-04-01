<!-- @format -->

# Fetch API

The fetch api is a new resource added to javascript for the fetching of data with the use of asynchronous javascript and promises

## How to use

---

Once you type `fetch("API_URL")`, this by default sends a get request. It also returns a promise so we can call the `.then()`, `.catch()` methods on it

```js
fetch("API")
  .then((response) => {
    console.log(response);
    response.json();
  })
  .then((responseData) => {
    console.log(responseData);
  });
```

The `.json()` method converts the data from json to normal javascript data and it also returns data (like the resolve method). This data can also be passed into another `.then` method for further processing. <br />
In the above case, we passed it into another then method and called it responseData.

Apart from the `.json()` method, we also have other methods like

- `.text()`

These methods also return promises, so we can add other `.then()` methods as steps.

The `.json()` method creates a promise and this promise is then attached to the chain (joining of the `.then()` methods )

The promises returned by the `.json()` and other methods like that are like when we resolve a promise. So the data from this can then be accessed by the next then method

## Using async ... await

---

<br />

```js
const getData = async () => {
  const response = await fetch("http://www.my_api_link.com/users");
  const data = await response.json();
};
```

## Specifying the type of requests and other options

---

<br />

By default, the fetch request is making get requests. However, we can
specify the type of requests of the fetch <br />
Some of the requests include:

- `GET` - This request is made to get data from the api
- `POST` - This request is made to add data or post data to the api
- `DELETE` - This is to delete data from the api
- `PUT` - This request is used to update some data in the api

<br />

## Using these request types

<br />

---

<br />

### **POST**

---

<br />

```js
const postData = async () => {
  const res = await fetch("api.link", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ message: "what you want to send" }),
  });
};
```

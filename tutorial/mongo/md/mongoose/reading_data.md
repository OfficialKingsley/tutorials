<!-- @format -->

# Reading data

## Find method

---

The find method is called on the model to look for something based on a particular query that is being passed into the find method. The second parameter is a callback that accepts the error (if any) and the the result gotten from the find method

```js
Fruit.find({ username: "King" }, (err, user) => {
  if (err) {
    log(err);
  } else {
    mongoose.connection.close;
    //This will close the database
    log(user[0]);
  }
});
```

In the above we are telling mongoose to find the user with the username of King

> The find method **always** returns data in the form of an array even if one item was found

## More on the find method

---

If no query is passed into the find method, it will return all the items in the collection

```js
Fruit.find({}, (err, fruits) => {
  if (err) {
    log(err);
  } else {
    mongoose.connection.close;
    log(fruits);
  }
});

//OR

Fruit.find((err, fruits) => {
  if (err) {
    log(err);
  } else {
    mongoose.connection.close;
    log(fruits);
  }
});
```

## Finding by id

---

> You can actually find something by its id

```js
Fruit.findById(id, (err) => {
  if (err) {
    console.log(err);
  }
});
```

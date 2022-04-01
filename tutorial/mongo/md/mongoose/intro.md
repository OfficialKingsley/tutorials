<!-- @format -->

Mongoose is an <abbr title="Object Document Mapper">ODM</abbr> which stands for object document mapper.

<br />

It allows your node js app which speaks the language of JS objects to be able to talk to your mongo DB which speaks in the language of documents
and collections and the rest

<br />

The main objective of this framework is to simplify the writing of validation code, the writing of business logic boiler plate and to make
the code shorter and easier to work with

Mongoose could be seen as jQuery to Javascript since it helps us to write shorter code for our node js app for our mongo database

## Starting up the connection

---

First of all, make sure you have an active mongo DB server running and make sure you have installed mongoose

> `npm i mongoose`

> In your nodejs app, you can type:

```js
const mongoose = require("mongoose");

mongoose.connect("/database-server-url/database-name", {
  useNewUrlParser: true,
});
//The above will connect to the database
```

## Closing the connection

---

To close a collection with mongoose, we can type this

```js
mongoose.connection.close();
```

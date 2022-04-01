<!-- @format -->

# Creating or Adding Data

To create new data, we need to create a new Schema which is basically a blueprint or the structure of the data that we're going to save into our database

```js
import mongoose from "mongoose";

const fruitSchema = new mongoose.Schema({
  name: String,
  rating: Number,
  review: String,
});

//Some do this
import { Schema } from "mongoose";

const fruitSchema = new Schema({
  name: String,
  rating: Number,
  review: String,
});
```

This is what our fruit schema would look like and this lays the foundation for every new fruit document that will be added to our database

After we create a schema, we use the schema to create a mongoose model

## Model

---

You can think of the model as the collection for your database. Since we are using mongoose, we know that this collection must follow a particular structure (schema)

#### Syntax

---

```js
//format
const type_of_document = mongoose.model(
  "singular_form_of_collection_name", schema to follow
)
const Fruit = mongoose.model("Fruit", fruitSchema)


```

This `Fruit` before the equal to sign is called a model. The `mongoose.model()` method accepts two parameters.
<br />
The first is the name of your collection. This name has to be singular and by default mongoose will pluralize the name of that collection for you.
<br />
The second parameter is the particular structure or Schema to be followed by that collection

## Creating the data

---

Now to actually create a fruit, we do the following

```js
const fruit = new Fruit({
  name: "Apple",
  rating: 7,
  review: "Pretty good fruit",
});
```

And then to finally add the fruit to the collection called Fruits, we do:

```js
fruit.save((err) => {
  if (err) {
    console.log(err);
  } else {
    console.log("successfully added");
  }
});
```

The save method accepts a call back incase of any errors encountered

## Adding multiple data

---

What if you want to add many things

```js
Fruit.insertMany([kiwi, orange, banana], (err) => {
  if (err) {
    console.log(err);
  } else {
    ("successfully added fruits");
  }
});
```

From the above, notice that when we wanted to save one fruit, we called the `fruit` object itself but when we wanted to save many fruits, we used the `Fruit` model

<!-- @format -->

# Promises

A promise object in JS is an object that contains a `producing code` and calls to the `consuming code`

The producing code is the code that can take some time. The producing code produces an output

The consuming code is the code that must wait for the results. The
consuming code then waits for the output of the producing code to then do
something with it

```js
let myPromise = new Promise(function (myResolve, myReject) {
  myResolve();
  myReject();
});
```

The `myResolve` and `myReject` functions are automatically passed into the function but we decided to call it myResolve and myReject.

The `myResolve` function is called if there's no error and the promise was successful. It often returns a value which will be passed down into the `consuming code`

The `myReject` function will be called if there's an error and this error will be returned and then passed into the consuming codes

The whole promise call is the `producing code` which often takes time to find a response

```js

myPromise.then(function(value) {
 //code if there's no error
},
function(for if not resolved){}
)
```

The `.then()` method is now the `consuming code` which has to wait for the response from the promise whether it is resolved or rejected

The `.then()` method takes in two functions as parameters. The first is the function that will be called if the response from the promise was a successful one i.e. it was produced from the `myResolve()` function <br />
The second function is called when an error is returned

## Real life Scenario of a promise

---

Assuming you have a restaurant, and a customer comes in. You make a `promise` of serving him food. If he has not yet made any order, the promise is still `pending`. Once a customer makes an order, you have to `resolve` the
promise. Resolving the promise is either `fulfilling` it (if you have the
ingredients) or `rejecting` the promise (if you don't have the ingredients).

This whole process of determining whether you will resolve or reject is the `producing code`.

The processes that occur after this "`producing code` depend on whether the promise was fulfilled or rejected. Since they depend on the result of the promise, they `await` the results of the promise, this is the `consuming code` the .thens

If the promise was fulfilled, we move on to make the food that's where the

```js
let makeFood = new Promise((resolve, reject) => {
  if (hasIngredients === true) {
    resolve(startProduction());
  } else {
    reject("Error");
  }
});
```

Now we move on to the consuming code

```js
makeFood.then(
  function (/*If resolved*/) {
    continueProduction();
  },
  function (error /*if rejected*/) {
    breakProduction();
  }
);
```

</pre></code
      >
</fieldset>

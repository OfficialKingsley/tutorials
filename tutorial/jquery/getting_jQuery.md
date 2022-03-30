<!-- @format -->

# Getting jQuery

So where do we get jQuery from?

1. You can download the jQuery folder from the [jQuery website](https://www.jquery.com/download/)

   - Using bower
     - `bower install jquery`

2. You can also use the CDN
   - Using Google's CDN (The most popular CDN)

## Where to put the CDN

It is very important to note where to put the CDN link. You can either put it in the head tag or put it just before the closing body tag

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
    <link rel="stylesheet" href="style.css" />
  </head>
  <body>
    <h1>jQuery Tutorial</h1>
    <p>
      Lorem ipsum dolor sit amet, consectetur adipisicing elit. Optio sed
      necessitatibus voluptate assumenda mollitia, cupiditate officiis deleniti
      quo provident quae consequatur magnam, obcaecati at repellat. Optio
      distinctio, dolore incidunt molestias minima porro nobis molestiae quis
      adipisci vitae ab maiores suscipit illum aliquid, exercitationem nemo
      minus nostrum, sequi ipsam sint sunt.
    </p>
    <!-- Script for the jQuery -->
    <script
      src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"
      charset="utf-8"
    ></script>
    <script src="./index.js" charset="utf-8"></script>
  </body>
</html>
```

Notice that:

---

1. The script tag for the jQuery **must come** before your javascript files
   - This is because the html reads line by line from
   - If you place your scripts before the jquery and you try to access jQuery variables, you end up getting errors like **variable not defined**

## Placing the jquery script in the head

---

Incase you want to put the script tag for your jquery in the head tag, you have to type this

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
    <link rel="stylesheet" href="style.css" />
    <!-- Script for the jQuery -->
    <script
      src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"
      charset="utf-8"
    ></script>
    <script src="./index.js" charset="utf-8"></script>
  </head>
  <body>
    <h1>jQuery Tutorial</h1>
    <p>
      Lorem ipsum dolor sit amet, consectetur adipisicing elit. Optio sed
      necessitatibus voluptate assumenda mollitia, cupiditate officiis deleniti
      quo provident quae consequatur magnam, obcaecati at repellat. Optio
      distinctio, dolore incidunt molestias minima porro nobis molestiae quis
      adipisci vitae ab maiores suscipit illum aliquid, exercitationem nemo
      minus nostrum, sequi ipsam sint sunt.
    </p>
  </body>
</html>
```

```js
//In the Javascript
$(document).ready(function () {
  $("h1").css("color", "red");
});
```

From the above, it can be seen that it's up to you to where you want to put the jQuery script

<!-- @format -->

# Basic compilation of sass

To use sass in the browser, we need to compile it down into vanilla javascript

To do this, we have a range of options like using the `live sass compiler` in vscode or using a package or task runners like gulp

## Using gulp

---

```bash
npm install gulp gulp-sass sass --save-dev
```

We now need a gulp file

> You can call this gulpfile.js

```js
const { src, dest, watch, series } = require("gulp");

const sass = require("gulp-sass")(require("sass"));

function buildStyles() {
  return src("index.scss").pipe(sass()).pipe(dest("css"));
}

//Function that watches the sass file
function watchTask() {
  watch(["index.scss"], buildStyles);
}

exports.default = series(buildStyles, watchTask);
```

> Then in the terminal we type

```
gulp
```

```js
const { src, dest, watch, series } = require("gulp");

const sass = require("gulp-sass")(require("sass"));

function buildStyles() {
  return src("library/**/*.scss").pipe(sass()).pipe(dest("css"));
}

//Function that watches the sass file
function watchTask() {
  watch(["library/**/*.scss"], buildStyles);
}

exports.default = series(buildStyles, watchTask);
```

In the above, we are telling the compiler that we want to look for files in the library folder and in any other sub folder (if there is any) to find a scss file and then compile it

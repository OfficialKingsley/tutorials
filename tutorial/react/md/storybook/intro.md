<!-- @format -->

# Introduction to md

So let's say you have some components that is not really used in any part of your app yet but you want to check out how the component looks without actually affecting the flow of our program, we can use storybook.

The interesting thing about storybook is that it works on a lot of frontend frameworks and libraries

To start a storybook, you have to first create your react-app or frontend app and then you type:

> `npx sb init`

This will also add a script called `storybook` which we can run as so:

> `npm run storybook`

This will start a local storybook server for us

> When you first initialize storybook, everything will be done in a stories folder i.e. all your work and all

## Naming convention

> `Component.stories.js`

The `.stories` is very important as you tell story book that it's a new story

# Usage

To use storybook you have to export an object which will actually be your actual story

```js
import Button from "../components/button";

export default {
  title: "Button",
  component: Button,
};
```

We need to tell story what our different stories are like we have primary, small, large

To do that, we just have to export our different stories as functions. These functions must return the component

```js
import Button from "../components/button";

export default {
  title: "Button",
  component: Button,
};

//This is a new story
export const Red = () => {
  <Button label="Press me" backgroundColor="red" />;
};
```

You will see that some text is generated if you have some prop-types

```js
// In the button component file

Button.propTypes = {
  label: PropTypes.string,
  backgroundColor: PropTypes.string,
  size: PropTypes.oneOf(["sm", "md", "lg"]),
  onClick: PropTypes.func,
};
```

## Controls

---

Normally, one of the most powerful tools of storybook is that you can customize your components and pass in different colors and props to make it very interactive

However, with the above code, that is not possible. You have to first create a template or base (function) for all your buttons so that your buttons will follow that schema

```js
import Button from "../components/button";

export default {
  title: "Button",
  component: Button,
};

// Template button

const Template = (args) => {
  <Button {...args} />;
};

//This is a new story
export const Red = Template.bind({});
Red.args = {
  backgroundColor: "red",
  label: "Press me",
  size: "md",
};
```

## ArgTypes

You can also specify what type of arguments are passed into your components

```js
export default {
  title: "Button",
  component: Button,
  argTypes: { handleClick: { action: "Name of event" } },
};
```

From the above, it can be seen that the argTypes is an object. Each key is a prop being passed to the component. The value of that specifies what that prop means. In the above case, we are saying that our handleClick prop is actually going to trigger an action and then we also passed in the name of the action

```js
import Button from "../components/button";

export default {
  title: "Button",
  component: Button,
  argTypes: { handleClick: { action: "Name of event" } },
};

// Template button

const Template = (args) => {
  <Button {...args} />;
};

//This is a new story
export const Red = Template.bind({});
Red.args = {
  backgroundColor: "red",
  label: "Press me",
  size: "md",
};

export const Green = Template.bind({});
Green.args = {
  backgroundColor: "green",
  label: "Press me",
  size: "md",
};

export const Yellow = Template.bind({});
Yellow.args = {
  backgroundColor: "yellow",
  label: "Press me",
  size: "md",
};

export const Small = Template.bind({});
Small.args = {
  backgroundColor: "red",
  label: "Press me",
  size: "sm",
};

export const Large = Template.bind({});
Large.args = {
  backgroundColor: "red",
  label: "Press me",
  size: "lg",
};

export const LongLabel = Template.bind({});
LongLabel.args = {
  backgroundColor: "red",
  label: "Press me This is a very long label for this button",
  size: "lg",
};
```

## Putting components in folders

You can arrange your code and put your storybook components in a folder

You just need to do that by changing your component name like so:

```js
import Button from "../components/button";

export default {
  title: "Components/Button",
  component: Button,
  argTypes: {
    handleClick: {
      action: "click",
    },
  },
};
```

## Stack Component

---

Created a stack component for aligning items

```js
import Stack from "../components/Stack";

export default {
  title: "Components/Stack",
  component: Stack,
  argTypes: {
    numberOfChildren: {
      type: "number",
      defaultValue: 4,
    },
  },
};

const Template = ({ numberOfChildren, ...args }) => (
  <Stack {...args}>
    {[...Array(numberOfChildren).keys()].map((n) => (
      <div
        style={{
          backgroundColor: "red",
          display: "flex",
        }}
      >
        {n + 1}
      </div>
    ))}
  </Stack>
);

export const Horizontal = Template.bind({});
Horizontal.args = {
  numberOfChildren: 15,
  direction: "row",
  spacing: 2,
  wrap: false,
};
```

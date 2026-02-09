# Bug Report

### Describe the bug

I'm experiencing an issue with destructuring assignment when using computed property names. The destructuring doesn't seem to work correctly - properties that should be extracted are coming back as undefined.

### Reproduction

```js
const obj = {
  foo: 'bar',
  baz: 'qux'
};

const key = 'foo';
const { [key]: value } = obj;

console.log(value); // Expected: 'bar', but getting undefined
```

Also seeing similar behavior with nested destructuring:

```js
const data = {
  user: {
    name: 'John',
    age: 30
  }
};

const prop = 'name';
const { user: { [prop]: userName } } = data;

console.log(userName); // Should be 'John' but is undefined
```

### Expected behavior

When using computed property names in destructuring patterns, the values should be correctly extracted from the source object. The computed property should behave the same as a static property name.

### System Info

- Rollup version: latest
- Node version: 18.x

This seems like a regression as it was working in previous versions. Any help would be appreciated!

---
Repository: /testbed

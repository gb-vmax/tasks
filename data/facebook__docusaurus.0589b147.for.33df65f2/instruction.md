# Bug Report

### Describe the bug

The `findAsyncSequential` utility function is skipping the first element of the array when searching for a match. When I pass an array where the first element should match the predicate, the function returns `undefined` instead of returning that element.

### Reproduction

```js
const items = ['apple', 'banana', 'cherry'];

const result = await findAsyncSequential(items, async (item) => {
  return item === 'apple';
});

console.log(result); // Expected: 'apple', Actual: undefined
```

If the matching element is anywhere except the first position, it works fine:

```js
const items = ['apple', 'banana', 'cherry'];

const result = await findAsyncSequential(items, async (item) => {
  return item === 'banana';
});

console.log(result); // Works correctly: 'banana'
```

### Expected behavior

The function should return the first element in the array that matches the predicate, regardless of its position. If the first element matches, it should be returned immediately.

### System Info
- Package: @docusaurus/utils
- Version: latest

---
Repository: /testbed

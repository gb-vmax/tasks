# Bug Report

### Describe the bug

The `findAsyncSequential` function is skipping the first element of the array when searching for a match. It starts iterating from index 1 instead of index 0, which means the first element is never evaluated against the predicate.

### Reproduction

```js
const items = ['apple', 'banana', 'cherry'];

const result = await findAsyncSequential(items, async (item) => {
  return item === 'apple';
});

console.log(result); // Expected: 'apple', Actual: undefined
```

When the matching element is at the beginning of the array, the function returns `undefined` instead of finding it.

### Expected behavior

The function should check all elements in the array, including the first one (index 0). If a match is found at any position, it should return that element immediately.

### System Info
- Package: @docusaurus/utils
- Node version: 18.x

---
Repository: /testbed

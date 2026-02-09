# Bug Report

### Describe the bug

The `findAsyncSequential` utility function is returning `undefined` on the first iteration instead of continuing to search through the array. It seems to exit early even when there are more elements to check.

### Reproduction

```js
const items = ['a', 'b', 'c', 'd'];

const result = await findAsyncSequential(items, async (item) => {
  return item === 'c';
});

console.log(result); // Expected: 'c', Actual: undefined
```

The function should iterate through all items until it finds a match, but it's returning `undefined` immediately after checking the first element.

### Expected behavior

The function should continue searching through the array until it finds an element that satisfies the predicate, then return that element. If no element matches, it should return `undefined` only after checking all elements.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed

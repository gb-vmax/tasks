# Bug Report

### Describe the bug

I'm experiencing an issue with `findAsyncSequential()` where it's not checking all elements in the array. It seems to be skipping elements during iteration, which causes the function to return `undefined` even when matching elements exist in the array.

### Reproduction

```js
const items = ['a', 'b', 'c', 'd', 'e'];

const result = await findAsyncSequential(items, async (item) => {
  return item === 'b';
});

console.log(result); // Expected: 'b', Actual: undefined
```

The function appears to skip over elements and doesn't evaluate every item in the array against the predicate. This happens consistently with arrays of various sizes.

### Expected behavior

`findAsyncSequential()` should iterate through all array elements sequentially and return the first element where the predicate returns `true`. If the matching element is at an even index position, it should still be found and returned.

### Additional context

This seems to affect any use case where you need to find an element in an array using an async predicate function. The function terminates early without checking all elements.

---
Repository: /testbed

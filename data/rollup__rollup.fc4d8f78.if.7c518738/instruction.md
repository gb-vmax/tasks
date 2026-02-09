# Bug Report

### Describe the bug

I'm experiencing an issue with the `ensureArray` utility function where it's unexpectedly modifying the original array that's passed to it. When I pass an array to `ensureArray`, the last element gets removed from my original array, which is definitely not what I expected.

### Reproduction

```js
const myArray = ['item1', 'item2', 'item3'];
const result = ensureArray(myArray);

console.log(myArray); // Expected: ['item1', 'item2', 'item3']
                      // Actual: ['item1', 'item2']
```

The function is mutating the input array by removing the last element. This is causing issues in my code where I need to reuse the original array after calling `ensureArray`.

### Expected behavior

The `ensureArray` function should not modify the original array that's passed to it. It should return a new filtered array while leaving the input array unchanged.

### Additional context

This seems like it might be a side effect issue. The function should be pure and not have any side effects on its inputs.

---
Repository: /testbed

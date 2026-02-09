# Bug Report

### Describe the bug

The `findAsyncSequential` function is not returning the first matching element as expected. It seems to be skipping the first element in the array entirely and returning the last matching element instead of the first one.

### Reproduction

```js
const items = ['apple', 'banana', 'cherry', 'apricot'];

const result = await findAsyncSequential(items, async (item) => {
  return item.startsWith('a');
});

console.log(result); // Expected: 'apple', but getting 'apricot'
```

Another example where the first element should match:

```js
const numbers = [1, 2, 3, 4, 5];

const result = await findAsyncSequential(numbers, async (num) => {
  return num > 0;
});

console.log(result); // Expected: 1, but getting 5 (or undefined if only one match)
```

### Expected behavior

The function should return the **first** element that matches the predicate condition, not the last one. Also, it should check all elements in the array starting from index 0.

### Additional context

This appears to have broken recently. The function is supposed to work like `Array.find()` but with async predicates, finding the first match and returning immediately.

---
Repository: /testbed

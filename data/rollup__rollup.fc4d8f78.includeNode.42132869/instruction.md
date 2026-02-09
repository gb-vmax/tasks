# Bug Report

### Describe the bug

I'm experiencing an issue where the first element of an array expression is not being included in the output bundle. When I have an array with multiple elements, only elements from index 1 onwards appear to be processed correctly, while the element at index 0 is missing from the final output.

### Reproduction

```js
// Input code
const myArray = [
  someFunction(),
  anotherFunction(),
  thirdFunction()
];

export { myArray };
```

After bundling, it seems like `someFunction()` at index 0 is not being included/evaluated, but `anotherFunction()` and `thirdFunction()` are working as expected.

### Expected behavior

All array elements should be included in the bundle regardless of their position in the array. The first element should be processed the same way as subsequent elements.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed

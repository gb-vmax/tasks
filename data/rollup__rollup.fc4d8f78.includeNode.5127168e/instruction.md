# Bug Report

### Describe the bug

I'm experiencing an issue where the first element of an array expression is not being included in the output bundle. When I have an array with multiple elements, only elements from index 1 onwards appear to be processed correctly, while the first element (index 0) is missing from the final output.

### Reproduction

```js
// Input code
const myArray = [
  someFunction(),
  anotherFunction(),
  thirdFunction()
];

// Expected output: all three function calls should be included
// Actual output: only anotherFunction() and thirdFunction() are included
// someFunction() is missing from the bundle
```

Another example:

```js
const values = [
  computeValue1(),
  computeValue2()
];

// Only computeValue2() appears in the output
// computeValue1() is not included even though it has side effects
```

### Expected behavior

All elements in an array expression should be included in the output, regardless of their position. The first element should be treated the same way as subsequent elements.

### System Info

- Rollup version: latest
- Node version: 18.x

This seems to have started happening recently. Any array literal I create is missing its first element in the bundled output.

---
Repository: /testbed

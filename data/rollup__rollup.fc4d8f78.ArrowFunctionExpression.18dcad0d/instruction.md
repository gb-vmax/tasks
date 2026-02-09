# Bug Report

### Describe the bug

I'm encountering an issue with arrow functions where the first parameter is not being processed correctly. When I use arrow functions with multiple parameters, the first parameter seems to be ignored in certain contexts.

### Reproduction

```js
const myFunction = (first, second, third) => {
  return first + second + third;
};

// The first parameter doesn't seem to be handled properly
// Expected all three parameters to be included
```

This appears to affect arrow functions specifically. Regular function declarations seem to work fine, but arrow functions with multiple parameters show unexpected behavior where the first parameter is skipped or not included as expected.

### Expected behavior

All parameters of an arrow function should be processed and included correctly, including the first parameter. The current behavior seems to skip the first parameter which breaks functions that rely on it.

### Additional context

This might be related to how arrow function parameters are being iterated over. The issue only manifests with arrow functions that have more than one parameter - single parameter arrow functions work as expected.

---
Repository: /testbed

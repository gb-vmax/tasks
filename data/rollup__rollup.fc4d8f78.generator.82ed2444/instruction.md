# Bug Report

### Describe the bug

I'm encountering an issue with generator function detection in my code. When I define a generator function and try to check if it's a generator, the property returns the opposite value of what I expect.

### Reproduction

```js
// Define a generator function
function* myGenerator() {
  yield 1;
  yield 2;
}

// Check if it's detected as a generator
// Expected: true
// Actual: false (or vice versa)
```

The `generator` property seems to be inverted - regular functions are being identified as generators and generator functions are being identified as regular functions.

### Expected behavior

Generator functions should be correctly identified with the `generator` property returning `true`, and regular functions should have this property return `false`.

### Additional context

This appears to have started happening recently. The detection logic seems to be backwards - everything is reporting the opposite of what it should be.

---
Repository: /testbed

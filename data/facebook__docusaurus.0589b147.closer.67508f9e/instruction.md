# Bug Report

### Describe the bug

I'm experiencing an issue with callback execution in the MDX compiler. When a callback function is provided to the `closer` function, it's being called even when it shouldn't be, leading to unexpected behavior and potential runtime errors.

### Reproduction

```js
// When closer is called with a callback function
const callback = (token) => {
  // This function should be called
  console.log('Processing token:', token);
};

const closeFunc = closer(callback);

// When close is invoked, the callback gets called incorrectly
// It's being invoked when the condition check fails instead of when it passes
closeFunc(someToken);
```

### Expected behavior

The callback function passed to `closer` should only be invoked when it exists and the appropriate condition is met. Currently, it appears the logic is inverted - the callback is being called when the condition is false rather than when it's true.

This causes the callback to be executed at the wrong time and potentially with incorrect or missing arguments, leading to errors in the compilation process.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed

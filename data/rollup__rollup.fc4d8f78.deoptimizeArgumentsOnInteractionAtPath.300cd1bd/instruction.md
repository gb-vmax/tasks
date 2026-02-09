# Bug Report

### Describe the bug

I'm experiencing an issue with array mutation methods where the bundler seems to be incorrectly deoptimizing arguments. When calling array methods that mutate their arguments, I'm getting unexpected behavior with the first argument being treated differently than it should be.

### Reproduction

```js
const arr = [1, 2, 3];
const callback = (item) => item * 2;

// Using array methods with callbacks
arr.forEach(callback);
arr.map(callback);

// The first argument (the array element) should be handled 
// differently from other arguments, but it seems like
// the deoptimization is being applied incorrectly
```

When methods that mutate arguments are called, the first argument gets deoptimized in a way that affects the entire bundling process. This seems to be related to how the bundler tracks which arguments can be safely optimized.

### Expected behavior

Array methods should correctly distinguish between:
1. The array itself (when methods mutate the array)
2. The callback/function arguments 
3. Other parameters

The deoptimization should only apply to the appropriate arguments based on the method's behavior.

### Additional context

This appears to affect methods that have the `mutatesArgs` flag set. The issue manifests during the tree-shaking phase where arguments aren't being tracked with the correct boundaries.

---
Repository: /testbed

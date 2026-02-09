# Bug Report

### Describe the bug

I'm encountering an issue with variable declarations that use the `using` or `await using` syntax. It seems like the variables are not being rendered correctly in the output, and they're getting removed even when they should be included.

### Reproduction

```js
// Example 1: using declaration
using resource = getResource();
console.log(resource);

// Example 2: await using declaration  
await using asyncResource = getAsyncResource();
console.log(asyncResource);
```

After bundling, the variable declarations are missing from the output even though they're being used. The code doesn't work as expected.

### Expected behavior

The `using` and `await using` declarations should be preserved in the output when the variables are referenced. The bundled code should maintain the proper disposal semantics.

### Additional context

This appears to be related to how variable declarators are being rendered. Regular `const`/`let`/`var` declarations work fine, but the explicit resource management syntax seems to have issues.

---
Repository: /testbed

# Bug Report

### Describe the bug

I'm encountering an issue where function calls with arguments are not being properly analyzed, leading to incorrect tree-shaking behavior. It appears that the last argument in a function call is not being deoptimized correctly, which can result in side effects being incorrectly removed during the build process.

### Reproduction

```js
function processData(a, b, c) {
  // Function with side effects
  console.log(a, b, c);
}

// When calling with exactly the number of parameters
processData(1, 2, 3);
```

The issue seems to occur when:
1. A function is called with arguments matching the parameter count
2. The last argument has side effects that should be preserved
3. The bundler incorrectly optimizes away the effects of the last argument

### Expected behavior

All arguments passed to a function should be properly tracked and deoptimized to ensure side effects are preserved. The last argument should receive the same treatment as other arguments in the call.

### Additional context

This appears to be related to how arguments are iterated during the deoptimization process. The problem manifests when the argument count exactly matches the parameter count, causing the final argument to be skipped during analysis.

---
Repository: /testbed

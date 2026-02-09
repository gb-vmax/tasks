# Bug Report

### Describe the bug

I'm experiencing an issue with accessing properties on global variables. When trying to access nested properties on globals like `Math.PI` or `console.log`, the bundler isn't correctly resolving the literal values at the specified path.

### Reproduction

```js
// Example code that demonstrates the issue
const value = Math.PI;
console.log(value);

// Or accessing methods on global objects
const logFn = console.log;
logFn('test');
```

When bundling code that accesses properties on global objects, the path resolution seems to be off by one level. It appears that the first element of the path is being skipped incorrectly, causing the bundler to look up the wrong property path on the global object.

### Expected behavior

The bundler should correctly resolve literal values for properties accessed on global variables. For example, accessing `Math.PI` should return the actual numeric value, and accessing `console.log` should properly identify it as a global method.

### Additional context

This seems to affect any code that accesses properties or methods on built-in global objects. The path traversal logic might not be handling the global object name correctly when constructing the lookup path.

---
Repository: /testbed

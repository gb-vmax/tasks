# Bug Report

### Describe the bug

I'm encountering an issue with named function expressions when they are immediately invoked (IIFE pattern). It seems like the function name is not being handled correctly in certain scenarios.

### Reproduction

```js
// This IIFE with a named function expression behaves unexpectedly
(function myFunc() {
  console.log('test');
})();

// The function name 'myFunc' should only be accessible within the function scope
// but something seems off with how it's being tracked
```

When using a named function expression as an IIFE, the scoping or variable tracking doesn't work as expected. This affects tree-shaking and dead code elimination in some cases.

### Expected behavior

Named function expressions used as IIFEs should be properly recognized and their identifiers should be scoped correctly to the function body only. The bundler should correctly identify when these are only used as function calls.

### Additional context

This seems to affect how the AST handles the relationship between:
- The function's identifier scope
- Whether the function is being called immediately
- How the function name variable is tracked

The issue appears when checking if a named function expression is an IIFE - there might be a logic error in determining this condition.

---
Repository: /testbed

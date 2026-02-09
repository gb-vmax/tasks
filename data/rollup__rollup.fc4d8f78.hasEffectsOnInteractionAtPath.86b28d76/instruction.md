# Bug Report

### Describe the bug

I'm experiencing an issue where function calls are not being tracked correctly for side effects. When calling a function that's returned from another function call, the side effect detection seems to be inconsistent.

### Reproduction

```js
// Example scenario
const result = getFactory()();

// The side effects of the inner call aren't being detected properly
// This affects tree-shaking and dead code elimination
```

The problem appears when you have a function that returns another function, and you immediately invoke the returned function. The bundler doesn't seem to correctly track whether this pattern has side effects.

### Expected behavior

The bundler should correctly identify and track side effects for both the outer function call and the returned function invocation. Code with side effects should not be eliminated during tree-shaking.

### Additional context

This seems to affect scenarios where:
- A function returns another function that is immediately called
- The returned function has side effects
- Tree-shaking is enabled

The issue might be related to how the context is being tracked for nested call expressions.

---
Repository: /testbed
